<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">
      <span class="material-symbols-outlined">
        savings
      </span>
      예금 · 적금 정보보기
    </h2>

      <!-- 예금 카드 -->
      <div class="mb-5">
        <div class="card h-100 p-3">
          <div class="card-body ca">
            <h4 class="card-title mb-4">
              <span class="material-symbols-outlined">
              payments
              </span>
              예금
            </h4>
            <p class="card-text mb-4">예금은 일정 금액을 일정 기간 동안 금융기관에 맡기고 이자를 받는 금융상품입니다. 안정적인 수익을 추구하는 분들에게 적합합니다.</p>
            <RouterLink :to="{ name: 'deposit' }" class="btn btn-pastel-yellow text-dark">예금 상품 보기</RouterLink>
          </div>
        </div>
      </div>
      <!-- 적금 카드 -->
      <div class="mb-5">
        <div class="card h-100 p-3">
          <div class="card-body">
            <h4 class="card-title mb-4">
              <span class="material-symbols-outlined">
              account_balance_wallet
              </span>
              적금
            </h4>
            <p class="card-text  mb-4">적금은 일정 금액을 매달 정기적으로 금융기관에 납입하고, 만기 시 원금과 이자를 받는 금융상품입니다. 꾸준히 저축하는 습관을 기르기에 좋습니다.</p>
            <RouterLink :to="{ name: 'saving' }" class="btn btn-pastel-orange text-dark">적금 상품 보기</RouterLink>
          </div>
        </div>
      </div>

  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';
</script>

<style scoped>
.btn-pastel-yellow {
  background-color: #fcf7ca; 
  border: none;
  transition: background-color 0.3s;
}
.btn-pastel-yellow:hover {
  background-color: #FFF9E3; 
}
.btn-pastel-orange {
  background-color: #ffd1c9; 
  border: none;
  transition: background-color 0.3s;
}
.btn-pastel-orange:hover {
  background-color: #ffeee3; 
}

.container {
  background: rgba(255, 255, 255, 0.8);
  padding: 50px 100px 100px 100px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  background-color: rgba(255, 255, 224, 0.8);
}

.card {
  border: none; /* 테두리 선 제거 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 설정 */
}

/* 추가적인 스타일 */
.card-body {
  padding: 20px; /* 내부 여백 추가 */
  border-radius: 10px; /* 카드의 모서리를 둥글게 만듦 */
  background-color: rgba(255, 255, 255, 0.8); /* 카드 내부 배경색 */
}
</style>
