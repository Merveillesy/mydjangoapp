from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import(LoginView)

import authentication.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='authentication/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('photo_upload/',blog.views.photo_upload,name='photo_upload'),
    path('blog/create', blog.views.blog_and_photo_upload, name='blog_create'),
    path('home/',blog.views.home, name ='home'),
    path('blog/<int:blog_id>',blog.views.view_blog,name='view_blog'),
    path('profile_photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('blog/<int:blog_id>/edit',blog.views.edit_blog,name='edit_blog'),
    path('photo/upload-multiple/', blog.views.create_multiple_photos,
    name='create_multiple_photos'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)