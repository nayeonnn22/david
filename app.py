from flask import Flask, render_template
import socket # 1. app.py에 socket 모듈을 import 한다.

app = Flask(__name__)

@app.route('/')
def home():
    # 2. render_template 호출 이전에 코드를 추가
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    # 3. render_template 호출 시 computername=hostname 인자를 추가
    return render_template('menu.html', computername=hostname)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True) # 5. app.run() 실행 시 debug=True 옵션을 설정