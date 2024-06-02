<template>
  <main class="root">
    <div class="signup-wrapper form active mt-5">
      <div class="form-wrapper">
        <h4 class="mb-5">비밀번호 변경</h4>
        <form @submit.prevent="changePassword">
          <div class="form-group">
            <label class="form-label" for="old_password">기존 비밀번호</label>
            <input type="password" id="old_password" v-model="old_password" class="form-field input-field" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="new_password1">새 비밀번호</label>
            <input type="password" id="new_password1" v-model="new_password1" class="form-field input-field" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="new_password2">새 비밀번호 확인</label>
            <input type="password" id="new_password2" v-model="new_password2" class="form-field input-field" required>
          </div>
          <button type="submit" class="button primary">비밀번호 변경</button>
          <button type="button" class="button secondary" @click="goBack">뒤로가기</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { useAccountsStore } from "@/stores/accounts";
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useAccountsStore();

const old_password = ref(null);
const new_password1 = ref(null);
const new_password2 = ref(null);

const changePassword = function () {
  if (new_password1.value !== new_password2.value) {
    alert("새 비밀번호가 일치하지 않습니다.");
    return;
  }

  const payload = {
    old_password: old_password.value,
    new_password1: new_password1.value,
    new_password2: new_password2.value,
  };
  store.changePassword(payload);
};

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
