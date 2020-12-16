from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from django_comments_xtd.admin import XtdCommentsAdmin

class DescriptionAdmin(SummernoteModelAdmin):
	summernote_fields = ('description',)

class ReportCommentAdmin(XtdCommentsAdmin):
	list_display = ('thread_level', 'cid', 'name', 'content_type',
					'object_pk', 'submit_date', 'followup', 'is_public',
					'is_removed')
	fieldsets = (
		(None,          {'fields': ('content_type', 'object_pk', 'site')}),
		(_('Content'),  {'fields': ('user', 'user_name', 'user_email',
									'user_url', 'comment', 'followup')}),
		(_('Metadata'), {'fields': ('submit_date', 'ip_address',
									'is_public', 'is_removed')}),
	)

# Register your models here.
admin.site.register(IncidentTicket, DescriptionAdmin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Source)
admin.site.register(Impact)
admin.site.register(Urgency)
admin.site.register(ReportComment, ReportCommentAdmin)
