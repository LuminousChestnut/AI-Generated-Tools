# os_examples.py

import os

def main():
    # 获取当前工作目录
    print("Current Working Directory:")
    print(os.getcwd())
    
    # 列出目录中的文件和子目录
    print("\nList Files and Directories in Current Directory:")
    print(os.listdir())
    
    # 创建目录
    new_dir = "test_dir"
    os.mkdir(new_dir)
    print(f"\nCreated Directory: {new_dir}")
    
    # 重命名文件或目录
    os.rename(new_dir, "new_test_dir")
    print("\nRenamed Directory to 'new_test_dir'")
    
    # 删除目录
    os.rmdir("new_test_dir")
    print("\nDeleted Directory 'new_test_dir'")
    
    # 检查文件或目录是否存在
    print("\nCheck if File/Directory Exists:")
    print(os.path.exists("os_examples.py"))
    print(os.path.exists("nonexistent_file.txt"))
    
    # 获取文件大小
    file_size = os.path.getsize("os_examples.py")
    print("\nSize of 'os_examples.py':", file_size, "bytes")
    
    # 获取文件或目录的最后访问时间和修改时间
    file_stats = os.stat("os_examples.py")
    print("\nFile Stats:")
    print("Last Access Time:", file_stats.st_atime)
    print("Last Modified Time:", file_stats.st_mtime)
    
    # 拼接路径
    path = os.path.join(os.getcwd(), "data", "file.txt")
    print("\nJoined Path:", path)
    
    # 获取文件名和目录名
    print("\nFile Name:", os.path.basename(path))
    print("Directory Name:", os.path.dirname(path))
    
    # 分割文件名和扩展名
    filename, file_extension = os.path.splitext("file.txt")
    print("\nFile Name:", filename)
    print("File Extension:", file_extension)

if __name__ == "__main__":
    main()
