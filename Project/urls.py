"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.conf.urls import handler400, handler403, handler404, handler500

# import model
from expenses.models import Expense


info_dict = {
    "queryset": Expense.objects.all(),
    "date_field": "date",
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # Local apps URL Configuration
    path("", include("income.urls")),
    path("accounts/", include("accounts.urls")),
    path("expenses/", include("expenses.urls")),
    # Sitemap and robots.txt URL Configuration
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "expense": GenericSitemap(
                    info_dict,
                    priority=0.6,
                    changefreq="weekly",
                )
            }
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="config/robots.txt", content_type="text/plain"
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Customizing-error-views
handler404 = "accounts.views.page_not_found_error"
handler500 = "accounts.views.page_error"
# handler403 = "accounts.views.error_403"
# handler400 = "accounts.views.error_400"
