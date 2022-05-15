'''
글 생성, 수정, 읽기 폼 필요
카테고리 생성, 읽기, 수정 폼 ->(선결) Models.py 수정해서 카테고리마다 유저를 받도록 변경
'''

from django import forms
from django.core.exceptions import ValidationError

from .models import Note

class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class NoteCreateForm(NoteBaseForm):
    class Meta(NoteBaseForm.Meta):
        fields = ['categories', 'title', 'contents', 'ref_link','tags',]