from django.urls import path
from app1 import views  

urlpatterns = [
    path('',views.home,name='home'),
    path('booklist/',views.booklist,name='booklist'),
    path('bookupload/',views.bookupload,name='bookupload'),
    path('aboutus/',views.aboutus,name="aboutus"),
]
