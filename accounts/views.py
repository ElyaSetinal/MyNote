from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignupForm
# Create your views here.

def userlogin(request): # 로그인 페이지
    '''
    Django에서 기본으로 제공하는 login과 겹치므로, userlogin으로 이름 변경(22.05.11)
    '''
    # GET: 로그인 화면
    # POST 
    # 데이터 유효성 검사, django에서 지원하는 forms 사용
    # 비지니스 로직 - 폼이 맞으면, 로그인 시행
    # 응답 - 노트 메인페이지로 이동
    if request.method=='GET':
        return render(request, 'login.html', {'form':AuthenticationForm()})
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #비지니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            #응답
            return redirect('notes:main_page')
        else:
            #비지니스 로직 처리 - 로그인 실패, 로그인 화면 재 연결
            #응답 
            return render(request, 'login.html', {'form':form})

@login_required
def userlogout(request): # 로그아웃 페이지, 일정시간 후 자동으로 인덱스 페이지로 넘기기/html의 메타태그 사용
    '''
    Django에서 기본으로 제공하는 logout과 겹치므로, userlogout으로 이름 변경(22.05.11)
    '''
    # 로그아웃
    # 데이터 유효성 검사 - 로그인 상태인지 확인
    # 비지니스 로직 - 사용자 로그아웃
    # 응답 - 인덱스 페이지
    if request.user.is_authenticated:
        # 비지니스 로직 - 로그아웃 처리
        logout(request)
    #응답
    return redirect('index')

def signup_view(request):
    #GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignupForm
        context = {'form':form }
        return render(request, 'signup.html', context)

    #POST 요청시 데이터 확인 후 회원 생성
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('notes:main_page')
        else:
            #리다이렉트
            return redirect('users:signup')