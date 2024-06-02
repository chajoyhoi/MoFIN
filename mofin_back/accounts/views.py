from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
# from dj_rest_auth.views import UserDetailsView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from .serializers import ProfileSerializer, UserInfoserializer, CustomRegisterSerializer
from finlife.models import Deposit, DepositOptions, Saving, SavingOptions  # 모델 import
from finlife.serializers import DepositOptions, DepositOptionsSerializer, Deposit, DepositSerializer, SavingOptions, Saving, SavingOptionsSerializer, SavingSerializer

# 회원정보조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


User = get_user_model()

#회원정보수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request):
    user = request.user
    serializer = UserInfoserializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 회원 탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    request.user.delete()
    return Response({'delete': '탈퇴가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


# 장바구니 버튼 클릭
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request, product_cd, option_trm):
    user = request.user
    
    if not user.financial_products:
        products = []
    else:
        products = user.financial_products.split(',')

    elem = f'{product_cd}/{option_trm}'

    if elem in products:
        products.remove(elem)
    else:
        products.append(elem)
    
    user.financial_products = ','.join(products)

    user.save()
    return Response({'message': 'Product added to favorites'}, status=status.HTTP_201_CREATED)

# 장바구니 상품 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_added_product(request):
    user = request.user

    if not user.financial_products:
        products = []
    else:
        products = user.financial_products.split(',')

    product_details = []

    for product in products:
        product_cd, option_trm = product.split('/')
        try:
            deposit_product = Deposit.objects.get(fin_prdt_cd=product_cd)
            deposit_options = DepositOptions.objects.filter(deposit=deposit_product, save_trm=option_trm)
            
            if deposit_options.exists():
                deposit_option = deposit_options.first()
                product_data = {
                    'product': DepositSerializer(deposit_product).data,
                    'options': DepositOptionsSerializer(deposit_option).data,
                }
                product_details.append(product_data)
        except Deposit.DoesNotExist:
            # 적금 상품 
            try:
                saving_product = Saving.objects.get(fin_prdt_cd=product_cd)
                saving_options = SavingOptions.objects.filter(saving=saving_product, save_trm=option_trm)
                
                if saving_options.exists():
                    saving_option = saving_options.first()
                    product_data = {
                        'product': SavingSerializer(saving_product).data,
                        'options': SavingOptionsSerializer(saving_option).data,
                    }
                    product_details.append(product_data)
            except (Saving.DoesNotExist, SavingOptions.DoesNotExist):
                continue

    return Response(product_details, status=status.HTTP_200_OK)
