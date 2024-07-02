import tensorflow as tf
import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k
        
    def fit(self, X_train, y_train):
        self.X_train = tf.constant(X_train, dtype=tf.float32)
        self.y_train = tf.constant(y_train, dtype=tf.int32)
        
    def predict(self, X_test):
        X_test = tf.constant(X_test, dtype=tf.float32)
        predictions = []
        
        for x in X_test:
            distances = tf.reduce_sum((self.X_train - x)**2, axis=1)
            _, indices = tf.math.top_k(-distances, k=self.k)
            k_nearest_labels = tf.gather(self.y_train, indices)
            prediction = tf.reduce_mode(k_nearest_labels, axis=0).values.numpy()
            predictions.append(prediction)
        
        return predictions

# 模拟数据
X_train = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y_train = np.array([0, 0, 1, 1, 0, 1])
X_test = np.array([[1, 3], [8, 9], [0, 3], [5, 4]])

# 创建KNN模型实例
knn = KNN(k=3)
knn.fit(X_train, y_train)

# 预测
predictions = knn.predict(X_test)
print("预测结果:", predictions)
