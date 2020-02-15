from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.posts, name='posts' ),
    path('single-post/<post>/', views.single_post, name='single_post'),
    path('search/', views.search_project, name='search'),

    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    # path('profile/<username>/', views.profile, name='profile' ),
]