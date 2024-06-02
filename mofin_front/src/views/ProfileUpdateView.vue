<template>
  <main class="root">
    <div class="signup-wrapper form active mt-5">
      <div class="form-wrapper">
        <h4 class="mb-5">회원정보 수정</h4>
        <form @submit.prevent="updateProfile">
          <div class="form-group">
            <label class="form-label">이메일</label>
            <input type="text" v-model="email" class="form-field input-field"/>
          </div>
          <div class="form-group">
            <label class="form-label">닉네임</label>
            <input type="text" v-model="nickname" class="form-field input-field"/>
          </div>
          <div class="form-group">
            <label class="form-label">나이</label>
            <input type="number" v-model="age" class="form-field input-field"/>
          </div>
          <div class="form-group">
            <label class="form-label">자산</label>
            <input type="number" v-model="money" class="form-field input-field"/>
          </div>
          <div class="form-group">
            <label class="form-label">연봉</label>
            <input type="number" v-model="salary" class="form-field input-field"/>
          </div>
          <button type="submit" class="button primary" :disabled="loading">수정하기</button>
          <button type="button" class="button secondary" @click="goBack">뒤로가기</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useAccountsStore } from "@/stores/accounts";
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useAccountsStore();

const nickname = ref(null);
const email = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const loading = ref(false);

const updateProfile = function () {
  loading.value = true;
  const payload = {
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    salary: salary.value,
    money: money.value,
  };

  store.updateProfile(payload).then(() => {
    loading.value = false;
    router.go(-1); // 프로필 업데이트 후 이전 페이지로 이동
  }).catch((err) => {
    console.error('프로필 업데이트 중 오류 발생', err);
    loading.value = false;
  });
};

onMounted(() => {
  email.value = store.userdata.email;
  nickname.value = store.userdata.nickname;
  age.value = store.userdata.age;
  money.value = store.userdata.money;
  salary.value = store.userdata.salary;
});

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
};
</script>

<style scoped>
.root {
  color: #ffc400;
  display: flex;
  width: 100%;
  height: 100%;
}

.signup-wrapper {
  flex-grow: 1;
  background-color: white;
  transition: all 0.32s ease-in-out;
  display: flex;
  justify-content: center;
  align-items: center;
}

.form-wrapper {
  background:rgba(255, 255, 224, 0.8); 
  width: 400px;
  height: auto;
  padding: 60px 20px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h4 {
  color: #212121;
  font-size: 25px;
  font-weight: bold;
  margin: 15px 0 30px 0;
}

.form-group {
  font-weight: bold;
  width: 100%;
  margin: 0 auto 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-label {
  margin-bottom: 5px;
}

.input-field {
  width: 230px;
  height: 35px;
  padding: 6px 15px;
  border-radius: 5px;
  outline: none;
  border: none;
  font-size: 14px;
}

.button {
  cursor: pointer;
  font-weight: bold;
  width: 230px;
  margin: 10px auto;
  height: 45px;
  padding: 6px 15px;
  border-radius: 5px;
  outline: none;
  border: none;
  font-size: 14px;
}

.button.primary {
  color: white;
  background: #ffd13b; 
}

.button.primary:hover {
  opacity: 0.9;
}

.button.secondary {
  background: white;
  color: #FFC107; 
}

.button.secondary:hover {
  background: #FFF8E1; 
}
</style>
