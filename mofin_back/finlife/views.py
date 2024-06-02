import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from .serializers import DepositSerializer, DepositOptionsSerializer, SavingSerializer, SavingOptionsSerializer
from .models import Deposit, DepositOptions, Saving, SavingOptions
import logging
from accounts.models import User
from rest_framework.permissions import IsAuthenticated


logger = logging.getLogger(__name__)
API_KEY = settings.FIN_API_KEY

# 데이터 확인
def index(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return JsonResponse(response)

# 정기예금 상품 목록 및 옵션 목록 저장 
@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if Deposit.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        
        save_data = {
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_cd': fin_prdt_cd,
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_way': li.get('join_way'),
            'mtrt_cnd': li.get('mtrt_cnd'),
            'spcl_cnd': li.get('spcl_cnd'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'etc_note': li.get('etc_note'),
            'max_limit': li.get('max_limit')
        }

        serializer = DepositSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()
            options = response.get('result').get('optionList')
            for option in options:
                if option.get('fin_prdt_cd') == fin_prdt_cd:
                    option_data = {
                        # 'deposit': product.id,
                        'fin_prdt_cd': option.get('fin_prdt_cd'),
                        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                        'intr_rate': option.get('intr_rate'),
                        'intr_rate2': option.get('intr_rate2'),
                        'save_trm': option.get('save_trm'),
                    }
                    option_serializer = DepositOptionsSerializer(data=option_data)
                    if option_serializer.is_valid(raise_exception=True):
                        option_serializer.save(deposit=product)

    return JsonResponse({"message": "okay"})

# 정기적금 상품 목록 및 옵션 목록 저장 
@api_view(['GET'])
def save_saving_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if Saving.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        
        save_data = {
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_cd': fin_prdt_cd,
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_way': li.get('join_way'),
            'mtrt_cnd': li.get('mtrt_cnd'),
            'spcl_cnd': li.get('spcl_cnd'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'etc_note': li.get('etc_note'),
            'max_limit': li.get('max_limit')
        }

        serializer = SavingSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()
            options = response.get('result').get('optionList')
            for option in options:
                if option.get('fin_prdt_cd') == fin_prdt_cd:
                    option_data = {
                        # 'saving': product.id,
                        'fin_prdt_cd': option.get('fin_prdt_cd'),
                        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                        'intr_rate': option.get('intr_rate'),
                        'intr_rate2': option.get('intr_rate2'),
                        'save_trm': option.get('save_trm'),
                    }
                    option_serializer = SavingOptionsSerializer(data=option_data)
                    if option_serializer.is_valid(raise_exception=True):
                        option_serializer.save(saving=product)

    return JsonResponse({"message": "okay"})

# 정기예금 상품 목록 출력 및 특정 조건에 따른 필터링
@api_view(['GET'])
def deposit_products(request):
    bank_name = request.GET.get('bank_name', None)
    save_trm = request.GET.get('save_trm', None)
    logger.debug(f"Received bank_name: {bank_name}, save_trm: {save_trm}")
    try:
        products = Deposit.objects.all()

        if bank_name:
            products = products.filter(kor_co_nm=bank_name)
        
        if save_trm:
            products = products.filter(depositoptions__save_trm=save_trm)
        
        serializer = DepositSerializer(products.distinct(), many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching deposit products: {e}")
        return Response({"error": str(e)}, status=500)

# 특정 예금 상품의 옵션 리스트 출력
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    deposit_products_options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_products_options, many=True)
    return Response(serializer.data)

# 정기적금 상품 목록 출력 및 특정 조건에 따른 필터링
@api_view(['GET'])
def saving_products(request):
    bank_name = request.GET.get('bank_name', None)
    save_trm = request.GET.get('save_trm', None)
    logger.debug(f"Received bank_name: {bank_name}, save_trm: {save_trm}")
    try:
        products = Saving.objects.all()

        if bank_name:
            products = products.filter(kor_co_nm=bank_name)
        
        if save_trm:
            products = products.filter(savingoptions__save_trm=save_trm)
        
        serializer = SavingSerializer(products.distinct(), many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching saving products: {e}")
        return Response({"error": str(e)}, status=500)

# 특정 적금 상품의 옵션 리스트 출력
@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    saving_products_options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(saving_products_options, many=True)
    return Response(serializer.data)

from django.db.models import Q
from collections import Counter

# 추천 알고리즘
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_products(request):
    age = request.user.age
    money = request.user.money
    salary = request.user.salary
    age_scope = 5
    money_scope = 10000000
    salary_scope = 150000000

    correct_users = User.objects.filter(
        Q(age__range=(age - age_scope, age + age_scope)) &
        Q(money__range=(money - money_scope, money + money_scope)) &
        Q(salary__range=(salary - salary_scope, salary + salary_scope)) &
        ~Q(id=request.user.id)  # 나 자신을 제외
    )

    # 가입한 상품 목록 리스트로 변환
    product_lists = correct_users.values_list('financial_products', flat=True)
    
    # 상품 목록을 하나의 리스트로 통합
    all_products = []
    for product_list in product_lists:
        if product_list:
            all_products.extend(product_list.split(','))

    # 상품별 가입자 수를 계산
    product_counter = Counter(all_products)

    # 가장 많이 가입한 상품 상위 5개 반환
    most_common_products = product_counter.most_common(5)
    # 제품 ID만 추출하여 리스트 생성
    product_ids = [product for product, count in most_common_products]

    return Response({
        # 'most_common_products': most_common_products
        'most_common_products': product_ids
        
    })

