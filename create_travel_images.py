import os
import requests
from PIL import Image, ImageDraw, ImageFont
import io

def create_placeholder_image(width, height, bg_color, text, text_color=(255, 255, 255)):
    """创建占位图片"""
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 尝试使用系统字体
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            font = ImageFont.truetype("simhei.ttf", 40)
        except:
            font = ImageFont.load_default()
    
    # 计算文本位置
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # 绘制文本
    draw.text((x, y), text, fill=text_color, font=font)
    return image

def download_or_create_image(url, filepath, placeholder_params=None):
    """尝试下载图片，失败则创建占位图"""
    try:
        print(f"正在处理: {filepath}")
        if placeholder_params:
            img = create_placeholder_image(*placeholder_params)
            img.save(filepath)
            print(f"已创建占位图: {filepath}")
        else:
            print(f"跳过下载，使用占位图: {filepath}")
    except Exception as e:
        print(f"创建占位图失败 {filepath}: {e}")
        # 创建默认占位图
        img = create_placeholder_image(800, 600, (139, 115, 85), os.path.basename(filepath))
        img.save(filepath)

# 创建images目录
os.makedirs('images', exist_ok=True)

print("开始创建景点和美食图片...")

# 定义图片参数
image_configs = [
    ('images/hero-bg.jpg', (1200, 800), (139, 115, 85), '万峰林日落美景'),
    ('images/day1.jpg', (800, 600), (100, 120, 140), '万峰林日落'),
    ('images/day2.jpg', (800, 600), (120, 140, 100), '万峰林田园'),
    ('images/day3.jpg', (800, 600), (140, 100, 120), '马岭河峡谷'),
    ('images/day4.jpg', (800, 600), (100, 140, 120), '青岩古镇'),
    ('images/day5.jpg', (800, 600), (140, 120, 100), '贵阳风光'),
    ('images/lodge1.jpg', (800, 600), (120, 100, 140), '万峰林观景民宿'),
    ('images/lodge2.jpg', (800, 600), (140, 130, 90), '贵阳舒适酒店'),
    ('images/food1.jpg', (800, 600), (150, 100, 100), '布依族特色餐'),
    ('images/food2.jpg', (800, 600), (100, 150, 100), '五色糯米饭'),
    ('images/food3.jpg', (800, 600), (100, 100, 150), '兴义鸡肉汤圆'),
    ('images/food4.jpg', (800, 600), (150, 150, 100), '贵阳酸汤鱼'),
    ('images/food5.jpg', (800, 600), (150, 100, 150), '玫瑰冰粉'),
    ('images/food6.jpg', (800, 600), (100, 150, 150), '青岩卤猪脚')
]

# 创建所有图片
for filepath, size, color, text in image_configs:
    download_or_create_image(
        None, 
        filepath, 
        (size[0], size[1], color, text)
    )

print("\n所有图片已创建完成！")
print("图片列表:")
for filepath, _, _, _ in image_configs:
    print(f"- {filepath}")

print("\n现在可以查看 images 文件夹中的图片了。")