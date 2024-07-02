import torch
import torch.nn as nn
import numpy as np

# 定义一个简单的LSTM模型类
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.linear = nn.Linear(hidden_size, output_size)
    
    def forward(self, input_seq):
        lstm_out, _ = self.lstm(input_seq.view(len(input_seq), 1, -1))
        output = self.linear(lstm_out[-1])
        return output

# 模拟数据
input_size = 5
hidden_size = 10
output_size = 1
sequence_length = 10
batch_size = 1

# 创建模型实例
model = LSTMModel(input_size, hidden_size, output_size)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 模拟训练数据
input_seq = torch.tensor(np.random.randn(sequence_length, input_size), dtype=torch.float32)
target = torch.tensor(np.random.randn(output_size), dtype=torch.float32)

# 训练模型
num_epochs = 1000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    output = model(input_seq)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 使用模型进行预测
input_seq_pred = torch.tensor(np.random.randn(sequence_length, input_size), dtype=torch.float32)
with torch.no_grad():
    predicted = model(input_seq_pred)
    print("预测结果：", predicted.numpy())
