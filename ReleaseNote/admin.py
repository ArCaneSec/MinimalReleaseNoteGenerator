from django.contrib import admin
from . import models as m
from django.urls import reverse
from django.utils.safestring import mark_safe
from jalali_date.admin import StackedInlineJalaliMixin, datetime2jalali, ModelAdminJalaliMixin


@admin.register(m.User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name"]


class DetailskInline(StackedInlineJalaliMixin, admin.StackedInline):   
    model = m.ReleaseNoteDetail
    extra = 1
    autocomplete_fields = ["assigned_to"]
    

@admin.register(m.Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(m.ReleaseNote)
class ReleaseNoteAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):

    list_display = ["version_number_link", "published_date_jalali", "project", "assigned_to"]
    autocomplete_fields = ["project"]
    list_display_links = ["assigned_to"]
    date_hierarchy = "published_date"
    inlines = [DetailskInline]

    @admin.display(description="Published date")
    def published_date_jalali(self, obj):
        return datetime2jalali(obj.published_date).strftime('%a, %d %b %Y %H:%M:%S')

    @admin.display
    def assigned_to(self, obj):
        user = obj.releasenotedetail_set.first().assigned_to
        if user is None:
            return None

        url = reverse('admin:%s_%s_change' % (user._meta.app_label,  user._meta.model_name),  args=[user.id])
        return mark_safe(f'<a href="{url}">{user.full_name}</a>')
    
    @admin.display
    def version_number_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
        return mark_safe(f'<a href="{url}">{obj.version_number}</a>')