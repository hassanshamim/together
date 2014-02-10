from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'together.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/', 'lists.views.list_page', name='list'),
    url(r'^admin/', include(admin.site.urls)),
)
