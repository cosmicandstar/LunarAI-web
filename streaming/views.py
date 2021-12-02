from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render
import json
import os
import re
import base64

from django.views.decorators.csrf import csrf_exempt

from streaming.apps import StreamingConfig
from streaming.video import gen, VideoCamera


# Create your views here.
def index(request):
    return render(request, 'index.html')


def video(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

@csrf_exempt
def upload(request):
    if request.META['CONTENT_TYPE'] == "application/json":
        data = json.loads(request.body)
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        file = data['img']
        encoded_photo = re.search(r'base64,(.*)', file).group(1)
        photo_bytes = base64.b64decode(encoded_photo)

        # todo unique ID 할당
        id = 1

        DIR = os.path.join(BASE_DIR, str(id))
        try:
            if not os.path.exists(DIR):
                os.makedirs(DIR)
        except Exception as e:
            pass

        with open(os.path.join(DIR, str(len(os.listdir(DIR))) + '.png'), 'wb+') as destination:
            destination.write(photo_bytes)

        return JsonResponse({ 'success': True })


def train(request):
    # todo unique ID 할당
    id = 1
    StreamingConfig.send_socket.send_string(f'fit:{id}')
    return JsonResponse({ 'success': True })