from django.urls import path
from .views import CourseDetailView,CourseListView

urlpatterns = [
    path('course/',CourseListView.as_view() ),
    path('course/<int:id>',CourseDetailView.as_view()),
    
    
]