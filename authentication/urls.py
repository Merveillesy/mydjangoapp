from django.contrib.auth.views import LoginView
    
urlpatterns = [
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    # path('profile-photo/upload', authentication.views.upload_profile_photo,
        #  name='upload_profile_photo'),
]