from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import (RegisterView, LoginView, CourseViewSet, GroupViewSet, TeacherViewSet, StudentViewSet, LessonViewSet, CommentViewSet,
                    UpdateViewSet, LikeDislikeViewSet, SearchLesson)

router = SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'likes', LikeDislikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'updates', UpdateViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('search/', SearchLesson.as_view()),
]

