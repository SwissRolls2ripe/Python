# 计算扇形面积
def calculate_sector_area(centerangle, radius):
    sector_area = centerangle / 360 * 3.14 * radius ** 2
    return sector_area

area = calculate_sector_area(160, 30)
print(f"扇形面积为：{area}")