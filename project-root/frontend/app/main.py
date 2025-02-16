import streamlit as st
import random
import pyqrcode
import io
import base64
import requests
import os
from datetime import datetime,timedelta

# バックエンドの API URL（Render 用）
API_URL = os.getenv("API_URL", "http://localhost:8000")  # ローカル開発時のデフォルト

# QRコード生成関数
def generate_qr_code():
    random_number = random.randint(100000, 999999)
    code = pyqrcode.create(str(random_number), error='L', version=3, mode='binary')

    buffer = io.BytesIO()
    code.png(buffer, scale=5)
    img_data = buffer.getvalue()

    base64_qr = base64.b64encode(img_data).decode('utf-8')
    img_html = f'<img src="data:image/png;base64,{base64_qr}" alt="QRコード" width="150">'
    return random_number

st.title("QRコード生成デバイス")

# セッション変数をセットする
if "qr_number" not in st.session_state:
  st.session_state.qr_number=generate_qr_code()
  st.session_state.read_time=datetime.now()
  
  
# placeholderの追加
qr_placeholder=st.empty()
timer_placeholder=st.empty()

qr_placeholder.markdown(st.session_state.qr_code_html, unsafe_allow_html=True)

#更新までの時間、取り敢えず便宜上5秒でやる。
reflash_time=timedelta(seconds=5)
time_to_update=st.session_state.read_time+reflash_time
while True:
  for i in range(int(reflash_time)):
    
  time_to_update-=(-1)
  
  timer_placeholder.write(f"QRコード更新まであと {int(reflash_time)} 秒")
  time.sleep(1)  # 1秒待機