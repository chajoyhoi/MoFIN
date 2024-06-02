<template>
  <div class="card option-item mx-2 my-4">
    <div class="card-body d-flex flex-column align-items-center">
      <!-- <h5 class="card-title">적금 상품 옵션 정보</h5> -->
      <p class="card-text px-2 pt-3">유형: {{ savingOption.intr_rate_type_nm }}</p>
      <p class="card-text px-2">저축 단위: {{ savingOption.save_trm }} 개월</p>
      <p class="card-text px-2">저축금리: {{ savingOption.intr_rate }} %</p>
      <p class="card-text px-2">최고 우대 금리: {{ savingOption.intr_rate2 }} %</p>
      <button v-if="accountsstore.isLogin" @click="addOrCancelProduct(savingOption.fin_prdt_cd, savingOption.save_trm)" class="btn btn-pastel-yellow mt-auto mb-3">
        {{ isProductAdded(savingOption.fin_prdt_cd, savingOption.save_trm) ? '가입 취소 하기' : '가입하기' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useFinanceStore } from '@/stores/finance';
import { useAccountsStore } from '@/stores/accounts';

const router = useRouter();
const financestore = useFinanceStore()
const accountsstore = useAccountsStore()

const props = defineProps({
  savingOption: {
    type: Object,
    required: true
  }
});

const isProductAdded = (product_cd, option_trm) => {
  const products = accountsstore.userdata?.financial_products || [];
  const elem = `${product_cd}/${option_trm}`;
  return products.includes(elem);
};

const addOrCancelProduct = (product_cd, option_trm) => {
  const elem = `${product_cd}/${option_trm}`;
  if (isProductAdded(product_cd, option_trm)) {
    cancelProduct(elem);
  } else {
    addProduct(product_cd, option_trm);
  }
};

const addProduct = (product_cd, option_trm) => {
  axios.post(`${financestore.API_URL}/accounts/profile/add_product/${product_cd}/${option_trm}`, {}, {
    headers: {
      Authorization: `Token ${accountsstore.token}`
    }
  })
  .then(response => {
    console.log(response.data);
    accountsstore.getUserdata();
    alert('가입이 완료되었습니다!');
    const confirmNavigation = confirm('프로필로 이동하시겠습니까?');
    if (confirmNavigation) {
      navigateToProfile();
    }
  })
  .catch(error => {
    console.error(error);
  });
};

const cancelProduct = (elem) => {
  axios.post(`${financestore.API_URL}/accounts/profile/add_product/${elem}`, {}, {
    headers: {
      Authorization: `Token ${accountsstore.token}`
    }
  })
  .then(response => {
    console.log(response.data);
    accountsstore.getUserdata();
    alert('가입이 취소되었습니다.');
  })
  .catch(error => {
    console.error(error);
  });
};

const navigateToProfile = () => {
  router.push({ name: 'profile' });
};
</script>

<style scoped>
.option-item {
  margin-bottom: 1rem;
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
}
.btn-pastel-yellow {
  background-color: #ffeece;
  border: none;
  color: #000;
  transition: background-color 0.3s, color 0.3s;
}
.btn-pastel-yellow:hover {
  background-color: #ffe8ca; 
}
</style>
