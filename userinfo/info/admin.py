from django.contrib import admin
from info.models import User,UserDoc
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','phone_number','address',"is_staff","is_superuser"]



@admin.register(UserDoc)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'bbox','docs_image_url' ,'doc_type','user']