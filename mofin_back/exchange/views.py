import requests
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Exchange
from .serializers import ExchangeSerializer
import pandas as pd 

API_KEY = settings.EXCHANGE_API_KEY

# 추후 수정필요
@api_view(['GET'])
def index(request):
    Exchange.objects.all().delete()

    # if Exchange.objects.exists():
    #     return Response("Exchange data already exists in the database.")
     
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01' # searchdate를 입력하지 않으면 당일 날짜 출력 
    response = requests.get(url)
    exchange_data = response.json()
    # return Response(exchange_data)
    
    for data in exchange_data:
        currency = data['cur_unit']
        buy_rate = float(data['deal_bas_r'].replace(',', '')) 
        sell_rate = float(data['bkpr'].replace(',', ''))  

        
        if currency == 'JPY(100)' or currency == 'IDR(100)':
            kor_to_cur = 1000 / float(buy_rate)  # 100으로 나누기
        else:
            kor_to_cur = 1000 / float(buy_rate)

        # Exchange 모델 인스턴스 생성
        exchange_instance = Exchange(
            CUR_UNIT=currency,
            CUR_NM=data['cur_nm'],
            TTB=data['ttb'],
            TTS=data['tts'],
            DEAL_BAS_R=data['deal_bas_r'],
            BKPR=data['bkpr'],
            YY_EFEE_R=data['yy_efee_r'],
            TEN_DD_EFEE_R=data['ten_dd_efee_r'],
            kor_to_cur=round(kor_to_cur, 2)  # kor_to_cur 값 추가
        )
        # 데이터베이스에 저장
        exchange_instance.save()

    # 수정된 환율 데이터 응답
    return Response("Exchange data saved successfully!")

# 데이터 확인
@api_view(['GET'])
def get_exchange_rates(request):
    if request.method == 'GET':
        exchanges = Exchange.objects.all()
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data)

