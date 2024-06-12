from django.db import models

class Exchange(models.Model):
    # 통화 코드
    CUR_UNIT = models.CharField(max_length=100)
    # 국가/통화명
    CUR_NM = models.CharField(max_length=100)
    # 전신환(송금) 받으실 때
    TTB = models.CharField(max_length=100)
    # 전신환(송금) 보내실 때
    TTS = models.CharField(max_length=100)
    # 매매 기준율
    DEAL_BAS_R = models.CharField(max_length=100)
    # 장부가격 
    BKPR = models.CharField(max_length=100)
    # 년환가료율
    YY_EFEE_R = models.CharField(max_length=100)
    # 10일환가료율
    TEN_DD_EFEE_R = models.CharField(max_length=100)
    # 한국 원(KRW)으로부터 해당 통화로 변환하는 값을 저장하는 필드
    kor_to_cur = models.FloatField()