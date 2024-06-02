from django.urls import path
from . import views

urlpatterns = [
    # 게시글
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),

    # 댓글
    path('<int:article_pk>/comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/create/', views.comment_create),

    # 좋아요
    path('<int:article_pk>/likes/', views.likes),
    path('<int:article_pk>/like-status/', views.get_like_status),
    path('<int:article_pk>/like-count/', views.get_like_count),  # 추가된 URL 패턴

    # 사용자가 좋아요 누른 글 목록
    path('profile/liked-articles/', views.liked_articles),
]
