from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from articles.views import ArticlesView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesSubView
from . import settings
from profiles.views import Testview, Loginview, Logoutview, ProfileDetail, ProfileChange, Profiles, Registerview, \
    CreateMessage, inbox, ProfileFollowingCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Testview, name='home'),

    path('login/', Loginview, name='login'),
    path('logout/', Logoutview, name='logout'),
    path('register/', Registerview, name='register'),

    path('profile/<int:pk>/', ProfileDetail, name='profile'),
    path('profile/follow/<int:pk>/', ProfileFollowingCreateView.as_view(), name='profiles'),
    path('profile-change/<int:pk>/', ProfileChange, name='change-profile'),
    path('profiles/', Profiles, name='profiles'),

    path('article/<int:pk>/', ArticlesDetailView.as_view(), name='article'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('articles/sub/', ArticlesSubView.as_view(), name='articles-sub'),
    path('articles/create/', ArticlesCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit', ArticlesUpdateView.as_view(), name='article-edit'),

    path('create-message/', CreateMessage, name='create-message'),
    path('inbox/', inbox, name='inbox'),

    # path('sub/', Subscribe, name='sub'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
