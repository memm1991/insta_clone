"""pathing"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views as users_views




from insta_clone import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', local_views.hola),
    path('query/',local_views.query),
    path('params/<str:name>/<int:age>',local_views.params),
    #posts path
    path('posts/', posts_views.list_posts),
    #users path
    path('users/login', users_views),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
