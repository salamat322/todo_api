from django.urls import path

from .import views


urlpatterns = [
    path('tags', views.TagView.as_view(), name='tags-list'),
    path('tags/create', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>', views.TagRetrieve.as_view(), name='tag-detail'),
]