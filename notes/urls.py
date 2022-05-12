from django.urls import path
from .views import main_page, Pcategory_page, Scategory_page, create_page, detail_page, edit_page, delete_page, tsearch_page

app_name = 'notes'

"""
필요한 페이지 
1. 로그인 후 보여줄 메인페이지 : 작성된 전체글, 부모 카테고리 지정 링크
2. 부모 카테고리 : 부모 카테고리에 포함된 모든 글 및 자식 카테고리 지정 링크
3. 자식 카테고리 : 자식 카테고리에 포함된 모든 글 링크
4. 글 쓰기 : 새로운 글 쓰기
5. 개별글 보기 : 작성된 글 상세보기 링크
6. 개별글 수정 : 작성된 글 수정 링크
7. 개별글 삭제 : 작성된 글 삭제 페이지, Hard-Delete
8. 태그별 보기 : 작성된 글 중에서 태그에 해당되는 글 리스트 출력
"""

urlpatterns = [
    path('main/', main_page, name='main_page'),
    path('category/<str:cate_name>', Pcategory_page, name='Pcategory_page'),
    path('category/category2/<str:cate2_name>', Scategory_page, name='Scategory_page'),
    path('new/', create_page, name='create_page'),
    path('<int:id>/', detail_page, name='detail_page'),
    path('<int:id>/edit/', edit_page, name='edit_page'),
    path('<int:id>/delete/', delete_page, name='delete_page'),
    path('tagsearch/',tsearch_page, name='Tsearch_page')
]