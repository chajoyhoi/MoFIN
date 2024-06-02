import { ref, computed, onMounted, watch } from "vue";
import { defineStore } from "pinia";
import axios from "axios";


export const useFinanceStore = defineStore("finance", () => {
  const API_URL = "http://127.0.0.1:8000";
  // =========================== 예금 =============================
  // 금융 데이터를 저장
  const deposit_products = ref([]);
  const depositProductOptions = ref([])

  // 금융 데이터 저장 
  const saveDeposit = () => {
    axios({
      method: "get",
      url: `${API_URL}/finlife/save-deposit-products/`,
    })
      .then((res) => {
        // console.log(res.data);
        console.log('정기예금 상품 목록 DB 저장')
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // // 금융 데이터 조회
  const getDeposit = (params = {}) => {
    axios({
      method: "get",
      url: `${API_URL}/finlife/deposit-products/`,
      params: params,
    })
      .then((res) => {
        // console.log(res)
        deposit_products.value = res.data;
        // console.log(deposit_products.value)
        console.log('예금 데이터 조회')
      })
      .catch((err) => {
        console.log(err);
      });
  };


  // =========================== 적금 =============================
  const saving_products = ref([]);
  const savingProductOptions = ref([])

  // 금융 데이터 저장 
  const saveSaving = () => {
    axios({
      method: "get",
      url: `${API_URL}/finlife/save-saving-products/`,
    })
      .then((res) => {
        console.log(res.data);
        console.log('정기적금 상품 목록 DB 저장')
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // // 금융 데이터 조회
  const getSaving = (params = {}) => {
    axios({
      method: "get",
      url: `${API_URL}/finlife/saving-products/`,
      params: params,
    })
      .then((res) => {
        // console.log(res)
        saving_products.value = res.data;
        console.log(saving_products.value)
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const signUpDeposit = (payload) => {
    axios({
      method: "post",
      url: `${API_URL}/finlife/user-deposits/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: payload,
    })
      .then((res) => {
        console.log('예금 가입 성공', res.data);
        getDeposit(); // 가입 후 예금 목록 갱신
      })
      .catch((err) => {
        console.log('예금 가입 실패', err);
      });
  };


  return {
    API_URL,
    depositProductOptions,
    deposit_products,
    savingProductOptions,
    saving_products,
    saveDeposit,
    getDeposit,
    saveSaving,
    getSaving,
    signUpDeposit,
  };
}, { persist: true });