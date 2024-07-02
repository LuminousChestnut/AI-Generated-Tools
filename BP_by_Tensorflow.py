import tensorflow as tf
import numpy as np

# 模拟数据
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y = np.array([[0], [1], [1], [0]], dtype=np.float32)

# 定义神经网络模型
class NeuralNet(tf.keras.Model):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.dense1 = tf.keras.layers.Dense(4, activation='sigmoid')
        self.dense2 = tf.keras.layers.Dense(4, activation='sigmoid')
        self.dense3 = tf.keras.layers.Dense(1, activation='sigmoid')
    
    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)
        return x

# 初始化模型、损失函数和优化器
model = NeuralNet()
criterion = tf.keras.losses.BinaryCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.1)

# 编译模型
model.compile(optimizer=optimizer, loss=criterion)

# 训练模型
model.fit(X, y, epochs=10000, verbose=0)

# 测试模型
predictions = model.predict(X).round()
print("预测结果:", predictions.astype(int))
