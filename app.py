from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app = Flask(__name__)


@app.route('/')
def index():
    return "Default Message"


def gen(video1):
    while True:
        success, image = video1.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    video = cv2.VideoCapture(0)
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True, debug=True)
