import numpy as np

def pca(X, num_components):
    # 数据标准化
    X_meaned = X - np.mean(X, axis=0)
    
    # 计算协方差矩阵
    cov_matrix = np.cov(X_meaned, rowvar=False)
    
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # 对特征值排序，并选择前 num_components 个主成分
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, sorted_indices]
    eigenvalues = eigenvalues[sorted_indices]
    
    # 选择前 num_components 个主成分
    components = eigenvectors[:, :num_components]
    
    # 投影数据到新的空间
    projected_data = np.dot(X_meaned, components)
    
    return projected_data, components, eigenvalues

# 测试数据
np.random.seed(0)
X = np.random.rand(10, 4)  # 生成一个10x4的随机数据矩阵

# 执行PCA降维到2维
num_components = 2
projected_data, components, eigenvalues = pca(X, num_components)

# 输出结果
print("原始数据矩阵 X:")
print(X)
print("\n降维后的数据矩阵:")
print(projected_data)
print("\n前 %d 个主成分：" % num_components)
print(components)
print("\n对应的特征值：")
print(eigenvalues)
