from django.contrib import admin
from eBord.models import EBordModel, CategoryModel
from accoutUser.models import UserProfileModel

admin.site.register(EBordModel)
admin.site.register(CategoryModel)
admin.site.register(UserProfileModel)

# Register your models here.
