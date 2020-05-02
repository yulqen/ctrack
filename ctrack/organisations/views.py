from typing import Any
from typing import Dict

from crispy_forms.layout import Submit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .forms import OrganisationCreateForm, AddressInlineFormSet, OrganisationInlineFormSetHelper
from .models import Organisation


class OrganisationCreate(CreateView):
    model = Organisation
    template_name = "organisations/org_create_formset.html"
    form_class = OrganisationCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["addresses"] = AddressInlineFormSet(self.request.POST)
        else:
            context["addresses"] = AddressInlineFormSet()
            context["helper"] = OrganisationInlineFormSetHelper()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context["addresses"]
        with transaction.atomic():
            form.instance.updated_by = self.request.user
            self.object = form.save()
            if addresses.is_valid():
                addresses.instance = self.object
                addresses.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("organisations:detail", kwargs={"slug": self.object.slug})


class OrganisationListView(LoginRequiredMixin, ListView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organisation_list"] = Organisation.objects.all().order_by("name")
        return context


class OrganisationDetailView(LoginRequiredMixin, DetailView):
    model = Organisation

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        org = kwargs['object']
        no_addr = org.addresses.count()
        if no_addr > 1:
            context['no_addr'] = no_addr
            addr = org.addresses.all()
            context['addr'] = addr
        else:
            context['no_addr'] = 1
            addr = org.addresses.first()
            context['addr'] = addr
        people = org.person_set.all()
        context['people'] = people
        applicable_systems = org.applicablesystem_set.all()
        context['applicable_systems'] = applicable_systems
        return context
