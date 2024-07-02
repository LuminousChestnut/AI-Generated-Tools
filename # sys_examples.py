# sys_examples.py

import sys

def main():
    # 获取 Python 解释器的路径
    print("Python Interpreter Path:")
    print(sys.executable)
    
    # 获取命令行参数
    print("\nCommand Line Arguments:")
    print(sys.argv)
    
    # 获取 Python 版本信息
    print("\nPython Version:")
    print(sys.version)
    
    # 获取平台信息
    print("\nPlatform:")
    print(sys.platform)
    
    # 获取模块搜索路径
    print("\nModule Search Path:")
    print(sys.path)
    
    # 退出程序
    print("\nExiting Program...")
    sys.exit(0)

if __name__ == "__main__":
    main()
