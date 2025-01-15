from django.contrib import admin
from .models import employeestatus,task,todolist,leaves

# Register your models here.
admin.site.register(employeestatus)
admin.site.register(task)
admin.site.register(todolist)
admin.site.register(leaves)
