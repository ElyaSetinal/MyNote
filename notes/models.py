from django.db import models
from django.contrib.auth import get_user_model

#모델로써 제작 되어야 할 것들 : 노트본문, 카테고리 항목, 하위 카테고리 항목

# 장고에서 제공하는 User Model 불러오기
User = get_user_model()

class Category(models.Model): # 상위 카테고리
    # 상위 카테고리 이름 지정
    cate_name = models.CharField(verbose_name='카테고리', max_length=10)

class Category2(models.Model): # 하위 카테고리
    # 상위 카테고리 확인
    P_cate_name = models.ForeignKey(Category, verbose_name='상위 카테고리', on_delete=models.CASCADE, related_name='Cate2_Parents_name')
    # 하위 카테고리 이름 지정
    cate2_name = models.CharField(verbose_name='하위 카테고리', max_length=10, null=True, blank=True)

class Note(models.Model):
    # 노트에 들어갈 내용들 - 제목, 내용, 작성시간, 작성자, 참조 링크, 카테고리

    # 노트 카테고리 : 노트에 지정될 카테고리 항목, 2차 카테고리에 연결
    categories = models.ForeignKey(Category2, verbose_name='카테고리', on_delete=models.CASCADE, related_name='Note_Category_name')
    # 제목 : 글의 제목 / 인덱스 페이지, 전체글 보기, 카테고리별 글 보기, 개별글 보기에 표기
    title = models.CharField(verbose_name='제목', max_length=100) 
    # 내용 : 글의 본문 / 개별글 보기에만 표기
    contents = models.TextField(verbose_name='본문')
    # 작성시간 : 글이 작성된 시간 / 생성후 변경되면 안되므로 auto_now_add 사용
    created_at = models.DateTimeField(verbose_name='작성시간', auto_now_add=True)
    # 수정시간 : 글이 수정된 시간 / 수정될때마다 변경되어야 하므로 auto_now 사용
    modified_at = models.DateTimeField(verbose_name='수정시간', auto_now=True)
    # 작성자 : 글쓴이 / 장고에서 제공하는 User Model을 사용하기
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='Note_Created_User')
    # 참조링크 : CharField의 확장, 편리한 유효성 검사를 URLField를 사용. 반드시 필요한 항목은 아님
    ref_link = models.URLField(verbose_name='참조링크', max_length=300, null=True, blank=True)