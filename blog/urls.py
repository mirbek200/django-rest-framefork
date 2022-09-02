from django.urls import path
from .views import PostListApiView, PostCreateApiView, PostDetailApiView, PostUpdateApiView, PostDestroyApiView


urlpatterns = [
    path('list/', PostListApiView.as_view(), name='list'),
    path('create/', PostCreateApiView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateApiView.as_view(), name='update'),
    path('delete/<int:pk>', PostDestroyApiView.as_view(), name='delete'),
    path('detail/<int:pk>', PostDetailApiView.as_view(), name='detail')
]
