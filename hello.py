from flask import Flask
app = Flask(__name__)

@app.route('/')           #'/'는 정해준 포트값의 정의이다. ('/', methods=['GET','POST'])
def hello_world():        # app.run(port=$$,debug = true/false)
    return 'Hello World!' # 포트값 = 주소, 디버그 = 활동내역 true시 해킹 위험
# @는 '다음 행동과 연결하게 해준다.' method = login, 다음줄 check loging 정도로, 로그인했는지 검사하고 다음 으로 넘겨준다는 뜻
if __name__ == '__main__':
    app.run()
