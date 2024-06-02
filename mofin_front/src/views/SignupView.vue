<template>
  <main class="root">
    <div class="signup-wrapper form active mt-5">
      <div class="form-wrapper">
        <h4 class="mb-5">회원가입</h4>
        <form @submit.prevent="signUp">
          <p v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</p>
          <input type="text" v-model.trim="username" placeholder="아이디" class="form-field" id="username" />
          <input type="password" v-model.trim="password1" placeholder="비밀번호 (8자 이상)" class="form-field" id="password1" />
          <input type="password" v-model.trim="password2" placeholder="비밀번호 확인 (8자 이상)" class="form-field" id="password2" />
          <input type="text" v-model.trim="name" placeholder="이름" class="form-field" id="name" />
          <input type="text" v-model.trim="nickname" placeholder="닉네임" class="form-field" id="nickname" />
          <input type="email" v-model.trim="email" placeholder="이메일" class="form-field" id="email" />
          <input type="number" v-model.trim="age" placeholder="나이" class="form-field" id="age" />
          <input type="number" v-model.trim="money" placeholder="자산" class="form-field" id="money" />
          <input type="number" v-model.trim="salary" placeholder="연봉" class="form-field" id="salary" />
          <button type="submit" class="button primary">Sign Up</button>
          <button type="button" class="button secondary" @click="navigateToSignIn">Sign In</button>
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
const password1 = ref(null);
const password2 = ref(null);
const nickname = ref(null);
const name = ref(null);
const email = ref(null);
const age = ref(null);
const salary = ref(null);
const money = ref(null);
const errorMessage = ref(null);

const store = useAccountsStore();
const router = useRouter(); 

const signUp = function () {
  if (password1.value !== password2.value) {
    errorMessage.value = "비밀번호가 일치하지 않습니다."; 
    return;
  }
  
  if (!username.value || !password1.value || !password2.value || !name.value || !nickname.value || !email.value || !age.value || !salary.value || !money.value) {
    errorMessage.value = "모든 정보를 입력해주세요.";
    return;
  }

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    name: name.value,
    email: email.value,
    age: age.value,
    salary: salary.value,
    money: money.value,
  };
  
  store.signUp(payload).then(response => {
    errorMessage.value = null; 
  }).catch(error => {
    errorMessage.value = error.response.data.detail || "An error occurred"; 
  });
};

const navigateToSignIn = () => {
  router.push({ name: 'login' }); // 'login' 라우트로 이동
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
  height: 830px; 
  margin-bottom: 50px;
  padding: 50px 20px;
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
  background: #FFC107; /* 연한 노란색 */
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
