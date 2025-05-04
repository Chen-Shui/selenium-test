from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_apple_mac_section():
    # 設定 chromedriver 路徑
    service = Service('./chromedriver')  # Windows 改成 './chromedriver.exe'

    # 啟動 Chrome
    driver = webdriver.Chrome(service=service)

    try:
        # 打開 apple.com
        driver.get('https://www.apple.com')

        # 檢查標題是否有 Apple
        assert 'Apple' in driver.title
        print('✅ 進入 Apple 首頁成功')

        # 點擊 Mac 連結
        mac_link = driver.find_element(By.LINK_TEXT, 'Mac')
        mac_link.click()
        time.sleep(3)  # 等待 Mac 頁面載入

        # 檢查 URL 是否包含 /mac
        assert '/mac' in driver.current_url
        print('✅ 成功進入 Mac 頁面')

        # 檢查 Mac 頁面有 MacBook Air
        body_text = driver.find_element(By.TAG_NAME, 'body').text
        assert 'MacBook Air' in body_text
        print('✅ MacBook Air 出現在頁面中')

    finally:
        # 關閉瀏覽器
        driver.quit()
        print('✅ 測試完成，關閉瀏覽器')

if __name__ == "__main__":
    test_apple_mac_section()
