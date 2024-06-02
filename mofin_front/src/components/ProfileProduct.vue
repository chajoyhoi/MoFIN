<template>
  <div>
    <div>
      <br>
      <h3>가입 상품</h3>
      <br>
      <div v-if="products.length" class="product-container">
        <div v-for="product in products" :key="product.product.fin_prdt_cd" class="product-card">
          <div class="card p-2">
            <div class="card-body">
              <h4 class="card-title">{{ product.product.fin_prdt_nm }}</h4>
              <p class="card-text">금융 회사명: {{ product.product.kor_co_nm }}</p>
              <p class="card-text">금리 유형: {{ product.options.intr_rate_type_nm }}</p>
              <p class="card-text">저축 금리: {{ product.options.intr_rate }}%</p>
              <p class="card-text">최고 우대 금리: {{ product.options.intr_rate2 }}%</p>
              <p class="card-text">저축 기간: {{ product.options.save_trm }}개월</p>
              <button @click="cancelPurchase(product.product.fin_prdt_cd, product.options.save_trm)" class="btn btn-pastel-red">구매 취소</button>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        가입 상품이 없습니다.
      </div>
      <br>
      
    </div>

    <div v-if="products.length">
      <br>
      <hr>
      <h3 class="mt-5">가입한 상품 금리</h3>
      <br>
      <div class="chart-container">
        <canvas id="interestRateChart"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';
import { useAccountsStore } from '@/stores/accounts';
import { Chart } from 'chart.js/auto';

const profilestore = useAccountsStore();
const products = ref([]);
let chartInstance = null;

const fetchProducts = () => {
  axios.get('http://127.0.0.1:8000/accounts/profile/get_added_product/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    products.value = response.data;
    nextTick(() => {
      if (products.value.length > 0) {
        renderChart();
      } else if (chartInstance) {
        chartInstance.destroy();
        chartInstance = null;
      }
    });
  })
  .catch(error => {
    console.error('관심 상품을 가져오는 중 에러 발생:', error);
  });
};

const cancelPurchase = (product_cd, option_trm) => {
  const elem = `${product_cd}/${option_trm}`;
  axios.post(`http://127.0.0.1:8000/accounts/profile/add_product/${elem}`, {}, {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    console.log(response.data);
    alert('구매가 취소되었습니다.');
    fetchProducts();
  })
  .catch(error => {
    console.error(error);
  });
};

const renderChart = () => {
  const ctx = document.getElementById('interestRateChart').getContext('2d');
  const labels = products.value.map(product => product.product.fin_prdt_nm);
  const intrRates = products.value.map(product => product.options.intr_rate);
  const intrRates2 = products.value.map(product => product.options.intr_rate2);

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: '저축 금리 (%)',
          data: intrRates,
          backgroundColor: 'rgba(255, 205, 86, 0.2)',
          borderColor: 'rgba(255, 205, 86, 1)',
          borderWidth: 1
        },
        {
          label: '최고 우대 금리 (%)',
          data: intrRates2,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

onMounted(() => {
  fetchProducts();
});
</script>

<style scoped>
.product-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: flex-start;
}

.product-card {
  flex: 1 1 calc(33.33% - 1rem); 
  max-width: calc(33.33% - 1rem);
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.card {
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  min-height: 350px; 
}

.card-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.chart-container {
  width: 80%;
  height: 400px;
  margin: 0 auto;
}

.btn-pastel-red {
  background-color: #f4cccc;
  color: #333;
  border: none;
}
</style>
