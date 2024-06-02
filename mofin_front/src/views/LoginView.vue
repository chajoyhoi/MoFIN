<template>
  <main class="root">
    <div class="signup-wrapper form active mt-5">
      <div class="form-wrapper">
        <h4 class="mb-5">로그인</h4>
        <form @submit.prevent="logIn">
          <input type="text" v-model.trim="username" placeholder="아이디" class="form-field" id="username" />
          <input type="password" v-model.trim="password" placeholder="비밀번호" class="form-field" id="password" />
          <button type="submit" class="button primary">Log In</button>
          <button type="button" class="button secondary" @click="navigateToSignUp">Sign Up</button>
          <p v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</p>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountsStore } from '@/stores/accounts';

const username = ref(null);
const password = ref(null);
const errorMessage = ref(null);

const store = useAccountsStore();
const router = useRouter(); 

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  };
  
  store.logIn(payload).then(response => {
    errorMessage.value = null; // 성공 시 에러 메시지 초기화
    // 다른 성공 처리 로직 추가 가능
  }).catch(error => {
    errorMessage.value = error.response.data.detail || "An error occurred"; // 실패 시 에러 메시지 설정
  });
};

const navigateToSignUp = () => {
  router.push({ name: 'signup' }); // 'signup' 라우트로 이동
};
</script>

<style scoped>
.root {
  color: #ffefbc;
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
  height: 500px;
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

.form-field {
  font-weight: bold;
  width: 230px;
  margin: 0 auto 20px;
  height: 35px;
  padding: 6px 15px;
  border-radius: 5px;
  outline: none;
  border: none;
  /* background: #f5f5f5;
  color: #748194; */
  font-size: 14px;
}

.button {
  cursor: pointer;
  font-weight: bold;
  width: 230px;
  margin: 0 auto 20px;
  height: 45px;
  padding: 6px 15px;
  border-radius: 5px;
  outline: none;
  border: none;
  font-size: 14px;
}

.button.primary {
  color: white;
  background: #ffd13b; /* 연한 노란색 */
}

.button.primary:hover {
  opacity: 0.9;
}

.button.secondary {
  background: white;
  color: #FFC107; /* 연한 노란색 */
}

.button.secondary:hover {
  background: #FFF8E1; /* 더 연한 노란색 */
}

p.alert {
  font-size: 14px;
  color: #D32F2F; /* 에러 메시지 색상 */
  background-color: #FFCDD2; /* 에러 메시지 배경색 */
  padding: 10px;
  border-radius: 5px;
  margin-top: 20px;
}
</style>
