from django.utils.functional import LazyObject
from django.contrib.admin import AdminSite


class OverwrittenAdminSite(AdminSite):
    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active and request.user.is_staff or request.user.is_owner

class OverwrittenDefaultAdminSite(LazyObject):
    def _setup(self):
        AdminSiteClass = OverwrittenAdminSite
        self._wrapped = AdminSiteClass()

    def __repr__(self):
        return repr(self._wrapped)


# This global object represents the default admin site, for the common case.
# You can provide your own AdminSite using the (Simple)AdminConfig.default_site
# attribute. You can also instantiate AdminSite in your own code to create a
# custom admin site.
site = OverwrittenDefaultAdminSite()