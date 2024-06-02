from django.db import models

class Deposit(models.Model):
    # 공시 제출월
    dcls_month = models.CharField(max_length=6)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField(unique=True)
    # 금융 상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입 방법
    join_way = models.TextField(null=True)
    # 만기 후 이자율 
    mtrt_cnd = models.TextField(null=True)
    # 우대 조건 
    spcl_cnd = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입 대상
    join_member = models.TextField(null=True)
    # 금융 상품 설명 
    etc_note = models.TextField(null=True)
    # 최고한도 
    max_limit = models.IntegerField(null=True)

class DepositOptions(models.Model):
    # 외래키
    deposit = models.ForeignKey(Deposit, on_delete = models.CASCADE)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField(null=True)
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 단위
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고 우대 금리
    intr_rate2 = models.FloatField(null=True)

class Saving(models.Model):
    # 공시 제출월
    dcls_month = models.CharField(max_length=6)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField(unique=True)
    # 금융 상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입 방법
    join_way = models.TextField(null=True)
    # 만기 후 이자율 
    mtrt_cnd = models.TextField(null=True)
    # 우대 조건 
    spcl_cnd = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입 대상
    join_member = models.TextField(null=True)
    # 금융 상품 설명 
    etc_note = models.TextField(null=True)
    # 최고한도 
    max_limit = models.IntegerField(null=True)

class SavingOptions(models.Model):
    # 외래키
    saving = models.ForeignKey(Saving, on_delete = models.CASCADE)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField(null=True)
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 단위
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고 우대 금리
    intr_rate2 = models.FloatField(null=True)