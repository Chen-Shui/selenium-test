from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化 WebDriver（以 Chrome 為例）
driver = webdriver.Chrome()

try:

    # 1. 測試首頁載入與標題驗證
    driver.get("https://www.perfectcorp.com/zh-tw/business")
    assert "玩美移動" in driver.title
    print("✅ 首頁載入成功，標題正確。")


    # 2. 測試 AR 虛擬試妝功能頁面
    driver.get("https://www.perfectcorp.com/zh-tw/business/products/virtual-makeup")
    assert "虛擬試妝" in driver.page_source
    print("✅ AR 虛擬試妝功能頁面載入成功。")

    # 3. 測試 AI 肌膚檢測功能頁面
    driver.get("https://www.perfectcorp.com/zh-tw/business/products/ai-skin-diagnostic")
    assert "AI 肌膚檢測" in driver.page_source
    print("✅ AI 肌膚檢測功能頁面載入成功。")

    # 4. 測試首頁logo功能
    logo = driver.find_element(By.CLASS_NAME, "pf-header__logo")
    assert logo.is_displayed()
    logo.click()
    print("✅ Logo 存在且可點擊。")



finally:
    # 關閉瀏覽器
    driver.quit()
