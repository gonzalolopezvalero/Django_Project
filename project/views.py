from django.views.generic import RedirectView


class RedirectToAdmin(RedirectView):
    pattern_name = "admin:index"