<template>
  <tr @click="goToDetail" class="clickable-row">
    <td>{{ index }}</td>
    <td>{{ article.title }}</td>
    <!-- <td>{{ article.content }}</td> -->
    <td>{{ article.user.nickname }}</td>
  </tr>
</template>

<script setup>
import { useRouter } from 'vue-router';

const props = defineProps({
  article: Object,
  index: Number
});

const articleId = props.article.id;
const router = useRouter();

const goToDetail = () => {
  router.push({ name: 'detail', params: { id: articleId } });
};
</script>

<style scoped>
td, th {
  text-align: center;
  vertical-align: middle;
}
.clickable-row {
  cursor: pointer;
}
.clickable-row:hover {
  background-color: #f0f0f0;
}
</style>
