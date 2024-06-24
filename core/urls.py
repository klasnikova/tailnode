import uuid
from django.urls import path, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve
from . import views
from .sitemaps import TNWebSitemap

sitemaps = {
    'index': TNWebSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('get-started', views.get_started, name='get-started'),
    path('initialize/<uuid:uuid>', views.initialize_tailnode_site_data, name='initialize-tailnode-site-data'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-out', auth_views.LogoutView.as_view(), name='sign-out'),
    path('our-project', views.our_project, name='our-project'),
    path('add-project', views.add_project, name='add-project'),
    path('edit-project/<str:project_id>', views.edit_project, name='edit-project'),
    path('delete-project/<str:project_id>', views.delete_project, name='delete-project'),
    path('settings', views.site_settings, name='settings'),
    path('settings/edit-social-media/<str:social_name>', views.edit_social_media, name='edit-social-media'),
    path('settings/edit-service-excellence/<str:service_id>', views.edit_service_excellence, name='edit-service-excellence'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots.txt$', serve, {
        'path': 'robots.txt',
        'document_root': settings.STATIC_ROOT,
    }),
]