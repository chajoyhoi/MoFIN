<template>
  <div>
    <div class="container mt-5">
      <h1 class="text-center mb-4">예금 상품 상세 페이지</h1>
      <button @click="goBack" class="btn btn-outline-light-gray mb-4">뒤로가기</button>
      <div class="card p-2">
        <div class="card-body">
          <p class="card-text highlight-text text-start mx-3 mt-3">{{ product.kor_co_nm }}</p>
          <h2 class="card-title mb-3 mx-4 mt-1"><strong>{{ product.fin_prdt_nm }}</strong></h2>
          <div v-if="product" class="mx-4">
            <p><strong>금융 코드:</strong> {{ product.fin_prdt_cd }}</p>
            <p><strong>금융 상품 설명:</strong> {{ product.etc_note }}</p>
            <p v-if="product.join_deny === 1"><strong>가입 제한:</strong> 제한없음</p>
            <p v-if="product.join_deny === 2"><strong>가입 제한:</strong> 서민전용</p>
            <p v-if="product.join_deny === 3"><strong>가입 제한:</strong> 일부제한</p>
            <p><strong>가입 대상:</strong> {{ product.join_member }}</p>
            <p><strong>가입 방법:</strong> {{ product.join_way }}</p>
            <p><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="depositOptions" class="container mt-4">
      <h3 class="card-title mt-5 text-center">상품 옵션</h3>
      <div class="row row-cols-1 row-cols-md-3">
        <div class="col mb-2" v-for="depositOption in depositOptions" :key="depositOption.id">
          <DepositOptionListItem 
            :depositOption="depositOption"
            @toggle-product="toggleProduct"
            class="h-100"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useFinanceStore } from "@/stores/finance";
import { useAccountsStore } from '@/stores/accounts';

import DepositOptionListItem from '@/components/DepositOptionListItem.vue'

const finStore = useFinanceStore();
const accountsstore = useAccountsStore()

const router = useRouter();
const route = useRoute();
const depositOptions = ref(null);

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
};

const toggleProduct = (product_cd) => {
  const token = accountsstore.token;
  axios({
    method: 'post',
    url: `${finStore.API_URL}/accounts/profile/add_product/${product_cd}/`,
    headers: {
      Authorization: `Token ${token}`
    },
  })
    .then((response) => {
      console.log(response.data)
      accountsstore.getUserdata()
    })
    .catch((error) => {
      console.log(error)
    })
}

const productCd = route.params.id;
const product = computed(() => {
  return finStore.deposit_products?.filter(
    (product) => product.fin_prdt_cd === productCd
  )[0];
});

axios({
    method: "get",
    url: `${finStore.API_URL}/finlife/deposit-products-options/${productCd}/`,
  })
    .then((res) => {
      depositOptions.value = res.data;
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err);
    });
    
onMounted(() => {
  accountsstore.getUserdata();
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}
.card {
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
}
.card-title {
  margin-bottom: 20px;
}
.btn-outline-light-gray {
  background-color: #f8f9fa;
  border: 1px solid #ced4da;
  color: #000;
  transition: background-color 0.3s, color 0.3s;
}
.btn-outline-light-gray:hover {
  background-color: #e9ecef;
}

.highlight-text {
  display: inline-block;
  background-color: #ffe4da; 
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
  color: #856404;
}
.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}
.col {
  display: flex;
  flex-direction: column;
}
</style>