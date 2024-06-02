from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    # 정기예금 상품 목록 DB에 저장
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    # 전체 정기예금 상품 목록 출력 & 데이터 삽입
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    # 특정 상품의 옵션 리스트 출력 
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options, name='deposit_products_options'),
    # 정기적금 상품 목록 DB에 저장
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    # 전체 정기적금 상품 목록 출력 & 데이터 삽입
    path('saving-products/', views.saving_products, name='saving_products'),
    # 특정 상품의 옵션 리스트 출력 
    path('saving-products-options/<str:fin_prdt_cd>/', views.saving_products_options, name='saving_products_options'),

    # 추천 알고리즘
    # path('recommendations/', views.recommend_financial_products, name='recommendations'),
    path('recommend/', views.recommend_products)
]

