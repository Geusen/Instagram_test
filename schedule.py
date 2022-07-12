import settings
import datetime
import os
import time
from instagram_private_api import Client, ClientCompatPatch
from PIL import Image
import io
import urllib.request

#-----------------------------------------------------------------------------
# バグが発生した場合様々が情報が必要になるため、日付を取得(日本時間)
dt = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
w_list = ['月', '火', '水', '木', '金', '土', '日']
print(dt.strftime('\n[%Y年%m月%d日(' + w_list[dt.weekday()] + ') %H:%M:%S]'))
#-----------------------------------------------------------------------------
user_name = settings.ID
password = settings.PW
url = "https://user-images.githubusercontent.com/5179467/57978324-23e4b000-7a46-11e9-8b04-4d16e97a702c.jpg"
api = Client(user_name, password)


img_in = urllib.request.urlopen(url).read()
img_bin = io.BytesIO(img_in)
img = Image.open(img_bin)

api.post_photo(img_bin.getvalue(), (img.width, img.height))
