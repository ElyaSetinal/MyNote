"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from notes.views import index
"""
통합페이지 구성
1. 인덱스 페이지 : 뭐하는 페이지인지 간단한 설명, 로그인으로 넘어갈 수 있는 구조
2. 로그인 페이지
3. 로그아웃 페이지, 일정시간 후 자동으로 인덱스 페이지로 넘기기/html의 메타태그 사용
4. 노트 앱으로 접속
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('notes/', include('notes.urls', namespace = 'notes')),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path("__reload__/", include("django_browser_reload.urls")),
]
