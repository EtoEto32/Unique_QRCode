# pythonのhttpサーバーって結局何者？

## 全体の構造の概要

- http.serverモジュールは、シンプルで手軽にHTTPサーバーを立ち上げるためのモジュール（？）らしい。特に開発やテスト、学習目的で使われる。

→じゃあhttp.serverというモジュールは、アプリケーション層で動くサーバーサイドのモジュールと捉える事が出来る。（フレームワークの範疇にはいかないけど、サーバーサイドの簡易的な操作なら出来るよねという話。）

- OSI参照モデルでいうところの**アプリケーション層**である。

### 主な用途

- 開発環境でのテスト：ブラウザ側の開発をする際に、ローカルでウェブサイトを表示して動作確認を行う。
- ファイル共有：ネットワークないで簡単にファイルを共有する。
- 学習目的：WebサーバーやHTTPプロトコルの基本を学ぶための教材として利用。

### 簡単な動作

```
+------------------+          HTTP リクエスト          +------------------+
|     クライアント    |  <------------------------------> |   http.server    |
| (ブラウザやHTTPクライアント) |                                    | (PythonのHTTPサーバー) |
+------------------+                                       +------------------+

```

## 役立ちそうな情報

https://blog.serverworks.co.jp/tech/2020/02/11/python-http-server/

https://docs.python.org/ja/3/library/http.server.html