from django.urls import path
from .views import signup,login_view,logout_view
#,profile_update,profile_detail

urlpatterns = [
    path('api/signup/', signup, name='api-signup'),
    path('api/signin/', login_view, name='api-signin'),
    #path('profile/<int:user_id>/', profile_detail, name='profile_detail'),
    #path('profile/update/<int:user_id>/', profile_update, name='profile_update'),
    path('api/logout/', logout_view, name='api-logout'),
]   