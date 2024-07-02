'''
运用库
	pip install pillow base64


代码说明

    函数 image_to_base64(image_path)：
        打开指定路径的图片文件，并以二进制模式读取文件内容。
        使用 base64.b64encode 方法对图片文件内容进行Base64编码，并将结果转换为字符串返回。

    函数 base64_to_image(base64_string, output_path)：
        使用 base64.b64decode 方法对Base64字符串进行解码，得到图片的二进制数据。
        使用 PIL.Image.open 方法打开二进制数据，并将图片保存到指定的输出路径。

    主程序：
        指定输入图片文件路径和输出图片文件路径。
        调用 image_to_base64 函数将图片编码为Base64字符串，并打印编码结果。
        调用 base64_to_image 函数将Base64字符串解码回图片，并保存到指定的输出路径。

使用方法

    将上述代码保存为一个Python文件，例如 base64_image.py。
    确保你的图片文件路径正确（替换示例中的 example.png 和 decoded_image.png）。
    运行Python文件：
'''


import base64
from PIL import Image
from io import BytesIO

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def base64_to_image(base64_string, output_path):
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    image.save(output_path)

if __name__ == "__main__":
    image_path = "example.png"  # 将此替换为你的图片文件路径
    output_path = "decoded_image.png"  # 将此替换为解码后的图片文件路径

    # 将图片编码为Base64
    encoded_string = image_to_base64(image_path)
    print("Encoded Base64 string:")
    print(encoded_string)

    # 将Base64字符串解码为图片
    base64_to_image(encoded_string, output_path)
    print(f"Decoded image saved to {output_path}")
