# ✅ 1. 웹 환경 테스트 (app.py)
# Flask를 사용하여 간단한 메시지를 출력하는 웹 애플리케이션을 구현하고, VS Code 환경에서 실행한다.

# Python 파일명: app.py
# 구현 요구사항:
    # 1. Flask 웹 프레임워크 사용
    # 2. @app.route("/") 데코레이터 사용
    # 3. 함수 이름: hello_world
    # 4. 반환 문자열: "Hello, DevOps!"
    # 5. 서버 실행 시 호스트: 0.0.0.0, 포트: 8080

# Flask는 파이썬에서 가장 많이 쓰이는 웹 프레임워크 중 하나이다.
# 여기서 Flask는 클래스이며, 이를 통해 웹 서버 애플리케이션을 만든다.
from flask import Flask

# Flask 클래스의 객체 app을 생성한다. __name__은 현재 파일의 이름이 들어간다.
app = Flask(__name__)

# @app.route("/") = Flask에서 라우팅(Route)을 정의하는 부분으로, 웹사이트에서 / 경로(즉, 홈페이지)를 방문했을 때 어떤 함수를 실행할지 지정하는 것이다.
# 실행할 함수는 아래에 작성하면 된다.
@app.route("/") # 요구사항 2
def hello_world(): # 요구사항 3
    message = "Hello, DevOps"
    return message # 요구사항 4

if __name__ == "__main__": # 이 코드는 이 파일이 직접 실행될 때만 아래 코드를 실행하겠다는 의미이다.
    # app.run(host="0.0.0.0", port=8080)
    app.run(host="0.0.0.0", port=8080, debug = True) # 요구사항 5

# Visual Studio Code의 Run 메뉴에서 Run Without Debugging를 선택해서 해당 파일을 실행한다.
# 웹브라우저로 접속하여 Hello, DevOps! 출력을 확인한다.
# Visual Studio Code의 Run 메뉴에서 Stop Debugging를 선택해서 실행을 종료한다.

# Visual Studio Code의 Run 메뉴에서 Start Debugging과 Run Without Debugging을 각각 실행해보고 차이점을 확인한다.
# Run Without Debugging : 단순히 실행을 한다. 중단 없이 동작을 확인하는 것이다.
# Start Debugging       : 중단점 설정이 가능하다. 코드가 실행되다가 중단점에서 멈춘다. 중단점 설정을 통해서 변수 값을 확인하고 코드 흐름을 분석할 수 있다.