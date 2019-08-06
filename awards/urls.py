from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^repos/$', views.all_repos, name='repos'),
    url(r'^site/(\d+)',views.site,name='site'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^directory/',views.directory, name='directory'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^new/project$',views.new_project, name='new-project'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
