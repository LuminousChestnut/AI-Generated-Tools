import numpy as np

# 定义sigmoid激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 定义BP神经网络类
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 初始化权重和偏置
        self.W1 = np.random.randn(hidden_size, input_size)
        self.b1 = np.zeros((hidden_size, 1))
        self.W2 = np.random.randn(output_size, hidden_size)
        self.b2 = np.zeros((output_size, 1))
    
    def forward(self, X):
        # 前向传播计算输出
        self.Z1 = np.dot(self.W1, X) + self.b1
        self.A1 = sigmoid(self.Z1)
        self.Z2 = np.dot(self.W2, self.A1) + self.b2
        self.A2 = sigmoid(self.Z2)
        return self.A2
    
    def backward(self, X, y, learning_rate):
        m = X.shape[1]  # 训练样本数
        
        # 计算输出层的误差和梯度
        dZ2 = self.A2 - y
        dW2 = np.dot(dZ2, self.A1.T) / m
        db2 = np.sum(dZ2, axis=1, keepdims=True) / m
        
        # 计算隐藏层的误差和梯度
        dZ1 = np.dot(self.W2.T, dZ2) * sigmoid_derivative(self.A1)
        dW1 = np.dot(dZ1, X.T) / m
        db1 = np.sum(dZ1, axis=1, keepdims=True) / m
        
        # 更新权重和偏置
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # 前向传播
            predictions = self.forward(X)
            
            # 反向传播
            self.backward(X, y, learning_rate)
            
            # 计算损失
            loss = np.mean(-y * np.log(predictions) - (1 - y) * np.log(1 - predictions))
            
            # 每1000次迭代打印一次损失
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
    
    def predict(self, X):
        # 进行预测
        predictions = self.forward(X)
        return (predictions > 0.5).astype(int)

# 模拟数据
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).T  # 输入数据
y = np.array([[0, 1, 1, 0]])  # 输出数据

# 创建BP神经网络实例
input_size = X.shape[0]
hidden_size = 4
output_size = y.shape[0]
nn = NeuralNetwork(input_size, hidden_size, output_size)

# 训练神经网络
nn.train(X, y, epochs=10000, learning_rate=0.1)

# 进行预测
predictions = nn.predict(X)
print("预测结果:", predictions)
