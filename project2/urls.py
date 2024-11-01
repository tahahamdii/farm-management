"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('logout',LogoutView.as_view(next_page='/'),name='logout'),
    path('about',about,name='about'),

    path('ajax/load-regions/', load_regions, name='ajax_load_regions'),

    #<-----Admin URLs----->

    path('admin_login',admin_login,name='admin_login'),
    path('admin_home',admin_home,name='admin_home'),
    path('admin_profile', admin_profile, name='admin_profile'),
    path('change_password_admin', change_password_admin, name='change_password_admin'),

    path('admin_approve_visitor', admin_approve_visitor,name='admin_approve_visitor'),
    path('approve_visitor', approve_visitor, name='approve_visitor'),
    path('delete_visitor', delete_visitor, name='delete_visitor'),

    path('admin_approve_seller', admin_approve_seller,name='admin_approve_seller'),
    path('approve_seller', approve_seller, name='approve_seller'),
    path('delete_seller', delete_seller, name='delete_seller'),


    path('admin_add_admin', admin_add_admin, name='admin_add_admin'),
    path('admin_active_admin', admin_active_admin,name='admin_active_admin'),
    path('delete_admin_active', delete_admin_active, name='delete_admin_active'),

    path('admin_active_visitor', admin_active_visitor,name='admin_active_visitor'),
    path('delete_visitor_active', delete_visitor_active, name='delete_visitor_active'),

    path('<int:id>/detail_seller', detail_seller,name='detail_seller'),
    path('<int:id>/detail_active_seller', detail_active_seller,name='detail_active_seller'),

    path('admin_active_seller', admin_active_seller,name='admin_active_seller'),
    path('delete_seller_active', delete_seller_active, name='delete_seller_active'),



    path('admin_product',admin_product,name='admin_product'),
    path('<int:id>/detail_product_admin',detail_product_admin,name='detail_product_admin'),
    path('<int:id>/detail_request_product_admin',detail_request_product_admin,name='detail_request_product_admin'),
    path('admin_request_product',admin_request_product,name='admin_request_product'),
    path('product_approve',product_approve,name='product_approve'),
    path('product_delete',product_delete,name='product_delete'),

    path('inactive',inactive,name='inactive'),
    path('active',active,name='active'),
    path('approve_product_delete',approve_product_delete,name='approve_product_delete'),

    #<-----Visitor URLs----->

    path('visitor_signup',visitor_signup,name='visitor_signup'),
    path('visitor_login',visitor_login,name='visitor_login'),
    path('visitor_home',visitor_home,name='visitor_home'),
    path('visitor_profile', visitor_profile, name='visitor_profile'),
    path('change_password_visitor', change_password_visitor, name='change_password_visitor'),

    path('visitor_add_soil', visitor_add_soil, name='visitor_add_soil'),

    path('visitor_find_soil',visitor_find_soil, name='visitor_find_soil'),
    path('visitor_find_soil_detail',visitor_find_soil_detail, name='visitor_find_soil_detail'),
    path('visitor_find_rainfall',visitor_find_rainfall, name='visitor_find_rainfall'),


    path('visitor_get_seed',visitor_get_seed, name='visitor_get_seed'),
    path('visitor_get_fertilizer',visitor_get_fertilizer, name='visitor_get_fertilizer'),
    
    path('visitor_seed_request',visitor_seed_request, name='visitor_seed_request'),
    path('visitor_fertilizer_request',visitor_fertilizer_request, name='visitor_fertilizer_request'),

    path('visitor_market_home',visitor_market_home, name='visitor_market_home'),
    path('search',search, name='search'),
    path('<int:id>/view_product_visitor',view_product_visitor, name='view_product_visitor'),
    




    path('vegetable_cat',vegetable_cat, name='vegetable_cat'),
    path('fruit_cat',fruit_cat, name='fruit_cat'),
    path('seed_cat',seed_cat, name='seed_cat'),
    path('bio_cat',bio_cat, name='bio_cat'),
    path('nut_cat',nut_cat, name='nut_cat'),
    path('spices_cat',spices_cat, name='spices_cat'),

    path('<int:id>/visitor_view_seller',visitor_view_seller, name='visitor_view_seller'),


    #<-----Sellers URLs----->

    path('seller_signup',seller_signup,name='seller_signup'),
    path('seller_login',seller_login,name='seller_login'),
    path('seller_home',seller_home,name='seller_home'),
    path('seller_profile',seller_profile,name='seller_profile'),
    path('change_password_seller', change_password_seller, name='change_password_seller'),

    path('product',product,name='product'),
    path('<int:id>/detail_product_seller',detail_product_seller,name='detail_product_seller'),
    path('add_product',add_product,name='add_product'),
    path('outofstock',outofstock,name='outofstock'),
    path('instock',instock,name='instock'),
    path('delete_product_seller',delete_product_seller,name='delete_product_seller'),


    path('shipped_package',shipped_package,name='shipped_package'),
    path('shipped_order_seller',shipped_order_seller,name='shipped_order_seller'),
    path('delivered_order',delivered_order,name='delivered_order'),
    path('delivered_order_seller',delivered_order_seller,name='delivered_order_seller'),
    path('canceled_order_seller',canceled_order_seller,name='canceled_order_seller'),


    # <-----Products Prediction URLs----->
    path('products_sales',predict_sales,name='products_sales'),
    path('predict_best_selling_product',predict_best_selling_product, name='predict_best_selling_product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)