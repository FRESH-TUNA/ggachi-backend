from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import LetterViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'letters', LetterViewSet, basename='letter')


# comments_router = NestedSimpleRouter(router, r'flowers', lookup='flower')
# comments_router.register(r'comments', CommentFlowerViewSet, base_name='flower_comments')

urlpatterns = [
    path('', include(router.urls)),
]