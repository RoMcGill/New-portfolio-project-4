''' import summer note wysiwyg library'''
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from.models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    ''' uses summer note for content '''

    summernote_fields = ('content')
