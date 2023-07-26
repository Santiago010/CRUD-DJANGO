"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name="signup"),
    path("logout/",views.signout,name="logout"),
    path("signin/",views.singin,name="singin"),
    path("",views.all_products,name="products"),
    path("product/<int:id>/",views.product_details,name='product_details'),
    path("product/<int:id>/delete",views.product_delete,name='product_delete'),
    path("products/create",views.create_product,name="create_product"),
    path("create/category/",views.create_category,name="create_cateogory"),
    path("category/",views.all_category,name="category"),
    path("category/<int:id>",views.category_details,name="category_details"),
    path("category/<int:id>/delete",views.category_delete,name='category_delete'),
    path('subCategory/',views.all_subCategorys,name='subCategory'),
    path('create/subCategory',views.create_subCategory,name='create_subCategory'),
    path("subCategory/<int:id>",views.subCategory_details,name="subCategory_details"),
    path("subCategory/<int:id>/delete",views.subCategory_delete,name='subCategory_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
