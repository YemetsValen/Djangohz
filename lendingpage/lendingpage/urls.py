
from django.contrib import admin
from django.urls import path
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page)
    path('thanks/', views.thank_page, name='thank_page')
]
