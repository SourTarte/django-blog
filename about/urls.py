from about import views
from django.urls import path

urlpatterns = [
    path('blog/', views.about_me, name='about'),
]