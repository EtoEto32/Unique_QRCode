FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#アプリのコードをコピー
COPY app/ ./app

# Streamlitアプリを実行
ENTRYPOINT ["streamlit","run"]

CMD ["main.py"]
