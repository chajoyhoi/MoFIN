<template>
  <div class="container mt-5">
    <div class="header">
      <button @click="goBack" class="btn btn-back mb-3">뒤로가기</button>
    </div>
    <h2>게시글 수정하기</h2>
    <form @submit.prevent="updateArticle" class="form-container">
      <label for="title" class="form-label">제목 : </label>
      <input type="text" id="title" v-model.trim="title" class="form-input"><br>
      <label for="content" class="form-label">내용 : </label>
      <textarea id="content" v-model.trim="content" class="form-input"></textarea><br>
      <div class="form-actions">
        <input type="submit" value="수정하기" class="btn btn-submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAccountsStore } from "@/stores/accounts";

const store = useAccountsStore();
const route = useRoute();
const router = useRouter();

const articleId = route.params.id
const title = ref('')
const content = ref('')

onMounted(() => {
  // 기존 게시글의 내용을 가져와서 폼에 채워줍니다.
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${articleId}`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    title.value = res.data.title;
    content.value = res.data.content;
  })
  .catch((err) => {
    console.log(err);
  });
});

const goBack = () => {
  router.go(-1)
}

const updateArticle = () => {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/${articleId}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    console.log(res.data)
    console.log('게시글 수정 성공')
    router.push({ name: 'detail', params: { id: articleId } }); // 수정 후 상세 페이지로 이동
    alert('게시글이 수정되었습니다!')
  })
  .catch((err) => {
    console.log(err)
    window.alert('작성자가 아닙니다!')
  })
}
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
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

/* h1 {
  font-size: 1.5rem;
  margin: 0 auto;
  text-align: center;
  flex-grow: 1;
} */

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
