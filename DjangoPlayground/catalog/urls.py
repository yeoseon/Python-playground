from django.urls import path
from catalog import views

# URL 패턴이 감지되었을 때 호출될 view 함수:views.index. 이 함수는 views.py 파일 안에서 index()로 이름지어져 있습니다
# <a href="{% url 'index' %}">Home</a>. 으로서 나타낼 수 있다.
# <a href="/catalog/">Home</a>), 다음과 같이 하드코딩 할 경우, url 정보가 바뀌었을 시 같이 바꿔줘야 하므로, 위의 예를 쓰는 것이 좋다.
urlpatterns = [
    path('', views.index, name='index'),
]