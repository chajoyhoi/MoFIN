<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">예금 상품 목록</h1>
    <button @click="goBack" class="btn btn-back mb-4">뒤로가기</button>

    <div class="d-flex mb-4">
      <select v-model="selectedBank" @change="fetchDepositProducts" class="form-select me-3 flex-grow-1">
        <option value="">All Banks</option>
        <option v-for="bank in banks" :key="bank" :value="bank">{{ formatBankName(bank) }}</option>
      </select>

      <select v-model="selectedTerm" @change="fetchDepositProducts" class="form-select flex-grow-1">
        <option value="">All Terms</option>
        <option v-for="term in terms" :key="term" :value="term">{{ term }}개월</option>
      </select>
    </div>

    <div class="row">
      <div class="col-md-4 mb-4" v-for="deposit in depositstore.deposit_products" :key="deposit.fin_prdt_cd">
        <DepositListItem :deposit="deposit"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import DepositListItem from "@/components/DepositListItem.vue";
import { ref, onMounted } from "vue";
import { useFinanceStore } from "../stores/finance";
import { useRouter } from "vue-router";

const router = useRouter();
const depositstore = useFinanceStore();

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
};

const selectedBank = ref("");
const banks = ref([
  '경남은행',
  '광주은행',
  '국민은행',
  '농협은행주식회사',
  '대구은행',
  '부산은행',
  '부산은행',
  '수협은행',
  '신한은행',
  '우리은행',
  '전북은행',
  '제주은행',
  '주식회사 카카오뱅크',
  '주식회사 케이뱅크',
  '중소기업은행',
  '토스뱅크 주식회사',
  '하나은행',
  '한국산업은행',
  '한국스탠다드차타드은행',
]);

const selectedTerm = ref("");
const terms = ref([1, 3, 6, 12, 24, 36]);

const fetchDepositProducts = () => {
  const params = {};
  if (selectedBank.value) {
    params.bank_name = selectedBank.value;
  }
  if (selectedTerm.value) {
    params.save_trm = selectedTerm.value;
  }
  depositstore.getDeposit(params);
};

onMounted(() => {
  depositstore.getDeposit();
  fetchDepositProducts();
});

const formatBankName = (name) => {
  return name.replace(/주식회사\s*/g, '').replace(/\s*주식회사/g, '');
};
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}
.row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: flex-start;
  margin-left: 60px;
}
.col-md-4 {
  flex: 1 0 30%; 
  max-width: 30%;
}
.select-group {
  display: flex;
  justify-content: space-between;
}
select.form-select {
  flex: 1;
  margin-right: 1rem;
}
select.form-select:last-child {
  margin-right: 0;
}
.btn-back {
  background-color: #f8f9fa;
  border: 1px solid #ced4da;
  color: #000;
  transition: background-color 0.3s, color 0.3s;
}
.btn-back:hover {
  background-color: #e9ecef;
}
</style>
