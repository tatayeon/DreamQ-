import cv2
import torch
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render


class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # 기본 카메라를 사용
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def __del__(self):
        self.video.release()

    def load_model(self):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def get_frame(self):
        success, image = self.video.read()
        if success:
            results = self.model(image)  # YOLOv5로 객체 감지 수행
            image = results.render()[0]  # 감지된 객체를 이미지에 렌더링
            
            # 사람 객체만 카운트
            people_count = 0
            for result in results.xyxy[0]:
                class_id = int(result[-1])
                class_name = self.classes[class_id]
                if class_name == 'person':
                    people_count += 1

            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes(), people_count
        else:
            return None, 0

def gen():
    camera = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다.
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                content_type='multipart/x-mixed-replace; boundary=frame')

def home(request):
    return render(request, "home.html")

def get_people_count(request):
    camera = VideoCamera()
    _, people_count = camera.get_frame()
    return JsonResponse({'people_count': people_count})
