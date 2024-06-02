<template>
  <div class="card deposit-card mb-4" v-if="deposit">
    <div class="card-body my-3">
      <p class="card-text highlight-text mx-4 text-center">{{ deposit.kor_co_nm }}</p>
      <h2 class="card-title px-3">{{ deposit.fin_prdt_nm }}</h2>
      <p class="card-text px-3">금융 상품명: {{ deposit.fin_prdt_nm }}</p>
      <p class="card-text px-3">{{ deposit.etc_note }}</p>
      <div v-if="deposit.options && deposit.options.length">
        <h3>가입 기간 정보:</h3>
        <ul>
          <li v-for="option in deposit.options" :key="option.id">
            가입 기간: {{ option.save_trm }}개월, 기본 금리: {{ option.intr_rate }}%, 우대 금리: {{ option.intr_rate2 }}%
          </li>
        </ul>
      </div>
      <button @click="goToDetailPage" class="btn btn-pastel-yellow">정기예금 상세보기</button>
    </div>
  </div>
  <div v-else>
    <p>데이터를 불러오는 중...</p>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
export default {
  name: 'DepositListItem',
  props: {
    deposit: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const router = useRouter();

    const goToDetailPage = () => {
      router.push({ name: 'DepositDetail', params: { id: props.deposit.fin_prdt_cd }});
    };

    return {
      goToDetailPage
    };
  }
};
</script>

<style scoped>
.card.deposit-card {
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
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
}
.btn-pastel-yellow:hover {
  background-color: #ffe8ca; 
}
</style>
