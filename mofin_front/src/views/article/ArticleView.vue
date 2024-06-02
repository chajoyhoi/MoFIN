<template>
  <div class="container my-5">
    <div class="header">
      <button @click="goBack" class="btn btn-back mb-3">뒤로가기</button>
    </div>
    <h2>커뮤니티</h2>
    <ArticleList :current-page="currentPage" @page-changed="handlePageChange" />
    <button v-if="accountsStore.isLogin" @click="goToCreatePage" class="btn btn-submit btn-bottom-right">게시글 작성</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useArticlesStore } from '@/stores/articles';
import { useRouter } from 'vue-router';
import ArticleList from '@/components/ArticleList.vue';
import { useAccountsStore } from '@/stores/accounts';

const store = useArticlesStore()
const accountsStore = useAccountsStore()
const router = useRouter()
const currentPage = ref(1)

const goToCreatePage = () => {
  router.push({ name: 'create' });
};

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
};

const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  store.getArticles(newPage);
};

onMounted(() => {
  store.getArticles(currentPage.value);
});
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
  position: relative; 
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
/* h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
} */

.title-center {
  text-align: center;
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

.btn-submit {
  background-color: #bae2f1;
  color: #333;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
}

.btn-submit:hover {
  background-color: #a8d0e6;
}

.btn-bottom-right {
  position: absolute;
  bottom: 20px;
  right: 20px;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}

.mg {
  margin-bottom: 60px;
}

</style>
