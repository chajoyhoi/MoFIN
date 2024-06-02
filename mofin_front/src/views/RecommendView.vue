<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4 pt-4">
      <span class="material-symbols-outlined" >featured_seasonal_and_gifts</span>
      금융 상품 추천받기
      
    </h2>
    <h4 class="text-center mb-4 pb-3">나와 비슷한 사람들이 많이 가입한 상품 ( 나이, 자산, 연봉 )</h4>

    <div v-if="recommendstore.recommendedProducts.length" class="row justify-content-center">
      <div class="col-md-4 mb-4" v-for="product in recommendstore.recommendedProducts" :key="product.fin_prdt_cd">
        <div class="card deposit-card h-100">
          <div class="card-body my-3">
            <p class="card-text highlight-text mx-4 text-center">{{ product.kor_co_nm }}</p>
            <h2 class="card-title px-3">{{ product.fin_prdt_nm }}</h2>
            <p class="card-text px-3">FIN Code<br>{{ product.fin_prdt_cd }}</p>
            <p class="card-text px-3">{{ product.spcl_cnd }}</p>
            <a :href="getProductLink(product.fin_prdt_cd)" class="btn btn-pastel-yellow">추천상품 상세보기</a>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="text-center">
      <p> {{ accountsstore.userdata.name }}님과 적합한 상품을 찾을 수 없습니다.</p>
      <p> 다른 예적금 상품을 보는 것은 어떠신가요?</p>
      <RouterLink :to="{name:'finance'}" class="btn btn-pastel-yellow">더 많은 예적금 상품 보러가기</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRecommendStore } from '@/stores/recommend';
import { useAccountsStore } from '@/stores/accounts';
import { useFinanceStore } from "@/stores/finance";
import { useRouter, useRoute } from "vue-router";

const recommendstore = useRecommendStore();
const fistore = useFinanceStore();
const accountsstore = useAccountsStore();

const router = useRouter();
const route = useRoute();

onMounted(() => {
  recommendstore.recommendAuto(accountsstore.token);
});

const productCd = route.params.id;
const product = computed(() => {
  return fistore.deposit_products?.filter(
    (product) => product.fin_prdt_cd === productCd
  )[0];
});

// 금융 상품 코드에 따라 가입 링크를 생성하는 함수
const getProductLink = (productCode) => {
  // 예금 상품인지 적금 상품인지 확인
  const isDeposit = fistore.deposit_products.some(
    (product) => product.fin_prdt_cd === productCode
  );
  if (isDeposit) {
    return `http://localhost:5173/deposit/detail/${productCode}`;
  } else {
    return `http://localhost:5173/saving/detail/${productCode}`;
  }
};
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: rgba(255, 255, 224, 0.8);
}
.row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center; /* 가운데 정렬 */
}
.col-md-4 {
  flex: 1 0 30%; 
  max-width: 30%;
}
.card.deposit-card {
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  height: 100%;
}
.card-title {
  margin-bottom: 20px;
}
.card-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.highlight-text {
  background-color: #ffe4da; 
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
  color: #856404;
}
.btn-pastel-yellow {
  background-color: #ffeece;
  border: none;
  color: #000;
  transition: background-color 0.3s, color 0.3s;
  display: inline-block;
  margin-top: 10px;
}
.btn-pastel-yellow:hover {
  background-color: #ffe8ca; 
}
.text-center {
  text-align: center;
}
</style>
