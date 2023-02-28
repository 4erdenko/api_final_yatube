from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

]
