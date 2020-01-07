"""DjangoPlayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# 만일 www.xxxx.com/catalog 로 시작되는 request 가 오면 catalog/urls.py 를 참조해서 관련된 화일을 mapping 하겠다는 의미.
urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# admin url
urlpatterns += [
    # yyskr
    # dbssu0430
    path('admin/', admin.site.urls),
]

# catalog 화면
# 장고는 import 함수 django.urls.include()를 만날 때 마다 지정된 마지막 문자에서 문자열을 나누고, 나머지 부분 문자열을 추가 작업을 위해 포함된 URLconf 모듈로 보냅니다.
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

