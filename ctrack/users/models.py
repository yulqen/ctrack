from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    oes_user = BooleanField(default=False, verbose_name="OES User")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
