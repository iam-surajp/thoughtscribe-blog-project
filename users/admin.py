from django.contrib import admin
from .models import profileModel, interestModel
# Register your models here.


class interestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'interests_list']

    def interests_list(self, obj):
        return ", ".join([interest.title for interest in obj.interests.all()])


admin.site.register(profileModel)
admin.site.register(interestModel, interestAdmin)
