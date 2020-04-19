from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Field, Hidden
from crispy_forms.layout import ButtonHolder
from crispy_forms.layout import Fieldset
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms
from django.forms import inlineformset_factory
from django.urls import reverse

from ctrack.caf.models import ApplicableSystem
from ctrack.caf.models import CAF

CAFCreateInlineFormset = inlineformset_factory(
    CAF, ApplicableSystem, fields=("name", "organisation"), extra=2)


class ApplicableSystemCreateFromOrgForm(forms.ModelForm):

    class Meta:
        model = ApplicableSystem
        fields = ["name", "description", "caf", "organisation"]

    def __init__(self, org_id, slug, org_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cancel_redirect = reverse("organisations:detail", args=[slug])
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                f"Create a new system for {org_name}",
                Field("name", css_class="form-control form-control-sm"),
                Field("description", css_class="form-control form-control-sm"),
                Hidden("organisation", org_id),
                Field("caf", css_class="form-control form-control-sm")
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="btn-primary"),
                Button("cancel", "Cancel", onclick=f"location.href='{cancel_redirect}';", css_class="btn-danger")
            )
        )

