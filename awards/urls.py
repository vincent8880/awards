from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^repos/$', views.all_repos, name='repos')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
