from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all-reviews', views.ALLIndexView.as_view(), name='index-all'),
    path('<int:pk>/', views.StoryView.as_view(),name='story'),
    path('add-story/', views.AddStoryView.as_view(), name = 'newsStory'),
    path('edit/<int:pk>/', views.EditStoryView.as_view(),name='editStory'),
    path('delete/<int:pk>/', views.DeleteStoryView.as_view(),name='deleteStory'),
    path('one_author/<str:username>/', views.OneAuthorView.as_view(), name = 'one_author'),
    path('filter/', views.CategoryFilterView.as_view(), name = 'filtering-cat'),
    path('like/<int:pk>/', views.LikeView, name = 'like-post'),
]
