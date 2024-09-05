# Dockerコンテナ起動
`docker-compose build`
`docker-compose up`

`docker-compose up -d`
でも可
buildなしでcompose upだけでも多分動く

mysqlが動くまでflaskに接続できない仕様にしてあるため、起動に少し時間がかかる(多分1分弱くらい)

# flask操作
`docker exec -it frask_dockerimage-app-1 /bin/bash`
<!-- bashに入る -->

`flask run`
<!-- flask起動 -->

http://localhost:8000/
<!-- ここにアクセスすると表示される -->
