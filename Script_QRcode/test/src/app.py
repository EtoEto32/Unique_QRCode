import streamlit as st
import random
import pyqrcode
import io
import base64
import time

def generate_qr_code():
    random_number = random.randint(100000, 999999)  # 6桁の乱数を生成
    code = pyqrcode.create(str(random_number), error='L', version=3, mode='binary')
    
    # QRコードをバッファにPNG形式で保存
    buffer = io.BytesIO()
    code.png(buffer, scale=5)
    img_data = buffer.getvalue()
    
    # Base64エンコード
    base64_qr = base64.b64encode(img_data).decode('utf-8')
    # HTMLのimgタグを作成
    img_html = f'<img src="data:image/png;base64,{base64_qr}" alt="QRコード" width="150">'
    return img_html

st.title("QRコード生成技術検証")

# プレースホルダーを用意
qr_placeholder = st.empty()
timer_placeholder = st.empty()

# ページが読み込まれるたびに新しいQRコードを生成
qr_code_html = generate_qr_code()
qr_placeholder.markdown(qr_code_html, unsafe_allow_html=True)


remit = 5
for seconds in range(remit, 0, -1):
    # 毎回同じプレースホルダー（timer_placeholder）に上書きする
    timer_placeholder.write(f"QRコード更新まであと {seconds} 秒")
    time.sleep(1)


# 0秒になったらページを再実行して、新しいQRコードを生成(セッションステートに保持している変数リセット)
st.rerun()
# ボタンを押して強制的に再読み込み（リロール）したい場合
if st.button("再読み込み"):
    st.rerun()
