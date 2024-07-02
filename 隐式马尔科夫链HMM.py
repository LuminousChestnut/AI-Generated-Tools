import numpy as np

class HiddenMarkovModel:
    def __init__(self, num_states, num_observations):
        self.num_states = num_states
        self.num_observations = num_observations
        self.start_prob = np.full(num_states, 1.0 / num_states)
        self.trans_prob = np.full((num_states, num_states), 1.0 / num_states)
        self.emission_prob = np.full((num_states, num_observations), 1.0 / num_observations)

    def _forward(self, observations):
        T = len(observations)
        alpha = np.zeros((T, self.num_states))
        alpha[0] = self.start_prob * self.emission_prob[:, observations[0]]
        
        for t in range(1, T):
            for j in range(self.num_states):
                alpha[t, j] = np.sum(alpha[t - 1] * self.trans_prob[:, j]) * self.emission_prob[j, observations[t]]
        
        return alpha

    def _backward(self, observations):
        T = len(observations)
        beta = np.zeros((T, self.num_states))
        beta[T - 1] = np.ones(self.num_states)
        
        for t in range(T - 2, -1, -1):
            for i in range(self.num_states):
                beta[t, i] = np.sum(self.trans_prob[i, :] * self.emission_prob[:, observations[t + 1]] * beta[t + 1])
        
        return beta

    def _baum_welch(self, observations, max_iter=100):
        T = len(observations)
        
        for _ in range(max_iter):
            alpha = self._forward(observations)
            beta = self._backward(observations)

            xi = np.zeros((T - 1, self.num_states, self.num_states))
            for t in range(T - 1):
                denom = np.sum(alpha[t] * beta[t])
                for i in range(self.num_states):
                    numer = alpha[t, i] * self.trans_prob[i, :] * self.emission_prob[:, observations[t + 1]] * beta[t + 1]
                    xi[t, i, :] = numer / denom
            
            gamma = np.sum(xi, axis=2)

            self.start_prob = gamma[0] / np.sum(gamma[0])

            for i in range(self.num_states):
                for j in range(self.num_states):
                    numer = np.sum(xi[:, i, j])
                    denom = np.sum(gamma[:, i])
                    self.trans_prob[i, j] = numer / denom
            
            gamma = np.vstack((gamma, np.sum(xi[-1, :, :], axis=0)))

            for k in range(self.num_observations):
                numer = np.sum(gamma[observations == k], axis=0)
                denom = np.sum(gamma, axis=0)
                self.emission_prob[:, k] = numer / denom

    def fit(self, observations, max_iter=100):
        self._baum_welch(observations, max_iter)

    def predict(self, observations):
        alpha = self._forward(observations)
        return np.argmax(alpha, axis=1)

# 测试数据
num_states = 2
num_observations = 3
observations = np.array([0, 1, 2, 1, 0])

# 创建HMM模型实例
hmm = HiddenMarkovModel(num_states, num_observations)

# 训练HMM模型
hmm.fit(observations, max_iter=100)

# 输出模型参数
print("初始状态概率:")
print(hmm.start_prob)
print("\n状态转移概率:")
print(hmm.trans_prob)
print("\n观测概率:")
print(hmm.emission_prob)

# 使用模型预测隐藏状态
predicted_states = hmm.predict(observations)
print("\n预测的隐藏状态序列:")
print(predicted_states)
