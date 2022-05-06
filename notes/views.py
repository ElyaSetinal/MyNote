from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Category, Category2, Note

""" 작성해야할 views
    인덱스, 로그인/로그아웃, 메인, 카테고리1,2차, 생성/읽기/수정/삭제(CRUD) 페이지
    탬플릿 필요 : 인덱스, 로그인/로그아웃, 메인, 카테고리, CRUD 
    # path('main/', main_page, name='main_page'),
    # path('category/', Pcategory_page, name='Pcategory_page'),
    # path('category/category2/', Scategory_page, name='Scategory_page'),
    # path('new/', create_page, name='create_page'),
    # path('<int:id>/', detail_page, name='detail_page'),
    # path('<int:id>/edit/', edit_page, name='edit_page'),
    # path('<int:id>/delete/', delete_page, name='delete_page'),
    # path('', index, name='index'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
"""

def index(request): # 뭐하는 페이지인지 간단한 설명, 로그인으로 넘어갈 수 있는 구조
    if request.method=='GET':
        pass
    else:
        pass

def login(request): # 로그인 페이지
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def logout(request): # 로그아웃 페이지, 일정시간 후 자동으로 인덱스 페이지로 넘기기/html의 메타태그 사용
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def main_page(request): # 로그인 후 보여줄 메인페이지 : 작성된 전체글, 부모 카테고리 지정 링크
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def Pcategory_page(request): # 부모 카테고리 : 부모 카테고리에 포함된 모든 글 및 자식 카테고리 지정 링크
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def Scategory_page(request): # 자식 카테고리 : 자식 카테고리에 포함된 모든 글 링크
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def create_page(request): # 글 쓰기 : 새로운 글 쓰기
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def detail_page(request, id): # 개별글 보기 : 작성된 글 상세보기 링크
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def edit_page(request, id): # 개별글 수정 : 작성된 글 수정 링크
    if request.method=='GET':
        pass
    else:
        pass

@login_required
def delete_page(request, id): # 개별글 삭제 : 작성된 글 삭제 페이지, Hard-Delete
    if request.method=='GET':
        pass
    else:
        pass
