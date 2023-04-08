from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
 #この上2行は、決り文句でして、はじめにfastapiからFastAPIを読み込み、
 #クラスをインスタンス化してappという変数に代入します。あまり深く考えずに、覚えていいと思います。

origins = [
    "http://localhost:3005",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#このコードは、主にセキュリティ面のコードです。Reactのアプリケーションと通信する際には、必要になります。
#最初にfastapiからCORSMiddlewareを読み込んだあとに、URL別にアクセスできる権限を付与しています。
#origins = []の[]の中に、通信するreactなどのアプリのURLを記載しましょう。最初はlocalとの通信をしたいので
# 、http://localhost:3000しか登録していませんが、後ほどフロントエンドのアプリをサーバーにデプロイした際には、URLを増やすことになると思います。



@app.get("/")
#このコードは、/というURLにGetリクエスト来たら、という意味です。/はデフォルトのURLです。
#Getリクエストは、webのリクエストの一つで、主にデータを取得したいときにクライアントから送られます。
# この場合のクライアントは、フロントエンドのアプリです。
def Hello():
    return {"Hello":"Wooorld!"}
