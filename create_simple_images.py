import os
from PIL import Image, ImageDraw

def create_simple_image(width, height, bg_color, text):
    """创建简单的带文字图片"""
    # 创建图片
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 使用基本的ASCII字符绘制简单标识
    text_parts = text.split()
    base_text = text_parts[0] if text_parts else "View"
    
    # 简单绘制一些几何图形和基本文字
    # 绘制一个简单的边框
    draw.rectangle([10, 10, width-10, height-10], outline=(255,255,255), width=2)
    
    # 绘制一个简单的图案（比如代表风景的线条）
    for i in range(0, width, 20):
        draw.line([(i, height-50), (i+10, height-80), (i+20, height-50)], fill=(200,200,200), width=2)
    
    # 绘制简单的标题
    title = base_text[:10]  # 只取前10个字符避免显示问题
    draw.text((20, 20), title, fill=(255, 255, 255))
    
    return image

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
    try:
        img = create_simple_image(size[0], size[1], color, text)
        img.save(filepath)
        print(f"已创建图片: {filepath}")
    except Exception as e:
        print(f"创建图片失败 {filepath}: {e}")
        # 创建纯色图片作为备选
        fallback_img = Image.new('RGB', size, color)
        fallback_img.save(filepath)
        print(f"已创建备选图片: {filepath}")

print("\n所有图片已创建完成！")