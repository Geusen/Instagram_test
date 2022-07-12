import settings
import datetime
import os
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#-----------------------------------------------------------------------------
# バグが発生した場合様々が情報が必要になるため、日付を取得(日本時間)
dt = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
w_list = ['月', '火', '水', '木', '金', '土', '日']
print(dt.strftime('\n[%Y年%m月%d日(' + w_list[dt.weekday()] + ') %H:%M:%S]'))

Insta_ID = settings.ID
Insta_PASS = settings.PW
text = "test"
Insta_URL = "https://www.instagram.com/accounts/login/"
#-----------------------------------------------------------------------------
# Chromeヘッドレスモード起動
mobile_emulation = { "deviceName": "iPhone X" }
options = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation", mobile_emulation)
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(10)

driver.get(Insta_URL)

 # ログイン
driver.find_element_by_name('username').send_keys(Insta_ID)
driver.find_element_by_name('password').send_keys(Insta_PASS)
driver.find_elements_by_css_selector('.sqdOP.L3NKy.y3zKF')[1].click() # ログインボタン押す

# トップページに遷移
driver.get("https://www.instagram.com/")
driver.find_element_by_css_selector('.aOOlW.HoLwm').click() # ホーム追加キャンセル押す
post_button = driver.find_element_by_xpath('//div[@data-testid="new-post-button"]').click()

# 画像アップロード（pywinautoによるOSウィンドウ制御）
time.sleep(1)
findWindow = lambda: pywinauto.findwindows.find_windows(title=u'開く')[0]
dialog = pywinauto.timings.wait_until_passes(5, 1, findWindow)
pwa_app = pywinauto.Application()
pwa_app.connect(handle=dialog)
window = pwa_app[u'開く']
window.wait(u'ready')
edit = window.Edit4

# 画像パス入力
edit.set_focus()
image = glob.glob("white.png")
edit.set_text(image[0])

# ダイアログの「開く」ボタンをクリック
button = window[u'開く(&O):']
button.click()
time.sleep(3) # アップロード完了まで待つ
driver.find_element_by_class_name('pHnkA').click() # 画像縮小ボタン押す
time.sleep(1)
driver.find_element_by_class_name('UP43G').click() # 次へボタン押す

# 投稿する文章取得
text = inifile.get('Common','text')

# 文章入力
time.sleep(3)
driver.find_element_by_tag_name('textarea').send_keys(text.decode('utf-8'))
time.sleep(3)

# 投稿
driver.find_element_by_class_name('UP43G').click() # 投稿ボタン押す
time.sleep(5) # 投稿完了まで待つ


time.sleep(1)
driver.quit()
