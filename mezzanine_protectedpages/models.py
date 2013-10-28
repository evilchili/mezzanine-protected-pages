from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from django.contrib.auth.models import Group


class ProtectedPage(Page, RichText):
    """
    Create a new content type that behaves just like a RichText Page, except that it includes a
    reference to django.contrib.auth.models.Group.
    """
    groups = models.ManyToManyField(Group)
