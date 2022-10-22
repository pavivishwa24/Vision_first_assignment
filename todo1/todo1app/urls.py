from django.contrib import admin
from django.urls import path
from todo1app import views
from django import forms



urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/',views.show),
    path('reg/',views.register),
    path('login/',views.login,name="login"),
    path('companies/',views.companies,name="companies"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('admin_page/',views.admin,name="admin"),
    path('approve/<int:id>/',views.approve,name="approve"),

    # path('success/',success,name="user_success"),
]