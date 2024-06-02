<template>
  <div class="container">
    <div class="header">
      <button @click="goBack" class="btn btn-back mb-3">뒤로가기</button>
    </div>
    <h2>게시글 작성하기</h2>
    <form @submit.prevent="createArticle" class="form-container">
      <label for="title" class="form-label">제목 : </label>
      <input type="text" id="title" v-model.trim="title" class="form-input"><br>
      <label for="content" class="form-label">내용 : </label>
      <textarea id="content" v-model.trim="content" class="form-input"></textarea><br>
      <div class="form-actions">
        <input type="submit" value="작성하기" class="btn btn-submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAccountsStore } from "@/stores/accounts";

const store = useAccountsStore();
const router = useRouter();

const title = ref('')
const content = ref('')

const goBack = () => {
  router.go(-1)
}

const createArticle = () => {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/articles/',
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    console.log('게시글 생성 완료!')
    router.push({ name: 'article' });
    alert('게시글이 생성되었습니다!')
  })
  .catch((err) => {
    console.log(err)
    alert('게시글 생성에 실패했습니다!')
  })
}
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 20px auto;
  text-align: center;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.btn {
  display: inline-block;
  padding: 8px 16px;
  font-size: 0.9rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
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

.form-container {
  text-align: left;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-input {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
}

textarea.form-input {
  height: 200px;
  resize: vertical;
}

.form-actions {
  text-align: right;
}

.btn-submit {
  background-color: #c3e6cb;
  color: #155724;
  font-size: 1rem;
  padding: 10px 20px;
  cursor: pointer;
}
.btn-submit:hover {
  background-color: #b1dfbb;
}
</style>
