import numpy as np

class RBFNetwork:
    def __init__(self, input_dim, num_centers, output_dim):
        self.input_dim = input_dim
        self.num_centers = num_centers
        self.output_dim = output_dim
        self.centers = np.random.uniform(-1, 1, (self.num_centers, self.input_dim))
        self.beta = 2  # 参数beta用于控制高斯函数的宽度
        self.weights = np.random.randn(self.num_centers, self.output_dim)
    
    def _gaussian(self, x, c):
        return np.exp(-self.beta * np.linalg.norm(x - c) ** 2)
    
    def _basis_function(self, X):
        G = np.zeros((X.shape[0], self.num_centers))
        for i, x in enumerate(X):
            for j, c in enumerate(self.centers):
                G[i, j] = self._gaussian(x, c)
        return G
    
    def fit(self, X, y):
        G = self._basis_function(X)
        self.weights = np.dot(np.linalg.pinv(G), y)
    
    def predict(self, X):
        G = self._basis_function(X)
        return np.dot(G, self.weights)

# 测试数据
np.random.seed(0)
X = np.random.rand(10, 1)  # 输入数据
y = np.sin(2 * np.pi * X) + 0.1 * np.random.randn(10, 1)  # 输出数据

# 创建RBF网络实例
input_dim = 1
num_centers = 10
output_dim = 1
rbf_net = RBFNetwork(input_dim, num_centers, output_dim)

# 训练RBF网络
rbf_net.fit(X, y)

# 预测
predictions = rbf_net.predict(X)

# 输出结果
print("输入数据 X:")
print(X)
print("\n实际输出 y:")
print(y)
print("\n预测输出:")
print(predictions)
