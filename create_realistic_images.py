import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_scenic_image(filepath, width, height, scene_type):
    """创建模拟风景图片"""
    # 创建基础图像
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    if scene_type == "sunset":
        # 万峰林日落场景
        # 渐变天空
        for y in range(height):
            r = int(255 - y * 0.05)
            g = int(180 - y * 0.1)
            b = int(50 - y * 0.05)
            color = (min(255, r), min(255, g), min(255, b))
            draw.line([(0, y), (width, y)], fill=color)
        
        # 添加山峰
        peak_heights = []
        for i in range(20):
            x = i * width // 20
            height_var = random.randint(30, 100)
            peak_heights.append(height - 150 - height_var)
            draw.polygon([(x-20, height), (x, peak_heights[-1]), (x+20, height)], 
                        fill=(100, 80, 60))
        
        # 添加太阳
        draw.ellipse([(width-100, 50), (width-50, 100)], fill=(255, 200, 50))
        
        # 添加田园效果
        for y in range(int(height*0.7), height, 5):
            for x in range(0, width, 10):
                if random.random() > 0.7:
                    draw.rectangle([(x, y), (x+5, y+3)], fill=(50, 120, 50))
    
    elif scene_type == "field":
        # 万峰林田园场景
        # 蓝天
        for y in range(int(height*0.4)):
            draw.line([(0, y), (width, y)], fill=(135, 206, 235))
        
        # 白云
        for i in range(3):
            cloud_x = random.randint(50, width-100)
            cloud_y = random.randint(20, int(height*0.3))
            draw.ellipse([(cloud_x, cloud_y), (cloud_x+60, cloud_y+30)], fill=(255, 255, 255))
            draw.ellipse([(cloud_x+20, cloud_y-10), (cloud_x+80, cloud_y+20)], fill=(255, 255, 255))
        
        # 山峰
        for i in range(15):
            x = i * width // 15
            peak_y = int(height*0.6) - random.randint(50, 120)
            draw.polygon([(x-25, height*0.6), (x, peak_y), (x+25, height*0.6)], 
                        fill=(120, 100, 80))
        
        # 田野
        for y in range(int(height*0.6), height):
            for x in range(0, width, 3):
                if random.random() > 0.3:
                    draw.point((x, y), fill=(50, 150, 50))
                else:
                    draw.point((x, y), fill=(60, 160, 60))
    
    elif scene_type == "canyon":
        # 马岭河峡谷场景
        # 深色峡谷壁
        for y in range(height):
            gray_val = 50 + int(y * 0.3)
            draw.line([(0, y), (width, y)], fill=(gray_val, gray_val, gray_val))
        
        # 峡谷形状
        for y in range(height):
            mid_x = width // 2
            width_at_y = max(20, 100 - abs(y - height//2) * 0.1)
            left_bound = max(0, int(mid_x - width_at_y))
            right_bound = min(width, int(mid_x + width_at_y))
            
            for x in range(left_bound, right_bound):
                # 峡谷壁颜色变化
                if x < mid_x - 10 or x > mid_x + 10:
                    color_factor = random.uniform(0.7, 1.0)
                    draw.point((x, y), fill=(
                        int(80 * color_factor), 
                        int(70 * color_factor), 
                        int(60 * color_factor)
                    ))
                else:
                    # 峡谷中央（河流）
                    color_factor = random.uniform(0.3, 0.7)
                    draw.point((x, y), fill=(
                        int(50 * color_factor), 
                        int(100 * color_factor), 
                        int(150 * color_factor)
                    ))
        
        # 添加瀑布效果
        for i in range(5):
            water_x = random.randint(50, width-50)
            for y in range(20, height-20, 3):
                if random.random() > 0.7:
                    draw.point((water_x, y), fill=(100, 180, 255))
    
    elif scene_type == "ancient_town":
        # 青岩古镇场景
        # 蓝天
        for y in range(int(height*0.5)):
            draw.line([(0, y), (width, y)], fill=(135, 206, 235))
        
        # 白云
        for i in range(2):
            cloud_x = random.randint(50, width-100)
            cloud_y = random.randint(20, int(height*0.3))
            draw.ellipse([(cloud_x, cloud_y), (cloud_x+80, cloud_y+30)], fill=(255, 255, 255))
        
        # 古镇建筑
        building_heights = []
        for i in range(8):
            x = i * width // 8
            b_height = int(height*0.5) - random.randint(80, 150)
            building_heights.append(b_height)
            
            # 建筑主体
            draw.rectangle([(x-30, b_height), (x+30, int(height*0.5))], fill=(180, 160, 140))
            
            # 屋顶
            roof_points = [(x-35, b_height), (x, b_height-20), (x+35, b_height)]
            draw.polygon(roof_points, fill=(150, 80, 60))
            
            # 门窗
            if random.random() > 0.3:
                door_y = int(height*0.5) - 30
                draw.rectangle([(x-10, door_y), (x+10, int(height*0.5)-5)], fill=(100, 80, 60))
        
        # 石板路
        for y in range(int(height*0.5), height):
            for x in range(0, width, 5):
                stone_color = (random.randint(150, 180), random.randint(150, 180), random.randint(150, 180))
                draw.rectangle([(x, y), (x+4, y+4)], fill=stone_color)
    
    elif scene_type == "city":
        # 贵阳城市风光
        # 天空渐变
        for y in range(int(height*0.4)):
            blue_val = 200 + int(y * 0.6)
            draw.line([(0, y), (width, y)], fill=(135, 200, blue_val))
        
        # 白云
        for i in range(3):
            cloud_x = random.randint(30, width-80)
            cloud_y = random.randint(10, int(height*0.3))
            draw.ellipse([(cloud_x, cloud_y), (cloud_x+70, cloud_y+25)], fill=(250, 250, 250))
        
        # 建筑群
        for i in range(12):
            x = i * width // 12
            b_height = int(height*0.4) + random.randint(50, int(height*0.5))
            
            # 建筑
            building_width = width // 15
            draw.rectangle([(x-building_width//2, b_height), (x+building_width//2, int(height*0.4))], 
                          fill=(random.randint(180, 220), random.randint(180, 220), random.randint(180, 220)))
            
            # 窗户
            for win_y in range(int(b_height)+10, int(height*0.4), 15):
                for win_x in range(x-building_width//2+5, x+building_width//2-5, 8):
                    if random.random() > 0.3:  # 随机点亮窗户
                        draw.rectangle([(win_x, win_y), (win_x+5, win_y+10)], fill=(255, 255, 200))
                    else:
                        draw.rectangle([(win_x, win_y), (win_x+5, win_y+10)], fill=(50, 50, 100))
    
    elif scene_type == "lake_castle":
        # 万峰湖吉隆堡场景
        # 天空
        for y in range(int(height*0.4)):
            draw.line([(0, y), (width, y)], fill=(135, 206, 235))
        
        # 白云
        for i in range(3):
            cloud_x = random.randint(50, width-100)
            cloud_y = random.randint(20, int(height*0.3))
            draw.ellipse([(cloud_x, cloud_y), (cloud_x+60, cloud_y+25)], fill=(255, 255, 255))
        
        # 湖泊
        for y in range(int(height*0.4), height):
            blue_var = random.randint(80, 120)
            draw.line([(0, y), (width, y)], fill=(0, blue_var, blue_var+50))
        
        # 吉隆堡
        castle_x = width // 2
        castle_base_y = int(height*0.5)
        
        # 主体建筑
        draw.rectangle([(castle_x-80, castle_base_y-80), (castle_x+80, castle_base_y)], fill=(200, 180, 160))
        
        # 城堡塔楼
        tower_width = 25
        for i in [-1, 1]:
            # 两侧塔楼
            draw.rectangle([(castle_x+i*60, castle_base_y-120), (castle_x+i*60+tower_width, castle_base_y)], 
                          fill=(180, 160, 140))
            # 塔顶尖顶
            draw.polygon([(castle_x+i*60-5, castle_base_y-120), 
                         (castle_x+i*60+tower_width//2, castle_base_y-140), 
                         (castle_x+i*60+tower_width+5, castle_base_y-120)], 
                        fill=(150, 80, 60))
        
        # 中央高塔
        draw.rectangle([(castle_x-15, castle_base_y-140), (castle_x+15, castle_base_y-80)], 
                      fill=(190, 170, 150))
        draw.polygon([(castle_x-20, castle_base_y-140), 
                     (castle_x, castle_base_y-160), 
                     (castle_x+20, castle_base_y-140)], 
                    fill=(150, 80, 60))
        
        # 城堡旗帜
        draw.line([(castle_x, castle_base_y-160), (castle_x, castle_base_y-180)], fill=(100, 100, 100), width=2)
        draw.polygon([(castle_x, castle_base_y-180), 
                     (castle_x+30, castle_base_y-175), 
                     (castle_x, castle_base_y-170)], 
                    fill=(255, 100, 100))
    
    elif scene_type == "lodging":
        # 民宿/酒店外观
        # 蓝天
        for y in range(int(height*0.4)):
            draw.line([(0, y), (width, y)], fill=(135, 206, 235))
        
        # 远山
        for i in range(5):
            x = i * width // 5
            peak_y = int(height*0.4) - random.randint(30, 70)
            draw.polygon([(x-40, int(height*0.4)), (x, peak_y), (x+40, int(height*0.4))], 
                        fill=(150, 130, 110))
        
        # 民宿建筑
        house_x = width // 2
        house_y = int(height*0.5)
        
        # 房屋主体
        draw.rectangle([(house_x-100, house_y-60), (house_x+100, house_y)], fill=(220, 200, 180))
        
        # 屋顶
        draw.polygon([(house_x-105, house_y-60), (house_x, house_y-80), (house_x+105, house_y-60)], 
                    fill=(180, 100, 80))
        
        # 门窗
        draw.rectangle([(house_x-20, house_y-20), (house_x+20, house_y)], fill=(100, 80, 60))  # 门
        
        for i in range(-2, 3):
            if i != 0:
                draw.rectangle([(house_x+i*30-10, house_y-50), (house_x+i*30+10, house_y-30)], 
                              fill=(180, 200, 220))  # 窗户
        
        # 花园
        for i in range(15):
            flower_x = random.randint(20, width-20)
            flower_y = house_y + random.randint(10, 50)
            petal_colors = [(255, 100, 100), (255, 200, 100), (200, 255, 100), (100, 200, 255)]
            color = random.choice(petal_colors)
            
            # 简单花朵
            draw.ellipse([(flower_x-5, flower_y-5), (flower_x+5, flower_y+5)], fill=color)
            draw.ellipse([(flower_x-8, flower_y), (flower_x+8, flower_y+2)], fill=(0, 100, 0))
    
    elif scene_type == "food":
        # 美食图片 - 根据不同类型创建不同的食物
        draw.rectangle([(0, 0), (width, height)], fill=(245, 240, 230))  # 浅色背景
        
        # 盘子
        plate_x, plate_y = width // 2, height // 2
        plate_radius = min(width, height) // 3
        draw.ellipse([(plate_x-plate_radius, plate_y-plate_radius), 
                     (plate_x+plate_radius, plate_y+plate_radius)], 
                    outline=(200, 200, 200), fill=(250, 250, 250), width=5)
        
        # 食物
        food_types = ["rice", "soup", "fish", "dessert", "meat"]
        food_type = random.choice(food_types)
        
        if food_type == "rice":  # 五色糯米饭
            colors = [(255, 100, 100), (100, 255, 100), (255, 255, 100), (100, 100, 255), (255, 100, 255)]
            for i, color in enumerate(colors):
                start_angle = i * 72 - 90
                end_angle = (i + 1) * 72 - 90
                draw.pieslice([(plate_x-plate_radius*0.8, plate_y-plate_radius*0.8), 
                              (plate_x+plate_radius*0.8, plate_y+plate_radius*0.8)], 
                             start_angle, end_angle, fill=color)
        elif food_type == "soup":  # 汤圆
            for i in range(6):
                row = i // 3
                col = i % 3
                ball_x = plate_x - 40 + col * 30
                ball_y = plate_y - 20 + row * 30
                draw.ellipse([(ball_x-12, ball_y-12), (ball_x+12, ball_y+12)], fill=(250, 230, 200))
                draw.ellipse([(ball_x-8, ball_y-8), (ball_x+8, ball_y+8)], fill=(200, 150, 100))
        elif food_type == "fish":  # 酸汤鱼
            fish_x, fish_y = plate_x, plate_y - 10
            draw.ellipse([(fish_x-40, fish_y-20), (fish_x+40, fish_y+20)], fill=(255, 200, 100))  # 鱼身
            draw.polygon([(fish_x+40, fish_y), (fish_x+60, fish_y-15), (fish_x+60, fish_y+15)], fill=(255, 180, 80))  # 鱼尾
            # 汤汁
            soup_color = (200, 150, 100)
            for y in range(plate_y, plate_y+plate_radius//2):
                for x in range(plate_x-plate_radius//2, plate_x+plate_radius//2):
                    if (x-plate_x)**2 + (y-plate_y)**2 <= (plate_radius//2)**2:
                        draw.point((x, y), fill=soup_color)
        elif food_type == "dessert":  # 冰粉
            bowl_x, bowl_y = plate_x, plate_y
            # 碗
            draw.ellipse([(bowl_x-30, bowl_y-15), (bowl_x+30, bowl_y+20)], fill=(240, 240, 240))
            # 冰粉
            for i in range(20):
                px = bowl_x - 25 + random.randint(0, 50)
                py = bowl_y - 10 + random.randint(0, 25)
                draw.ellipse([(px-3, py-3), (px+3, py+3)], fill=(200, 200, 220))
            # 玫瑰糖
            draw.ellipse([(bowl_x-20, bowl_y+5), (bowl_x-10, bowl_y+15)], fill=(255, 150, 150))
        else:  # 其他肉类
            meat_x, meat_y = plate_x, plate_y
            draw.ellipse([(meat_x-35, meat_y-20), (meat_x+35, meat_y+15)], fill=(180, 120, 100))
            # 添加纹理
            for i in range(10):
                x_start = meat_x - 30 + random.randint(0, 60)
                y_start = meat_y - 15 + random.randint(0, 25)
                x_end = x_start + random.randint(5, 15)
                y_end = y_start + random.randint(-5, 5)
                draw.line([(x_start, y_start), (x_end, y_end)], fill=(150, 80, 60), width=2)
    
    # 添加轻微噪点增加真实感
    for _ in range(500):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        r_offset = random.randint(-5, 5)
        g_offset = random.randint(-5, 5)
        b_offset = random.randint(-5, 5)
        
        current_pixel = img.getpixel((x, y))
        new_r = max(0, min(255, current_pixel[0] + r_offset))
        new_g = max(0, min(255, current_pixel[1] + g_offset))
        new_b = max(0, min(255, current_pixel[2] + b_offset))
        
        draw.point((x, y), fill=(new_r, new_g, new_b))
    
    img.save(filepath)
    print(f"已创建图片: {filepath}")


# 创建images目录
os.makedirs('images', exist_ok=True)

print("开始创建景点和美食图片...")

# 定义图片配置
image_configs = [
    ('images/hero-bg.jpg', 1200, 800, 'sunset'),       # 万峰林日落
    ('images/day1.jpg', 800, 600, 'sunset'),           # 万峰林日落
    ('images/day2.jpg', 800, 600, 'field'),            # 万峰林田园
    ('images/day3.jpg', 800, 600, 'canyon'),           # 马岭河峡谷
    ('images/day4.jpg', 800, 600, 'ancient_town'),     # 青岩古镇
    ('images/day5.jpg', 800, 600, 'city'),             # 贵阳风光
    ('images/lodge1.jpg', 800, 600, 'lodging'),        # 万峰林观景民宿
    ('images/lodge2.jpg', 800, 600, 'lodging'),        # 贵阳舒适酒店
    ('images/food1.jpg', 800, 600, 'food'),            # 布依族特色餐
    ('images/food2.jpg', 800, 600, 'food'),            # 五色糯米饭
    ('images/food3.jpg', 800, 600, 'food'),            # 兴义鸡肉汤圆
    ('images/food4.jpg', 800, 600, 'food'),            # 贵阳酸汤鱼
    ('images/food5.jpg', 800, 600, 'food'),            # 玫瑰冰粉
    ('images/food6.jpg', 800, 600, 'food')             # 青岩卤猪脚
]

# 创建所有图片
for filepath, width, height, scene_type in image_configs:
    create_scenic_image(filepath, width, height, scene_type)

print("\n所有图片已创建完成！")
print("图片列表:")
for filepath, _, _, _ in image_configs:
    print(f"- {filepath}")

print("\n现在可以查看 images 文件夹中的风景图片了。")