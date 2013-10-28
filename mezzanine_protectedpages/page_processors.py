from mezzanine.pages.page_processors import processor_for
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.conf import settings
from urllib2 import quote
from .models import ProtectedPage


@processor_for(ProtectedPage)
def page_view(request, page):
    """
    When a protected page is requested, compare the user's group memberships to those of the page.
    If the user is a member of at least one of the page's groups, show them the page.  If they
    aren't logged in, redirect to the login page.  If they are logged in, but aren't a member of
    any required group, throw a 403.
    """
    this_page = ProtectedPage.objects.filter(slug=page.slug)
    if request.user is None:
        redirect_url = "%s?next=%s" % (settings.LOGIN_URL, quote(request.path))
        return redirect(redirect_url)
    if this_page.filter(groups__in=request.user.groups.all()):
        return {"page": page}
    else:
        return HttpResponseForbidden()
