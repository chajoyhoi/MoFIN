from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from .serializers import ArticleSerializer, ArticleListSerializer , CommentSerializer
from .models import Article, Comment
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
# 게시판 조회
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    # 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시글 상세
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)
    # 삭제
    # elif request.method == 'DELETE':
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        if article.user != request.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    # elif request.method == 'PUT':
    #     serializer = ArticleSerializer(article, data=request.data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
    elif request.method == 'PUT':
        if article.user != request.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # if request.method == 'GET':
    comments = Comment.objects.filter(article=article)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 상세
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        if comment.user != request.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if user in article.like_users.all():
        article.like_users.remove(user)
        is_liked = False
    else:
        article.like_users.add(user)
        is_liked = True
    
    like_count = article.like_users.count()  # 좋아요 수 계산
    context = {
        'is_liked': is_liked,
        'like_count': like_count,  # 좋아요 수 반환
    }
    return Response(context)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_like_status(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    is_liked = user in article.like_users.all()
    return Response({'is_liked': is_liked})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liked_articles(request):
    user = request.user
    liked_articles = Article.objects.filter(like_users=user)
    serializer = ArticleSerializer(liked_articles, many=True)
    return Response(serializer.data)

# 좋아요 수 반환
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_like_count(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    like_count = article.like_users.count()
    return Response({'like_count': like_count})
