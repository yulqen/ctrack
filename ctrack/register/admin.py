from django.contrib import admin

from ctrack.register.models import EngagementEvent, SingleDateTimeEvent
from ctrack.register.models import EngagementType


class EngagementEventAdmin(admin.ModelAdmin):
    model = EngagementEvent
    list_display = ("type", "user", "date", "short_description", "response_date_requested")


class EngagementEventTypeAdmin(admin.ModelAdmin):
    model = EngagementEventAdmin
    list_display = ("descriptor", "enforcement_instrument", "single_date_type", "regulation_reference")


class SingleDateTimeEventAdmin(admin.ModelAdmin):
    model = SingleDateTimeEvent


admin.site.register(EngagementEvent, EngagementEventAdmin)
admin.site.register(EngagementType, EngagementEventTypeAdmin)
admin.site.register(SingleDateTimeEvent, SingleDateTimeEventAdmin)
