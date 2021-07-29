from django.contrib import admin
from .models import UserProfile
# Register your models here.
from django.contrib.auth.hashers import check_password,make_password

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username','last_login','department')

    def save_model(self, request, obj, form, change):
        user_database = UserProfile.objects.get(pk=obj.pk)
        # Check firs the case in which the password is not encoded, then check in the case that the password is encode
        if not (check_password(form.data['password'], user_database.password) or user_database.password == form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user_database.password
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile,UserModelAdmin)
admin.site.site_title="E Votting System"
admin.site.index_title="E Votting System"
admin.site.site_header="E Votting System Admin Panel"