import random,schedule
import io
import base64


# 実行する関数
def task():
  print("現在QRコードを表示！")
  random_number=random.randint(100000,999999) # 取り敢えず6桁の乱数を生成
  code=pyqrcode.create(str(random_number), error="L", version=3, mode="binary")
  
  # PNG形式などで一時的に画像を保存し、base64エンコードを行う例
  buffer=io.BytesIO()
  code.png(buffer,scale=5)
  img_data=buffer.getvalue()
  
  # base64エンコード
  base64_qr=base64.b64encode(img_data).decode("utf-8")
  
  # HTML imgタグ用のデータ
  img_url=f"data:image/png;base64,{base64_qr}"
  print(img_url)# 実際に埋め込む対象のもの
  output_div=docment.querySelector("#qr-code")
  output_div.innerHTML=img_url


# 6秒ごとにtaskを実行
schedule.every(0.1).minutes.do(task)

# Jobの実行監視、指定時間になったらjob関数を実行
while True:
  schedule.run_pending()
  time.sleep(1) # CPUの使用率を抑えるためにsleep関数を入れている。

