import numpy as np
import tensorflow as tf

# 定义模拟数据
# 假设输入数据 X 的形状为 (样本数, 时间步长, 特征数)
# 假设输出数据 Y 的形状为 (样本数, 输出特征数)
X = np.random.randn(100, 10, 5)  # 100个样本，每个样本有10个时间步长，每步长5个特征
Y = np.random.randn(100, 1)     # 每个样本对应一个输出特征

# 定义简单的LSTM模型
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, return_sequences=False, input_shape=(10, 5)),  # LSTM层，隐藏单元数50
    tf.keras.layers.Dense(1)  # 全连接层，输出维度为1
])

# 编译模型
model.compile(optimizer='adam', loss='mse')

# 训练模型
model.fit(X, Y, epochs=10, batch_size=32)

# 使用模型进行预测
predictions = model.predict(X[:1])  # 预测第一个样本的输出
print("预测结果：", predictions)
