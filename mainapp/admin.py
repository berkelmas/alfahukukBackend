from django.contrib import admin
from .models import Makaleler, ContactModel, Uzmanliklar, MakaleTags
from django.contrib.auth.models import Group, User

class MakalelerAdmin(admin.ModelAdmin):
    exclude = ('makale_slug',)
admin.site.register(Makaleler, MakalelerAdmin)

class MakaleTagsAdmin(admin.ModelAdmin):
    pass
admin.site.register(MakaleTags, MakaleTagsAdmin)

class UzmanliklarAdmin(admin.ModelAdmin):
    """
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    """
admin.site.register(Uzmanliklar, UzmanliklarAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_display = ['contact_isim', 'contact_tarih']
admin.site.register(ContactModel, ContactModelAdmin)


admin.site.unregister(Group)
admin.site.site_header = "Alfa Hukuk Yönetim Paneli"
