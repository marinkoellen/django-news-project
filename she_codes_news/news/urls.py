from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(),name='story'),
    path('add-story/', views.AddStoryView.as_view(), name = 'newsStory'),
    path('edit/<int:pk>/', views.EditStoryView.as_view(),name='editStory'),
    path('delete/<int:pk>/', views.DeleteStoryView.as_view(),name='deleteStory'),
    path('one_author/<str:username>/', views.OneAuthorView.as_view(), name = 'one_author'),
]
