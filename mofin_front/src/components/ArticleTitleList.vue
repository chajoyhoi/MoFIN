<template>
  <div class="px-5 pt-3 mb-3">
    <RouterLink :to="{ name: 'article' }" class="text-dark text-decoration-none">
    <h5 class="mb-4 fc">
      <img src="@/assets/icon/sound.png" width="30" alt="sound">
      최신 소식
    </h5>
    </RouterLink>
    <ArticleTitleItem
      v-for="(article, index) in topArticles"
      :key="article.id"
      :article="article"
      :index="index"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useArticlesStore } from '@/stores/articles';
import ArticleTitleItem from '@/components/ArticleTitleItem.vue';
import { onMounted } from 'vue';

const store = useArticlesStore();

// 상위 5개의 최신 글을 가져오기 위해 computed 속성 사용
const topArticles = computed(() => {
  return store.articles
    .slice() 
    .sort((a, b) => b.id - a.id) 
    .slice(0, 5); 
});

// onMounted(() => {
//   store.fetchArticles();
// });
</script>

<style scoped>
.fc {
  color: #494949;
  font-weight: bolder
}
</style>
