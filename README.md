mezzanine-protected-pages
=========================

Django app that restricts access to mezzanine page content based on group membership.


Installation
------------

Clone and copy the repo into your project apps (or submodule it, etc) and add the app 
to your mezzanine installed apps:

```python
INSTALLED_APPS = (
	# ...
	"mezzanine_protectedpages",
)
```


Usage
-----

After installation, you will have the new page type "Protected Page" in your mezzanine admin.
This is identical to a Rich Text Page, except that it also includes a select form for groups.
Selecting one-or-many groups will restrict access to the page to users who are members of 
that group.  

If a user who is not logged in attempts to access a protect page, they will be redirected to 
the login page (as defined by `settings.LOGIN_URL`). Users who are already logged in, but not 
members of at least one of the specified groups, will get a 403 error.

License
-------

(K) ALL RIGHTS REVERSED - Do what thou wilt.
