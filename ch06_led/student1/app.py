from flask import Flask, render_template
import config
import RPi.GPIO as GPIO  # GPIO 라이브러리 임포트 필요
from model.led_db import LedDB 

app = Flask(__name__)
LED = config.LED_PIN                        # 추가
led_db = LedDB()                            # 2. app 만든 줄 아래에 추가

# LED 핀 준비 (test_led.py 와 같음)         # 추가
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def home():
    return render_template('index.html')

# ───── 아래 두 라우트 추가 ─────
@app.route('/on', methods=['POST'])
def led_on():
    # LED를 켜고 ok 를 돌려줌. 실패하면 fail
    try:
        GPIO.output(LED, GPIO.HIGH)
        led_db.add(LED, 1)
        return 'ok'
    except Exception as e:
        print(e)
        return 'fail'

@app.route('/off', methods=['POST'])
def led_off():
    # LED를 끄고 ok 를 돌려줌. 실패하면 fail
    try:
        GPIO.output(LED, GPIO.LOW)
        led_db.add(LED, 0)
        return 'ok'
    except Exception as e:
        print(e)
        return 'fail'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)

