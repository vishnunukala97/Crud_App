"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



from django.urls import path
from items.views import *

urlpatterns = [
    path('', item_list, name='item_list'),
    path('create/', item_create, name='item_create'),
    path('<int:pk>/update/', item_update, name='item_update'),
    path('<int:pk>/delete/', item_delete, name='item_delete'),
]


urlpatterns = [
    path('', read_items, name='read_items'),
    path('create/', create_item, name='create_item'),
    path('update/<int:pk>/', update_item, name='update_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]