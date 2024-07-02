# pandas_examples.py
'''
查看前几行: head()
查看后几行: tail()
获取描述性统计信息: describe()
获取 DataFrame 的信息: info()
选择一列: df['A']
选择多列: df[['A', 'B']]
选择行（按位置）: iloc
选择行（按标签）: loc
选择子集: df.loc[1:3, ['A', 'B']]
添加新列: df['D'] = df['A'] + df['B']
删除列: df.drop('D', axis=1, inplace=True)
筛选数据: df[df['A'] > 2]
分组聚合: df.groupby('A').sum()
重设索引: df.reset_index(drop=True, inplace=True)
设置新的索引: df.set_index('A', inplace=True)
排序: df.sort_values(by='B', ascending=False, inplace=True)
处理缺失值: dropna(), fillna()
'''

import pandas as pd

def main():
    # 创建一个示例 DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # 查看前几行
    print("\nHead of DataFrame:")
    print(df.head(3))
    
    # 查看后几行
    print("\nTail of DataFrame:")
    print(df.tail(3))
    
    # 获取 DataFrame 的描述性统计信息
    print("\nDescriptive Statistics:")
    print(df.describe())
    
    # 获取 DataFrame 的信息
    print("\nDataFrame Info:")
    df.info()
    
    # 选择一列
    print("\nSelect Column 'A':")
    print(df['A'])
    
    # 选择多列
    print("\nSelect Columns 'A' and 'B':")
    print(df[['A', 'B']])
    
    # 选择行（按位置）
    print("\nSelect Row at Index 2:")
    print(df.iloc[2])
    
    # 选择行（按标签）
    print("\nSelect Row at Label 2 (index-based):")
    print(df.loc[2])
    
    # 选择子集
    print("\nSelect Subset (Rows 1 to 3, Columns 'A' and 'B'):")
    print(df.loc[1:3, ['A', 'B']])
    
    # 添加新列
    df['D'] = df['A'] + df['B']
    print("\nDataFrame after Adding Column 'D':")
    print(df)
    
    # 删除列
    df.drop('D', axis=1, inplace=True)
    print("\nDataFrame after Dropping Column 'D':")
    print(df)
    
    # 筛选数据
    print("\nFilter Rows where Column 'A' > 2:")
    print(df[df['A'] > 2])
    
    # 分组聚合
    print("\nGroup by Column 'A' and Calculate Sum:")
    print(df.groupby('A').sum())
    
    # 重设索引
    df.reset_index(drop=True, inplace=True)
    print("\nDataFrame after Resetting Index:")
    print(df)
    
    # 设置新的索引
    df.set_index('A', inplace=True)
    print("\nDataFrame after Setting New Index to Column 'A':")
    print(df)
    
    # 排序
    df.sort_values(by='B', ascending=False, inplace=True)
    print("\nDataFrame after Sorting by Column 'B' in Descending Order:")
    print(df)
    
    # 处理缺失值
    df_with_nan = df.copy()
    df_with_nan.loc[2, 'B'] = pd.NA
    print("\nDataFrame with NaN:")
    print(df_with_nan)
    print("\nDrop Rows with NaN:")
    print(df_with_nan.dropna())
    print("\nFill NaN with 0:")
    print(df_with_nan.fillna(0))

if __name__ == "__main__":
    main()
