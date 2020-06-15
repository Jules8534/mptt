from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

from genre.models import FileObject

admin.site.register(FileObject, DraggableMPTTAdmin)
