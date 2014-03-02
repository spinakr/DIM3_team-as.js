
from django.contrib import admin
from recap.models import UserProfile, Category, Requirement, RecapProject


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Requirement)
admin.site.register(RecapProject)

