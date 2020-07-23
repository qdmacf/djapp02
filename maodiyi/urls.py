from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('index',views.index,name="index"),
    path('math',views.mathtest,name="mathtest"), 
    path('guess/',views.guess,name="guess"),
    path('jobs',views.job_query,name="job_query"),
    path('bgsig', views.bgsig, name="bgsig"),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
]
