from django.http import StreamingHttpResponse
from django.shortcuts import render

from streaming.video import gen, VideoCamera


# Create your views here.
def index(request):
    return render(request, 'index.html')


def video(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
