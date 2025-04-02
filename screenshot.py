from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def take_screenshot(url, save_path="screenshots"):
    """自动截取网页截图并保存"""
    # 创建保存目录
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 设置无头浏览器
    options = Options()
    options.add_argument("--headless")  # 无界面模式
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # 用 Chrome 驱动（GitHub 会自动安装）
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # 等待页面加载
    time.sleep(3)
    
    # 截图并保存
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{save_path}/{timestamp}-screenshot.png"
    driver.save_screenshot(filename)
    print(f"截图已保存到: {filename}")
    
    driver.quit()

if __name__ == "__main__":
    # 示例：截取 GitHub 首页
    take_screenshot("https://github.com")
