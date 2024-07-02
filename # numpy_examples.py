# numpy_examples.py
'''
创建数组: np.array([1, 2, 3, 4, 5])
创建二维数组: np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
数组形状: arr_2d.shape
数组重塑: arr_2d.reshape((1, 9))
数组转置: arr_2d.T
数组类型: arr.dtype
创建全零数组: np.zeros((3, 3))
创建全一数组: np.ones((2, 2))
创建单位矩阵: np.eye(3)
数组加法: arr + np.array([5, 5, 5, 5, 5])
数组乘法: arr * 2
数组点积: np.dot(arr_2d, arr_2d)
数组索引: arr[2]
切片: arr[1:4]
条件筛选: arr[arr > 3]
求和: np.sum(arr)
求均值: np.mean(arr)
求标准差: np.std(arr)
求最大值: np.max(arr)
求最小值: np.min(arr)
随机数数组: np.random.rand(3, 3)
'''

import numpy as np

def main():
    # 创建数组
    arr = np.array([1, 2, 3, 4, 5])
    print("Original Array:")
    print(arr)
    
    # 创建二维数组
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\n2D Array:")
    print(arr_2d)
    
    # 数组形状
    print("\nShape of 2D Array:")
    print(arr_2d.shape)
    
    # 数组重塑
    arr_reshaped = arr_2d.reshape((1, 9))
    print("\nReshaped Array (1x9):")
    print(arr_reshaped)
    
    # 数组转置
    arr_transposed = arr_2d.T
    print("\nTransposed 2D Array:")
    print(arr_transposed)
    
    # 数组类型
    print("\nData Type of Array:")
    print(arr.dtype)
    
    # 创建全零数组
    zeros_arr = np.zeros((3, 3))
    print("\nZeros Array (3x3):")
    print(zeros_arr)
    
    # 创建全一数组
    ones_arr = np.ones((2, 2))
    print("\nOnes Array (2x2):")
    print(ones_arr)
    
    # 创建单位矩阵
    eye_arr = np.eye(3)
    print("\nIdentity Matrix (3x3):")
    print(eye_arr)
    
    # 数组加法
    arr_sum = arr + np.array([5, 5, 5, 5, 5])
    print("\nArray Sum:")
    print(arr_sum)
    
    # 数组乘法
    arr_product = arr * 2
    print("\nArray Product:")
    print(arr_product)
    
    # 数组点积
    dot_product = np.dot(arr_2d, arr_2d)
    print("\nDot Product of 2D Array:")
    print(dot_product)
    
    # 数组索引
    print("\nElement at Index 2:")
    print(arr[2])
    
    # 切片
    print("\nSlice of Array (Index 1 to 3):")
    print(arr[1:4])
    
    # 条件筛选
    print("\nElements Greater Than 3:")
    print(arr[arr > 3])
    
    # 求和
    print("\nSum of Array:")
    print(np.sum(arr))
    
    # 求均值
    print("\nMean of Array:")
    print(np.mean(arr))
    
    # 求标准差
    print("\nStandard Deviation of Array:")
    print(np.std(arr))
    
    # 求最大值
    print("\nMax Value of Array:")
    print(np.max(arr))
    
    # 求最小值
    print("\nMin Value of Array:")
    print(np.min(arr))
    
    # 随机数数组
    random_arr = np.random.rand(3, 3)
    print("\nRandom Array (3x3):")
    print(random_arr)

if __name__ == "__main__":
    main()
