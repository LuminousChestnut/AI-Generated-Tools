# beautifulsoup_examples.py

from bs4 import BeautifulSoup
import requests

def main():
    # 要解析的HTML内容示例
    html_content = """
    <html>
    <head>
        <title>BeautifulSoup Examples</title>
    </head>
    <body>
        <h1>BeautifulSoup Library</h1>
        <p class="intro">BeautifulSoup is a Python library for parsing HTML and XML documents.</p>
        <ul>
            <li><a href="https://www.crummy.com/software/BeautifulSoup/">BeautifulSoup Documentation</a></li>
            <li><a href="https://github.com/waylan/beautifulsoup">BeautifulSoup GitHub Repository</a></li>
        </ul>
        <div id="images">
            <img src="image1.jpg" alt="Image 1">
            <img src="image2.jpg" alt="Image 2">
        </div>
    </body>
    </html>
    """
    
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找标签
    print("Find tag by name:")
    h1_tag = soup.find('h1')
    print(h1_tag)
    
    # 查找所有标签
    print("\nFind all tags:")
    all_a_tags = soup.find_all('a')
    for tag in all_a_tags:
        print(tag.get('href'))

    # 获取属性
    print("\nGet tag attributes:")
    img_tag = soup.find('img')
    print(img_tag['src'])

    # 查找特定属性值
    print("\nFind tag by attribute value:")
    class_intro_tag = soup.find(class_='intro')
    print(class_intro_tag)

    # 查找特定ID的元素
    print("\nFind element by ID:")
    images_div = soup.find(id='images')
    print(images_div)

if __name__ == "__main__":
    main()
