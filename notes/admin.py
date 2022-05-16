from django.contrib import admin

from .models import Category, Category2, Note
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_name']
    list_filter = ['cate_name',]
    search_field = ['cate_name',]
    search_help_text = '상위 카테고리 검색'
    readonly_field = ['cate_name']
    verbose_name = '상위 카테고리'
    verbose_name_plural = '상위 카테고리'

@admin.register(Category2)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate2_name', 'P_cate_name']
    list_filter = ['P_cate_name']
    search_field = ['P_cate_name', 'cate2_name']
    search_help_text = '하위 카테고리 검색'
    verbose_name = '하위 카테고리'
    verbose_name_plural = '하위 카테고리'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','categories','created_by','created_at','tag_list']
    list_filter = ['categories', 'created_by',]
    search_field = ['categories', 'created_by',]
    search_help_text = '카테고리 검색 혹은 작성자 검색'
    readonly_field = ['created_at', 'modified_at',]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())