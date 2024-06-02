from django.urls import path
from . import views


urlpatterns = [
    path('get_userdata/', views.profile),
    path('update/',views.update),
    path('delete_account/', views.delete_account),
    path('add_product/<str:product_cd>/<str:option_trm>', views.add_product), 
    path('get_added_product/', views.get_added_product), 
    # path('get_user_products/', views.get_user_products, name='get_user_products'),
    # path('check_product/<str:product_cd>/<str:option_trm>/', views.check_product),
]