from django.urls import path, include
from . import views
# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# router.register(prefix='categories', viewset=views.CategoryViewSet, basename="category")
# router.register(prefix='course', viewset=views.CourseViewSet, basename='course')
# router.register(prefix='lesson', viewset=views.LessonViewSet, basename='lesson')
# router.register(prefix='comments', viewset=views.CommentViewSet, basename='comment')
# router.register(prefix='users', viewset=views.UserViewSet, basename='user')

urlpatterns = [
    # path('', views.index, name='course_index'),
    # path('', include(router.urls)),
    path('', views.index, name='clinic_index')
]