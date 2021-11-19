import cv2
import zmq
import numpy as np
import base64


class VideoCamera(object):
    def __init__(self):
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.SUB)
        self.footage_socket.connect('tcp://localhost:5000')  # 중간 서버의 ip
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

    def __del__(self):
        self.footage_socket.close(0)
        self.context.destroy(0)

    def get_frame(self):
        frame = self.footage_socket.recv_string()
        img = base64.b64decode(frame)
        np_img = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(np_img, 1)
        return cv2.imencode('.jpg', source)[1].tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
