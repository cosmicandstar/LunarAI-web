from django.http import StreamingHttpResponse

from streaming.video import gen, VideoCamera


# Create your views here.
def index(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
