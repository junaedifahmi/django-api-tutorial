from django.contrib import admin

# Register your models here.
from blog.models import Articles, Comment

admin.site.register(Articles)

admin.site.register(Comment)

