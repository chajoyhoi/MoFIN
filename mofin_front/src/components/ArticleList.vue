<template>
  <div class="containerss mb-3">
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <!-- <th>내용</th> -->
            <th>작성자</th>
          </tr>
        </thead>
        <tbody>
          <ArticleListItem
            v-for="(article, index) in paginatedArticles"
            :key="article.id"
            :article="article"
            :index="getArticleIndex(index)"
          />
        </tbody>
      </table>
    </div>
    <div class="d-flex justify-content-center mt-4">
      <button class="btn btn-pastel-blue mx-2" @click="prevPage" :disabled="currentPage === 1">이전</button>
      <button class="btn btn-pastel-blue mx-2" @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
  <br>

</template>

<script setup>
import { computed, ref, watch } from 'vue';
import { useArticlesStore } from '@/stores/articles';
import ArticleListItem from './ArticleListItem.vue';

const props = defineProps({
  currentPage: Number,
});

const emit = defineEmits(['page-changed']);

const store = useArticlesStore();
const itemsPerPage = 10;

const paginatedArticles = computed(() => {
  const reversedArticles = [...store.articles].reverse();
  const start = (props.currentPage - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return reversedArticles.slice(start, end);
});

const totalPages = computed(() => Math.ceil(store.articles.length / itemsPerPage));

const nextPage = () => {
  if (props.currentPage < totalPages.value) {
    emit('page-changed', props.currentPage + 1);
  }
};

const prevPage = () => {
  if (props.currentPage > 1) {
    emit('page-changed', props.currentPage - 1);
  }
};

const getArticleIndex = (index) => {
  // 전체 글 수에서 현재 페이지에 표시되는 글 수를 뺀 후, 해당 위치부터 역순으로 번호를 부여합니다.
  return store.articles.length - ((props.currentPage - 1) * itemsPerPage) - index;
};

watch(() => props.currentPage, () => {
  store.getArticles(props.currentPage);
});
</script>

<style scoped>
.containerss {
  max-width: 1000px;
  margin: 0 auto;
}
.table {
  margin-top: 20px;
}

/* .ma-bt {
  margin-bottom:500px;
} */
</style>
