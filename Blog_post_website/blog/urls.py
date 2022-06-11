
from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView, UserListView


urlpatterns = [
    path('', ProfileListView.as_view(), name ='blog-home'),
    path('user/<str:username>', UserListView.as_view(), name ='user-post'),
    path('post/new/', ProfileCreateView.as_view(), name ='post-create'),
    path('post/<int:pk>/', ProfileDetailView.as_view(), name ='post-detail'),
    path('post/<int:pk>/update/', ProfileUpdateView.as_view(), name ='post-update'),
    path('post/<int:pk>/delete/', ProfileDeleteView.as_view(), name ='post-delete'),
    path('about/', views.about, name ='blog-about'),
]
