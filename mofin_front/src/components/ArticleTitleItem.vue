<template>
  <div class="article-item">
    <RouterLink :to="{ name: 'article', params: { id: article.id } }" class="text-dark text-decoration-none">
      <div class="article-content px-4">
        <span>{{ article.title }}</span>
        <span class="username text-body-secondary"> 
          <span class="text-body-tertiary">작성자 </span>{{ article.user.username }}</span>
        <hr>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { defineProps } from 'vue';

const props = defineProps({
  article: Object,
  index: Number
});

</script>

<style scoped>
.article-item {
  padding: 10px;
}

h3 {
  font-size: 1.25rem;
  margin: 0;
}

.article-content {
  display: flex;
  justify-content: space-between; 
  border-bottom: 1px solid #dbdbdb;
}

.username {
  margin-left: auto; 
}
</style>
