from django.contrib import admin
from django.urls import path
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static
from users.views import *
# New

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('detail/<int:id>', detail_view, name="detail"),
    path('create/', create_view, name='create'),
    path('delete/<int:id>', delete_view, name='delete'),
    path('update/<int:id>', update_view, name='update'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
