<template>
  <div class="container my-5">
    <button @click="goBack" class="btn btn-back mb-3">뒤로가기</button>
    <div class="article-details">
      <p class="author-text">작성자 <span>{{ article.username }}</span></p>
      <h2>{{ article.title }}</h2>
      <hr>
      <h4>{{ article.content }}</h4>
      <p class="small-text mt-5">작성시간 : {{ formattedCreatedAt }}</p>
      <p class="small-text">수정시간 : {{ formattedUpdatedAt }}</p>
      <div class="author-actions" v-if="isAuthor">
        <button @click="updateArticle" class="btn btn-edit">게시글 수정</button>
        <button @click="deleteArticle(article.id)" class="btn btn-delete">게시글 삭제</button>
      </div>
    </div>
    <div class="like-section">
      <button v-if="!isLiked" @click="toggleLike" class="btn btn-like">
        <img src="@/assets/icon/heart_w.png" class="wi" alt="like">
        <span class="like-text">{{ likeCount }}</span>
      </button>
      <button v-if="isLiked" @click="toggleLike" class="btn btn-like">
        <img src="@/assets/icon/heart_y.png" class="wi" alt="not_like">
        <span class="like-text">{{ likeCount }}</span>
      </button>
    </div>
    <hr>
    <div class="comment-section">
      <textarea v-model.trim="commentContent" placeholder="댓글을 작성하세요" class="comment-input"></textarea>
      <div class="comment-actions">
        <button @click="createComment" class="btn btn-comment">댓글 작성</button>
      </div>
    </div>
    <br>
    <hr class="mt-4">
    <h5 v-if="comments.length" class="mb-4">댓글 목록</h5>
    <div v-for="comment in comments" :key="comment.id" class="comment">
      <p class="comment-author">
        {{ comment.user.username }} 님
      </p>
      <p>
        {{ comment.content }}
        <button v-if="isCommentAuthor(comment)" @click="deleteComment(comment.id)" class="btn btn-delete-comment">삭제</button>
      </p>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useArticlesStore } from '@/stores/articles';
import { useAccountsStore } from '@/stores/accounts';

const isLiked = ref(false);
const likeCount = ref(0);

const route = useRoute()
const router = useRouter()
const store = useArticlesStore()
const accountstore = useAccountsStore()

const articleId = route.params.id
const article = ref(
  store.articles.find((product) => product.id == articleId)
)

const commentContent = ref('')
const comments = ref([])

const goBack = () => {
  router.go(-1)
}

onMounted(() => {
  fetchArticle();
  fetchLikeStatus();
  fetchLikeCount();
  fetchComments();
});

const formatDateTime = (dateTime) => {
  const date = new Date(dateTime)
  return date.toLocaleString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  }).replace('T', ' ')
}

const formattedCreatedAt = computed(() => {
  return article.value ? formatDateTime(article.value.created_at) : ''
})

const formattedUpdatedAt = computed(() => {
  return article.value ? formatDateTime(article.value.updated_at) : ''
})

const isAuthor = computed(() => {
  return article.value.username === accountstore.userdata?.username
})

const fetchArticle = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${accountstore.token}`,
    },
  })
    .then((res) => {
      article.value = res.data;
      isLiked.value = res.data.is_liked;
      fetchComments();
    })
    .catch((err) => {
      console.log(err);
    });
};

const fetchComments = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${articleId}/comments/`,
    headers: {
      Authorization: `Token ${accountstore.token}`
    }
  })
  .then((res) => {
    comments.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}

const isCommentAuthor = (comment) => {
  return comment.user.username === accountstore.userdata?.username
}

const deleteArticle = function () {
  const token = store.token
  if (confirm("게시글을 삭제하시겠습니까?") == true) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/articles/${articleId}`,
      headers: {
        Authorization: `Token ${token}`
      },
    })
      .then((res) => {
        console.log('게시물 삭제 완료!')
        router.push({name: 'article'})
      })
      .catch((err) => {
        console.log(err)
      })
  }
}

const updateArticle = function () {
  router.push({name: 'update', params: { id: articleId }});
};

// 댓글 생성
const createComment = () => {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${articleId}/comments/create/`,
    headers: {
      Authorization: `Token ${accountstore.token}`
    },
    data: {
      content: commentContent.value
    }
  })
  .then((res) => {
    comments.value.push(res.data)
    commentContent.value = ''
  })
  .catch((err) => {
    console.log(err)
  })
}

const deleteComment = (commentId) => {
  const confirmed = confirm('댓글을 삭제하시겠습니까?');

  if (confirmed) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/articles/comments/${commentId}`,
      headers: {
        Authorization: `Token ${accountstore.token}`
      }
    })
    .then((res) => {
      console.log('댓글 삭제 성공');
      comments.value = comments.value.filter(comment => comment.id !== commentId);
    })
    .catch((err) => {
      console.log(err);
    });
  }
};


// 좋아요 상태를 가져오는 함수
const fetchLikeStatus = () => {
  axios.get(`http://127.0.0.1:8000/articles/${articleId}/like-status/`, {
    headers: {
      Authorization: `Token ${accountstore.token}`
    }
  })
  .then(response => {
    isLiked.value = response.data.is_liked
  })
  .catch(error => {
    console.error('좋아요 상태 가져오기 실패:', error)
  })
}

// 좋아요 수를 가져오는 함수
const fetchLikeCount = () => {
  axios.get(`http://127.0.0.1:8000/articles/${articleId}/like-count/`, {
    headers: {
      Authorization: `Token ${accountstore.token}`
    }
  })
  .then(response => {
    likeCount.value = response.data.like_count;
  })
  .catch(error => {
    console.error('좋아요 수 가져오기 실패:', error)
  })
}

// 좋아요 토글 함수
const toggleLike = () => {
  axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, {
    headers: {
      Authorization: `Token ${accountstore.token}`
    }
  })
  .then(response => {
    isLiked.value = response.data.is_liked;
    likeCount.value = response.data.like_count;  // 좋아요 수 업데이트
  })
  .catch(error => {
    console.error('좋아요 토글 실패:', error)
  })
}

onMounted(() => {
  fetchArticle();
  fetchLikeStatus();
  fetchLikeCount();
  fetchComments();
})

</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  max-width: 800px;
  margin: 20px auto;
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

.btn-edit, .btn-delete, .btn-comment {
  margin: 0 5px;
}

.btn-edit {
  background-color: #bae2f1;
  color: #333;
}

.btn-delete {
  background-color: #f8d7da;
  color: #721c24;
}

.btn-like {
  background-color: #fff5d8;
  color: #333;
  padding: 5px 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.btn-comment {
  background-color: #c3e6cb;
  color: #155724;
  float: right;
  margin-top: 0px;
}

.article-details {
  margin-bottom: 20px;
  text-align: left;
}

.article-details h2 {
  font-size: 2rem;
  margin-bottom: 10px;
}

.small-text {
  font-size: 0.8rem;
  color: #555;
}

.author-text {
  color: #555;
  font-size: 0.9rem;
}

.author-text span {
  color: #000;
  font-size: 1rem;
}

.author-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

.like-section {
  margin-top: 20px;
  text-align: center;
}

.like-text {
  margin-left: 5px;
}

.comment-section {
  margin-top: 20px;
  position: relative;
}

.comment-input {
  width: 100%;
  height: 100px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.comment-actions {
  text-align: right;
}

.comment {
  margin-top: 10px;
}

.comment-author {
  color: #555;
  font-size: 0.9rem;
}

.comment p {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-delete-comment {
  background-color: #f5c6cb;
  color: #721c24;
  font-size: 0.8rem;
  padding: 4px 8px;
}

.wi {
  width: 16px;
  margin: 5px;
}
</style>
