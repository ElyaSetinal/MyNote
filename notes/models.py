from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

#모델로써 제작 되어야 할 것들 : 노트본문, 카테고리 항목, 하위 카테고리 항목

# 장고에서 제공하는 User Model 불러오기
User = settings.AUTH_USER_MODEL

class Category(models.Model): # 상위 카테고리
    class Meta: # 클래스의 이름을 지정
        verbose_name = '상위 카테고리'
        verbose_name_plural = '상위 카테고리'

    # 상위 카테고리 이름 지정
    cate_name = models.CharField(verbose_name='카테고리', max_length=20, unique=True)
    # 카테고리 생성자 지정(22.05.16)
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='Cate1_Created_User', null=True, blank=True)

    def __str__(self): # 클래스의 정보를 name으로 호출하는 함수
        return f'{self.cate_name}'

class Category2(models.Model): # 하위 카테고리
    class Meta: # 클래스의 이름을 지정
        verbose_name = '하위 카테고리'
        verbose_name_plural = '하위 카테고리'

    # 상위 카테고리 확인
    P_cate_name = models.ForeignKey(Category, verbose_name='상위 카테고리', on_delete=models.CASCADE, related_name='Cate2_Parents_name')
    # 하위 카테고리 이름 지정
    cate2_name = models.CharField(verbose_name='하위 카테고리', max_length=20, null=True, blank=True, unique=True)
    # 카테고리 생성자 지정(22.05.16)
    created_by = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE, related_name='Cate2_Created_User', null=True, blank=True)

    def __str__(self): # 클래스의 정보를 name으로 호출하는 함수
        return f'{self.cate2_name}'

class Note(models.Model):
    # 노트에 들어갈 내용들 - 제목, 내용, 작성시간, 작성자, 참조 링크, 카테고리

    class Meta: # 클래스의 이름을 지정
        verbose_name = '노트'
        verbose_name_plural = '노트'

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
    # 태그 : 외부 모듈인 Taggit 사용하여 추가, 태그별 검색을 할 수 있도록 추가
    tags = TaggableManager(verbose_name="태그", help_text="콤마(,)로 구분합니다.", blank=True)

# Tagsave 비활성화, Taggit 사용