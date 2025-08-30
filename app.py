# 반달곰 커피 IT 혁신팀 프로젝트
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>반달곰 커피에 오신 것을 환영합니다!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
