<template>
  <div class="d-flex justify-content-center mt-5 ma-bt">
    <div class="container p-4 mx-2 rounded shadow-sm flex-grow-1" style="max-width: 600px;">
      <h2 class="text-center mb-4">
        <span class="material-symbols-outlined">
          currency_exchange
        </span>
        환율 계산기
        <span class="material-symbols-outlined">
          currency_exchange
        </span>
      </h2>
      <div class="mx-4">
        <div class="mb-3">
          <label for="amount" class="form-label">금액: </label>
          <input type="number" v-model="amount" id="amount" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="from_currency" class="form-label">기준 통화 선택: </label>
          <select v-model="temp_from_currency" id="from_currency" class="form-select" @change="updateToCurrencyOptions">
            <option v-for="exchange_val in exchange_vals" :value="exchange_val.CUR_UNIT">{{ exchange_val.CUR_NM }}({{ exchange_val.CUR_UNIT }})</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="to_currency" class="form-label">대상 통화 선택: </label>
          <select v-model="temp_to_currency" id="to_currency" class="form-select">
            <option v-for="exchange_val in exchange_vals" :value="exchange_val.CUR_UNIT">{{ exchange_val.CUR_NM }}({{ exchange_val.CUR_UNIT }})</option>
          </select>
        </div>
        <button @click="convertCurrency" class="btn btn-outline-warning w-100">계산하기</button>
        <div v-if="result !== null" class="mt-3">
          <p class="alert alert-warning">{{ result }} {{ to_currency }}</p>
        </div>
      </div>
    </div>
    <div class="container p-4 mx-2 rounded shadow-sm flex-grow-1 accordion" id="accordionExample" style=" max-width: 600px;">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            실시간 환율 정보 더보기
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <div v-for="exchange_val in exchange_vals" :key="exchange_val.CUR_UNIT" class="mb-1 p-2 border rounded">
              <p>{{ exchange_val.CUR_NM }}({{ exchange_val.CUR_UNIT }})</p>
              <p style="font-size: small;">매매 기준 환율 <span style="font-size: x-large;">{{ exchange_val.DEAL_BAS_R }}</span></p>
              
              <p style="font-size: small;">원화(1000원 기준) 환율 <span style="font-size: x-large;">{{ exchange_val.kor_to_cur }}</span></p>
              
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exchange_vals: [], // 데이터를 저장할 배열을 data 속성으로 추가
      loading: false,
      amount: 0,
      temp_from_currency: '',
      temp_to_currency: '',
      from_currency: '',
      to_currency: '',
      result: null
    };
  },
  mounted() {
    this.loading = true;
    // Django API에 GET 요청 보내기
    axios.get('http://127.0.0.1:8000/exchange/get_exchange_rates/')
      .then(res => {
        this.exchange_vals = res.data; // 데이터를 data 속성에 할당
        this.loading = false;
        console.log(this.exchange_vals); // 데이터가 잘 받아와졌는지 확인
      })
      .catch(error => {
        console.error('에러 발생:', error);
        this.loading = false;
      });
  },
  methods: {
    fetchExchangeRates() {
      this.loading = true;
      axios.get('http://127.0.0.1:8000/exchange/')
        .then(res => {
          this.exchange_vals = res.data;
          this.loading = false;
        })
        .catch(error => {
          console.error('에러 발생:', error);
          this.loading = false;
        });
    },
    updateToCurrencyOptions() {
      // 만약 기준 통화가 한국이면 모든 통화를 대상 통화로 선택할 수 있도록 설정
      if (this.temp_from_currency === 'KRW') {
        this.temp_to_currency_options = this.exchange_vals;
      } else {
        // 기준 통화가 한국이 아니면 대상 통화를 한국 원화로만 선택할 수 있도록 설정
        this.temp_to_currency_options = this.exchange_vals.filter(val => val.CUR_UNIT === 'KRW');
        // 선택된 통화가 대상 통화로 설정되어 있는지 확인하고, 대상 통화를 설정해주기
        if (!this.temp_to_currency_options.find(val => val.CUR_UNIT === this.temp_to_currency)) {
          this.temp_to_currency = 'KRW';
        }
      }
    },
    convertCurrency() {
      // 선택된 임시 통화 값을 실제 변환에 사용할 통화 값으로 설정
      this.from_currency = this.temp_from_currency;
      this.to_currency = this.temp_to_currency;

      const fromExchange = this.exchange_vals.find(val => val.CUR_UNIT === this.from_currency);
      const toExchange = this.exchange_vals.find(val => val.CUR_UNIT === this.to_currency);

      if (!fromExchange || !toExchange || this.amount <= 0) {
        this.result = null;
        return;
      }

      let fromRate = parseFloat(fromExchange.DEAL_BAS_R.replace(/,/g, ''));
      let toRate = parseFloat(toExchange.DEAL_BAS_R.replace(/,/g, ''));

      // JPY와 IDR의 환율은 100 단위로 제공되므로, 이를 반영합니다.
      if (this.from_currency === 'JPY(100)' || this.from_currency === 'IDR(100)') {
        fromRate /= 100;
      }
      if (this.to_currency === 'JPY(100)' || this.to_currency === 'IDR(100)') {
        toRate /= 100;
      }

      // 기준 통화를 원화로 변환한 다음, 대상 통화로 변환합니다.
      const amountInKRW = this.amount * fromRate;
      const convertedAmount = amountInKRW / toRate;

      this.result = convertedAmount.toFixed(2);
    }
  }
};
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  background-color: rgba(255, 255, 224, 0.8);
}

.d-flex {
  display: flex;
}

.flex-grow-1 {
  flex-grow: 1;
}

.mx-2 {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}

.ma-bt {
  margin-bottom:100px;
}

</style>

