from adminplus.sites import AdminSitePlus
from discourse.views import sso
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from . import views

admin.site = AdminSitePlus()
admin.autodiscover()

CACHE_SECS = 0


urlpatterns = [

    # Home Page
    url(r'^(?P<financial_year_id>\d{4}-\d{2}).yaml$',
        cache_page(CACHE_SECS)(views.home)),

    # Search results
    url(r'^(?P<financial_year_id>\d{4}-\d{2})/search-result.yaml',
        cache_page(CACHE_SECS)(views.FinancialYearPage.as_view(
            slug='search-result',
        ))),

    # Department List
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/departments.yaml', cache_page(CACHE_SECS)(views.department_list)),

    # Department
    url(r'^(?P<financial_year_id>\d{4}-\d{2})'
        '/national'
        '/departments'
        '/(?P<department_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.department),
        kwargs={'sphere_slug': 'national', 'government_slug': 'south-africa'}),
    url(r'^(?P<financial_year_id>[\w-]+)'
        '/(?P<sphere_slug>[\w-]+)'
        '/(?P<government_slug>[\w-]+)'
        '/departments'
        '/(?P<department_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.department)),


    # Contributed Dataset List
    url(r'^contributed-data.yaml', cache_page(CACHE_SECS)(views.contributed_dataset_list)),


    # Dataset
    url(r'^datasets'
        '/(?P<dataset_slug>[\w-]+).yaml$', cache_page(CACHE_SECS)(views.dataset)),

    # Authentication
    url(r'^accounts/', include('allauth.urls')),

    # SSO Provider
    url(r'^discourse/sso$', sso),

    # Admin
    url(r'^admin/', admin.site.urls),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
