from postCreate.models import Book,Category,ExtendUser
from django.contrib import admin
from django.contrib.auth.models import Group
from django.apps import apps

admin.site.unregister(Group)
admin.site.register(ExtendUser)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'isbn', 'price','date_created']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','id']


app = apps.get_app_config('graphql_auth')
for model_name, model in app.models.items():
    admin.site.register(model)








