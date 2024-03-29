from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView

from .models import Category, Category2, Note
from .forms import NoteCreateForm, NoteEditForm, Ctgr1CreateForm, Ctgr1EditForm, Ctgr2CreateForm, Ctgr2EditForm

""" 작성해야할 views
    인덱스, 로그인/로그아웃, 메인, 카테고리1,2차, 생성/읽기/수정/삭제(CRUD) 페이지
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
    # path('tagsearch/',Tsearch_page, name='Tsearch_page')
"""

def index(request): # 뭐하는 페이지인지 간단한 설명, 로그인으로 넘어갈 수 있는 구조
    # 로그인 유도 기본 화면 출력
    # 데이터 유효성 검사 - 로그인 상태인지 확인
    # 비지니스 로직 - 비 로그인 상태/ 로그인 상태 구분
    # 응답 - 비로그인: 인덱스 페이지 / 로그인: 노트 메인페이지
    if not request.session.session_key:
        #print('로그인이 되어 있지 않습니다.')
        return render(request, 'index.html',{'form':AuthenticationForm(),})
    else:
        #print(f'{request.user.username}님이 로그인 되어 있습니다.')
        return redirect('notes:main_page')

@login_required
def main_page(request): # 로그인 후 보여줄 메인페이지 : 작성된 전체글, 부모 카테고리 지정 링크
    # 전체글 게시할 메인 페이지
    # 데이터 유효성 검사 - 로그인 된 유저 데이터 확인
    # 비지니스 로직 - 로그인 된 유저가 작성한 게시글 불러오기 및 카테고리 불러오기
    # 응답 - 작성한 게시글 및 상위 카테고리 표시, 최신글 순서
    current_user = request.user

    note_list = Note.objects.filter(created_by = current_user).order_by('-created_at')
    ctgy_list = Category.objects.filter(created_by = current_user).order_by('id')

    paging = Paginator(note_list, 20) # 페이지 나누기 추가, (object_list, per_page)
    page_num = request.GET.get('page') # 페이지 번호 가져오기
    note_list_index = paging.get_page(page_num) # 페이지 인덱싱
    context = {
        'list_view_page':'On',
        'note_page_list':note_list_index,
        'ctgy_list':ctgy_list,
        }
    return render(request, 'notes/main.html', context)

@login_required
def Pcategory_page(request, cate_name): # 상위 카테고리 : 상위 카테고리에 포함된 모든 글 및 자식 카테고리 지정 링크
    # 상위 카테고리 표시 페이지
    # 데이터 유효성 검사 - 로그인 유저 데이터 + 선택한 상위 카테고리 명 확인
    # 비지니스 로직 - 해당 카테고리의 로그인 유저 작성글 불러오기
    # 응답 - 작성한 게시글 및 하위 카테고리 표시
    current_user = request.user
    current_category = Category.objects.get(cate_name = cate_name)

    note_list = Note.objects.filter(created_by = current_user).filter(categories__P_cate_name = current_category).order_by('-created_at')
    ctgy2_list = Category2.objects.filter(created_by = current_user).filter(P_cate_name = current_category).order_by('id')

    paging = Paginator(note_list, 20) # 페이지 나누기 추가, (object_list, per_page)
    page_num = request.GET.get('page') # 페이지 번호 가져오기
    note_list_index = paging.get_page(page_num) # 페이지 인덱싱

    context = {
        'list_view_page':'On',
        'ctgy_now':current_category,
        'note_page_list':note_list_index,
        'ctgy_list':ctgy2_list,
    }

    return render(request, 'notes/category.html', context)

@login_required
def Scategory_page(request, cate2_name): # 하위 카테고리 : 하위 카테고리에 포함된 모든 글 링크
    # 하위 카테고리 표시 페이지
    # 데이터 유효성 검사 - 로그인 유저 데이터 + 선택한 하위 카테고리 명 확인
    # 비지니스 로직 - 해당 카테고리의 로그인 유저 작성글 불러오기
    # 응답 - 작성한 게시글 표시
    current_user = request.user
    current_category = Category2.objects.get(cate2_name = cate2_name)

    note_list = Note.objects.filter(created_by = current_user).filter(categories = current_category).order_by('-created_at')

    paging = Paginator(note_list, 20) # 페이지 나누기 추가, (object_list, per_page)
    page_num = request.GET.get('page') # 페이지 번호 가져오기
    note_list_index = paging.get_page(page_num) # 페이지 인덱싱

    context = {
        'list_view_page':'On',
        'ctgy_now':current_category,
        'note_page_list':note_list_index,
    }

    return render(request, 'notes/category.html', context)

@login_required
def create_page(request): # 글 쓰기 : 새로운 글 쓰기
    # GET: 글 작성 페이지 render
    # POST 
    # 데이터 유효성 검사  
    #  반드시 들어가야할 몇가지 항목이 작성되어 있는가, is_valid를 사용 // 카테고리, 제목, 본문, 참조링크, 태그 읽어오기. cleaned_data
    #  태그 작성시 ,(콤마)로 구분짓고, 개별 단위로 생성(split)
    # 비지니스 로직 - 읽어온 항목들을 DB에 생성하기
    # 응답 - main-page로 redirect
    if request.method=='GET':
        form = NoteCreateForm()
        context = {
            'forms':form,
            'notepage':'notes'
        }
        return render(request, 'notes/create.html', context)
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            new_note = Note.objects.create(
                categories = form.cleaned_data['categories'],
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                ref_link = form.cleaned_data['ref_link'],
                created_by = request.user,
            )
            f_tags = form.cleaned_data['tags']
            for f_tag in f_tags:
                new_note.tags.add(f_tag)

            """ Official Doc. Method
            new_note = form.save(commit=False) # form을 구성하기, DB엔 저장하지 않음
            new_note.categories = form.cleaned_data['categories']
            new_note.title = form.cleaned_data['title']
            new_note.contents = form.cleaned_data['contents']
            new_note.ref_link = form.cleaned_data['ref_link']
            new_note.created_by = request.user
            new_note.save() # form에 적힌 내용을 저장하기
            form.save_m2m() # Many to Many, 다대다 연결
            """
        else:
            return redirect('notes:create_page')
        return redirect('notes:main_page')

@login_required
def detail_page(request, id): # 개별글 보기 : 작성된 글 상세보기 링크
    # 데이터 유효성 검사 - 선택한 게시글 아이디 확인 및 읽어오기
    # 비지니스 로직 - 해당 아이디의 카테고리, 제목, 본문, 참조링크, 태그등을 html에 전달
    # 응답 - 전달된 데이터로 render
    user = request.user
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return redirect('notes:main_page')
    if user != note.created_by:
        return redirect('notes:main_page')
    context = {
        'note':note,
        }
    return render(request, 'notes/detail.html', context)

@login_required
def edit_page(request, id): # 개별글 수정 : 작성된 글 수정 링크
    # GET : 기존 데이터 표기, render
    # POST
    # 데이터 유효성 검사 - 수정하는 게시글 내용 읽어오기
    # 비지니스 로직 - 신규 데이터를 해당되는 모델에 입력하고, 저장
    # 응답 - 해당되는 detail 페이지로 redirect
    ## Tag 수정할때 변경되는 로직이 필요한데?
    target = get_object_or_404(Note, id=id, created_by=request.user)
    if request.method=='GET':
        forms = NoteEditForm(instance= target)
        return render(request, 'notes/create.html', {'forms':forms,'notepage':'on'})
    else:
        forms = NoteEditForm(request.POST)
        if forms.is_valid():
            new_categories = Category2.objects.get(id=request.POST["categories"])
            new_title = request.POST.get('title')
            new_contents = request.POST.get('contents')
            new_ref_link = request.POST.get('ref_link')

            target.categories = new_categories
            target.title = new_title
            target.contents = new_contents
            target.ref_link = new_ref_link

            target.save()
            return redirect('notes:detail_page', target.id)

@login_required
def delete_page(request, id): # 개별글 삭제 : 작성된 글 삭제 페이지, Hard-Delete
    # GET : 삭제할 데이터 표기
    # POST
    # 데이터 유효성 검사 - 삭제 요청한 게시글 아이디 확인
    # 비지니스 로직 - 데이터 삭제 요청 재 확인 후 delete
    # 응답 - main-page로 redirect
    target = get_object_or_404(Note, id=id)
    if request.user != target.created_by:
        warn = messages.warning(request, "권한이 없습니다.")
        context = {
            'message': warn,
            'note': target,
        }
        return render(request, 'notes/detail.html', context)
    
    if request.method == "GET":
        context = {
            'note':target,
            'deleteorder': 'On'
        }
        return render(request, 'notes/detail.html', context)
    elif request.method == "POST":
        target.delete()
        return redirect('notes:main_page')

#tsearch_page, Taggit 모듈 사용으로 삭제(22.05.14)
#Taggit 제공 view 사용으로 변경(22.05.14)
class TagCloudTV(TemplateView):
    template_name= "taggit/tagsearch.html"

class TaggedObjectLV(ListView):
    template_name= "taggit/tagresult.html"
    model: Note

    def get_queryset(self):
        return Note.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

@login_required
def ctgr_view(request): # 생성된 카테고리 보기(22.05.12 추가)
    # 데이터 유효성 검사 - 로그인 유저 확인, 생성한 카테고리 확인
    # 비지니스 로직 - Category2써서 현재 유저가 생성한 카테고리를 확인
    # 응답 - 카테고리 리스트 표시
    current_user = request.user
    ctgy_manage_list = Category.objects.filter(created_by = current_user).order_by('id')
    ctgy2_manage_list = Category2.objects.filter(created_by = current_user).order_by('id')
        
    context = { 
        'category_manage_order':'On',
        'ctgy1':ctgy_manage_list, 
        'ctgy2':ctgy2_manage_list,
        }

    return render(request, 'notes/category.html', context)

@login_required
def ctgr1_create(request): # 카테고리 생성(22.05.12 추가)
    # GET : 재 렌더링
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인
    # 비지니스 로직 - 상위인지 하위인지 확인하고, 해당 신규 카테고리 생성
    # 응답 - main_page redirect
    if request.method=='GET':
        form = Ctgr1CreateForm()
        context = {
            'forms':form,
            'ctgypage':'1'
            }
        return render(request, 'notes/create.html', context)
    else:
        form = Ctgr1CreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                cate_name = form.cleaned_data['cate_name'],
                created_by = request.user,
            )
        else:
            return redirect('notes:create_page')
        return redirect('notes:ct_manage_view')

@login_required
def ctgr1_edit(request, id): # 카테고리 삭제(22.05.12 추가)
    # GET : 기존 카테고리명 표기
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인, 카테고리 생성자 확인
    # 비지니스 로직 - 생성자와 로그인 유저가 동일할때, 삭제처리
    # 응답 - main_page redirect
    target = get_object_or_404(Category, id=id, created_by=request.user)
    if request.method=='GET':
        forms = Ctgr1EditForm(instance= target)
        return render(request, 'notes/create.html', {'forms':forms,'ctgypage':'1'})
    else:
        forms = Ctgr1EditForm(request.POST)
        if forms.is_valid():
            new_categories = request.POST.get('cate_name')
            target.cate_name = new_categories
            target.save()
            return redirect('notes:ct_manage_view')

@login_required
def ctgr1_delete(request, id): # 카테고리 삭제(22.05.12 추가)
    # GET : 재 렌더링
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인, 카테고리 생성자 확인
    # 비지니스 로직 - 생성자와 로그인 유저가 동일할때, 삭제처리
    # 응답 - main_page redirect
    target = get_object_or_404(Category, id=id)
    if request.user != target.created_by:
        warn = messages.warning(request, "권한이 없습니다.")
        context = {
            'message': warn,
            'ctgy': target,
        }
        return render(request, 'notes/detail.html', context)
    
    if request.method == "GET":
        context = {
            'ctgy':target,
            'delete1order': 'On'
        }
        return render(request, 'notes/category.html', context)
    elif request.method == "POST":
        target.delete()
        return redirect('notes:ct_manage_view')

@login_required
def ctgr2_create(request): # 카테고리 생성(22.05.12 추가)
    # GET : 재 렌더링
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인
    # 비지니스 로직 - 상위인지 하위인지 확인하고, 해당 신규 카테고리 생성
    # 응답 - main_page redirect
    if request.method=='GET':
        form = Ctgr2CreateForm()
        context = {
            'forms':form,
            'ctgypage':'1'
            }
        return render(request, 'notes/create.html', context)
    else:
        form = Ctgr2CreateForm(request.POST)
        if form.is_valid():
            Category2.objects.create(
                P_cate_name = form.cleaned_data['P_cate_name'],
                cate2_name = form.cleaned_data['cate2_name'],
                created_by = request.user,
            )
        else:
            return redirect('notes:create_page')
        return redirect('notes:ct_manage_view')

@login_required
def ctgr2_edit(request, id): # 카테고리 삭제(22.05.12 추가)
    # GET : 기존 카테고리명 표기
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인, 카테고리 생성자 확인
    # 비지니스 로직 - 생성자와 로그인 유저가 동일할때, 삭제처리
    # 응답 - main_page redirect
    target = get_object_or_404(Category2, id=id, created_by=request.user)
    if request.method=='GET':
        forms = Ctgr2EditForm(instance= target)
        return render(request, 'notes/create.html', {'forms':forms, 'ctgypage':'1'})
    else:
        forms = Ctgr2EditForm(request.POST)
        if forms.is_valid():
            new_p_category = request.POST.get('P_cate_name')
            new_categories = request.POST.get('cate2_name')
            
            target.P_cate_name.id = new_p_category
            target.cate2_name = new_categories

            target.save()
            return redirect('notes:ct_manage_view')

@login_required
def ctgr2_delete(request, id): # 카테고리 삭제(22.05.12 추가)
    # GET : 재 렌더링
    # POST
    # 데이터 유효성 검사 - 로그인 유저 확인, 현재 생성된 카테고리 확인, 카테고리 생성자 확인
    # 비지니스 로직 - 생성자와 로그인 유저가 동일할때, 삭제처리
    # 응답 - main_page redirect
    target = get_object_or_404(Category2, id=id)
    if request.user != target.created_by:
        warn = messages.warning(request, "권한이 없습니다.")
        context = {
            'message': warn,
            'ctgy': target,
        }
        return render(request, 'notes/detail.html', context)
    
    if request.method == "GET":
        context = {
            'ctgy':target,
            'delete2order': 'On'
        }
        return render(request, 'notes/category.html', context)
    elif request.method == "POST":
        target.delete()
        return redirect('notes:ct_manage_view')

""" Patch Note
    22.05.06/ Initialize, 기초 틀 구성
    22.05.09/ Logic Memo 추가, Models-Tag 수정, Admin 화면 구성
    22.05.11/ login, logout. index 구성
    22.05.12/ main_page, category_page 구성, admin, url 수정
    22.05.12/ 카테고리 관리 페이지 별도 생성 구조 작성
    22.05.14/ 태그 기능 추가 구성, 외부 모듈 사용
    22.05.15/ create, detail 기능 구현
    22.05.16/ edit, delete, tag 기능 구현
"""