from django.contrib import admin

from .models import (
    Address,
    AddressType,
    IncidentReport,
    Mode,
    Organisation,
    Person,
    Role,
    Stakeholder,
    Submode,
)


# So we can get the organisation name - a reverse lookup
def get_organisation_name(person):
    return Organisation.objects.filter(person__id=person.id).first().name


# We need this to ensure the column header in the admin does't read the func name
get_organisation_name.short_description = "Organisation"


class IncidentReportAdmin(admin.ModelAdmin):
    model = IncidentReport


class AddressTypeAdmin(admin.ModelAdmin):
    pass


class StakeholderAdmin(admin.ModelAdmin):
    model = Stakeholder


class AddressInLine(admin.StackedInline):
    model = Address
    max_num = 3
    extra = 1


class OrganisationAdmin(admin.ModelAdmin):
    inlines = [AddressInLine]
    list_display = ("name", "submode", "date_updated")


class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = [
        "first_name",
        "last_name",
        "job_title",
        get_organisation_name,
        "email",
        "mobile",
    ]


class RoleAdmin(admin.ModelAdmin):
    model = Role


class ModeAdmin(admin.ModelAdmin):
    model = Mode


class SubmodeAdmin(admin.ModelAdmin):
    model = Submode


# Register your models here.
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(Submode, SubmodeAdmin)
admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(IncidentReport, IncidentReportAdmin)
