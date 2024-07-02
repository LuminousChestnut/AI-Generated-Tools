import requests

def download_file(url, save_path):
    try:
        # 发送GET请求
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200:
            # 保存文件
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"文件已成功下载到：{save_path}")
        else:
            print(f"下载失败：HTTP 状态码 {response.status_code}")
    except Exception as e:
        print(f"下载失败：{str(e)}")

# 示例用法
if __name__ == "__main__":
    file_url = 'https://example.com/path/to/file.zip'  # 替换为实际的文件下载链接
    save_location = './downloaded_file.zip'  # 保存路径和文件名
    
    download_file(file_url, save_location)
