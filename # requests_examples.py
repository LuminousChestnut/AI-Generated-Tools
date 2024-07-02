# requests_examples.py

import requests

def main():
    # 发送GET请求并获取响应
    response = requests.get('https://api.github.com')
    print("Status Code:", response.status_code)
    print("Response Content:")
    print(response.content.decode('utf-8'))

    # 发送带参数的GET请求
    params = {'q': 'requests+language:python'}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    print("\nGitHub Repositories (Python):")
    for repo in response.json()['items']:
        print(f"{repo['name']}: {repo['html_url']}")

    # 发送POST请求
    data = {'username': 'testuser', 'password': 'testpass'}
    response = requests.post('https://httpbin.org/post', data=data)
    print("\nPOST Request Response:")
    print(response.json())

    # 发送带请求头的GET请求
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get('https://api.github.com', headers=headers)
    print("\nCustom Header Response:")
    print(response.json())

    # 处理异常情况
    try:
        response = requests.get('https://invalid-url')
        response.raise_for_status()  # 抛出HTTP错误
    except requests.exceptions.RequestException as e:
        print("\nRequest Exception:", e)

if __name__ == "__main__":
    main()
