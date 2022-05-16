'''
글 생성, 수정, 읽기 폼 필요
카테고리 생성, 읽기, 수정 폼 ->(선결) Models.py 수정해서 카테고리마다 유저를 받도록 변경
'''

from django import forms

from .models import Note, Category, Category2

# 노트
class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class NoteCreateForm(NoteBaseForm):
    class Meta(NoteBaseForm.Meta):
        fields = ['categories', 'title', 'contents', 'ref_link','tags',]

class NoteEditForm(NoteBaseForm):
    class Meta(NoteBaseForm.Meta):
        fields = ['categories', 'title', 'contents', 'ref_link','tags',]

# 상위 카테고리
class Ctgr1BaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Ctgr1CreateForm(Ctgr1BaseForm):
    class Meta(Ctgr1BaseForm.Meta):
        fields = ['cate_name',]

class Ctgr1EditForm(Ctgr1BaseForm):
    class Meta(Ctgr1BaseForm.Meta):
        fields = ['cate_name',]

# 하위 카테고리
class Ctgr2BaseForm(forms.ModelForm):
    class Meta:
        model = Category2
        fields = '__all__'

class Ctgr2CreateForm(Ctgr2BaseForm):
    class Meta(Ctgr2BaseForm.Meta):
        fields = ['P_cate_name', 'cate2_name',]

class Ctgr2EditForm(Ctgr2BaseForm):
    class Meta(Ctgr2BaseForm.Meta):
        fields = ['P_cate_name', 'cate2_name',]