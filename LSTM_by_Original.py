import numpy as np

# 定义sigmoid激活函数和其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 定义tanh激活函数和其导数
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - x**2

# 定义LSTM类
class LSTM:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 初始化权重和偏置
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.bf = np.zeros((hidden_size, 1))
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.bi = np.zeros((hidden_size, 1))
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.bc = np.zeros((hidden_size, 1))
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)
        self.bo = np.zeros((hidden_size, 1))
        
        self.Wy = np.random.randn(output_size, hidden_size)
        self.by = np.zeros((output_size, 1))
        
        # 初始化记忆细胞和隐藏状态
        self.ct = np.zeros((hidden_size, 1))
        self.ht = np.zeros((hidden_size, 1))
    
    def forward(self, xt, ht_1, ct_1):
        # 合并输入和上一个时间步的隐藏状态
        a = np.concatenate((ht_1, xt), axis=0)
        
        # 遗忘门
        ft = sigmoid(np.dot(self.Wf, a) + self.bf)
        
        # 输入门
        it = sigmoid(np.dot(self.Wi, a) + self.bi)
        
        # 更新记忆细胞
        cct = tanh(np.dot(self.Wc, a) + self.bc)
        ct = ft * ct_1 + it * cct
        
        # 输出门
        ot = sigmoid(np.dot(self.Wo, a) + self.bo)
        
        # 更新隐藏状态
        ht = ot * tanh(ct)
        
        # 输出预测
        yt = np.dot(self.Wy, ht) + self.by
        
        # 保存中间变量以备反向传播使用
        self.xt = xt
        self.ht_1 = ht_1
        self.ct_1 = ct_1
        self.ft = ft
        self.it = it
        self.cct = cct
        self.ct = ct
        self.ot = ot
        self.ht = ht
        
        return yt
    
    def backward(self, dL_dy, learning_rate):
        # 计算损失函数关于输出层权重的梯度
        dL_dWy = np.dot(dL_dy, self.ht.T)
        dL_dby = dL_dy
        
        # 计算损失函数关于隐藏状态的梯度
        dL_dht = np.dot(self.Wy.T, dL_dy)
        dL_dot = dL_dht * tanh(self.ct)
        dL_dct = dL_dht * self.ot * tanh_derivative(tanh(self.ct))
        
        # 计算损失函数关于输出门的梯度
        dL_dWo = dL_dot * sigmoid_derivative(self.ot)
        dL_dbo = dL_dot * sigmoid_derivative(self.ot)
        
        # 计算损失函数关于记忆细胞的梯度
        dL_dct += dL_dct
        dL_dft = dL_dct * self.ct_1
        dL_dit = dL_dct * self.cct
        dL_dcct = dL_dct * self.it
        
        # 计算损失函数关于遗忘门的梯度
        dL_dWf = dL_dft * sigmoid_derivative(self.ft)
        dL_dbf = dL_dft * sigmoid_derivative(self.ft)
        
        # 计算损失函数关于输入门的梯度
        dL_dWi = dL_dit * sigmoid_derivative(self.it)
        dL_dbi = dL_dit * sigmoid_derivative(self.it)
        
        # 计算损失函数关于更新门的梯度
        dL_dWc = dL_dcct * tanh_derivative(self.cct)
        dL_dbc = dL_dcct * tanh_derivative(self.cct)
        
        # 更新权重和偏置
        self.Wy -= learning_rate * dL_dWy
        self.by -= learning_rate * dL_dby
        self.Wo -= learning_rate * dL_dWo
        self.bo -= learning_rate * dL_dbo
        self.Wf -= learning_rate * dL_dWf
        self.bf -= learning_rate * dL_dbf
        self.Wi -= learning_rate * dL_dWi
        self.bi -= learning_rate * dL_dbi
        self.Wc -= learning_rate * dL_dWc
        self.bc -= learning_rate * dL_dbc
        
        return dL_dht, dL_dct

# 模拟数据
X = np.random.randn(10, 5)  # 输入数据 X 的形状为 (时间步长, 特征数)
Y = np.random.randn(1, 1)   # 输出数据 Y 的形状为 (输出特征数,)

# 创建模型实例
input_size = 5
hidden_size = 10
output_size = 1
model = LSTM(input_size, hidden_size, output_size)

# 前向传播
for t in range(len(X)):
    xt = X[t].reshape((input_size, 1))
    ht_1 = model.ht
    ct_1 = model.ct
    yt = model.forward(xt, ht_1, ct_1)

# 计算损失和反向传播
loss = np.square(yt - Y).sum()
dL_dy = 2.0 * (yt - Y)
dL_dht, dL_dct = model.backward(dL_dy, learning_rate=0.1)

print("预测输出：", yt)
print("损失：", loss)
