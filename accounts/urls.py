from django.urls import path
from .views import TestProtectedView
from .views import SignupView

urlpatterns = [
    path('test/', TestProtectedView.as_view()),
    path('signup/', SignupView.as_view()),
]
