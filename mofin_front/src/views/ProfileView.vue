<template>
  <main>
    <div class="container text-center my-4" style="background: rgba(255, 255, 224, 0.8);">
      <button @click="goBack" class="btn btn-outline-light-gray mb-4 float-start">뒤로가기</button>
      <div class="containers text-center my-3">
        <h2 class="mb-4 mt-4 text-center mx-5">
          <span class="material-symbols-outlined" style="font-size: xx-large">
            assignment_ind
          </span>
          {{ userdata.name }} 님의 프로필 페이지
        </h2>
        <!-- <p><strong>이름 :</strong> {{ userdata.name }}</p> -->
        <p><strong>아이디 :</strong> {{ userdata.username }}</p>
        <p><strong>이메일 :</strong> {{ userdata.email }}</p>
        <p><strong>닉네임 :</strong> {{ userdata.nickname }}</p>
        <p><strong>나이 :</strong> {{ userdata.age }}</p>
        <p><strong>자산 :</strong> {{ userdata.money }}</p>
        <p><strong>연봉 :</strong> {{ userdata.salary }}</p>
        <div class="d-flex justify-content-center mt-4 mb-4">
          <RouterLink :to="{ name: 'profileupdate' }">
            <button class="btn btn-pastel-blue mx-2">회원정보 수정</button>
          </RouterLink>
          <RouterLink :to="{ name: 'changepassword' }">
            <button class="btn btn-pastel-yellow mx-2">비밀번호 변경</button>
          </RouterLink>
          <button @click="deleteAccount" class="btn btn-pastel-red mx-2">회원 탈퇴</button>
        </div>
      </div>
    </div>

    <div class="container text-center my-3" style="background: rgba(255, 255, 224, 0.8);">
      <div class="accordion" id="profileAccordion">
        <!-- 좋아요 누른 글 목록 -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#likedArticlesCollapse" aria-expanded="false" aria-controls="likedArticlesCollapse">
              좋아요 누른 글 목록
            </button>
          </h2>
          <div id="likedArticlesCollapse" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#profileAccordion">
            <div class="accordion-body">
              <ol v-if="likedArticles.length > 0" class="list-group list-group-numbered">
                <li v-for="article in likedArticles" :key="article.id" class="list-group-item d-flex justify-content-between align-items-center">
                  {{ article.title }}
                  <RouterLink :to="{ name: 'detail', params: { id: article.id } }">
                    <button class="btn btn-link">자세히 보기</button>
                  </RouterLink>
                </li>
              </ol>
              <p v-else>좋아요 한 게시글이 아직 없습니다.</p>
            </div>
          </div>
        </div>

        <!-- 구매상품 리스트 -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#purchaseProductCollapse" aria-expanded="false" aria-controls="purchaseProductCollapse">
              가입 상품 리스트 & 금리 비교
            </button>
          </h2>
          <div id="purchaseProductCollapse" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#profileAccordion">
            <div class="accordion-body">
              <ProfileProduct />
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useAccountsStore } from '@/stores/accounts';
import { RouterLink } from 'vue-router';
import ProfileProduct from '../components/ProfileProduct.vue';
import axios from 'axios';

const router = useRouter()
const profilestore = useAccountsStore()
const userdata = profilestore.userdata
const likedArticles = ref([])

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
};

const fetchLikedArticles = () => {
  axios.get('http://127.0.0.1:8000/articles/profile/liked-articles/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    likedArticles.value = response.data
    // profilestore.getUserdata()
  })
  .catch(error => {
    console.error('좋아요 누른 글 목록 가져오기 실패:', error)
  })
}

onMounted(() => {
  fetchLikedArticles();
  // profilestore.getUserdata()
});

const deleteAccount = () => {
  profilestore.deleteAccount()
}
</script>

<style scoped>
.container {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
}

.containers {
  padding: 20px;
  border-radius: 10px;
  max-width: 1000px;
}

.btn-outline-light-gray {
  background-color: #f8f9fa;
  border: 1px solid #e5ebf1;
  color: #000;
  transition: background-color 0.3s, color 0.3s;
}
.btn-outline-light-gray:hover {
  background-color: #f9fcff;
}
.btn-pastel-blue {
  background-color: #bae2f1;
  color: #333;
  border: none;
}
.btn-pastel-yellow {
  background-color: #fef3bd;
  color: #333;
  border: none;
}
.btn-pastel-red {
  background-color: #f4cccc;
  color: #333;
  border: none;
}
.btn-link {
  text-decoration: none;
  color: #007bff;
}
.btn-link:hover {
  color: #0056b3;
}

.float-start {
  float: left;
}

.accordion {
  background: rgba(255, 255, 224, 0.8);
  border-radius: 10px;
}

</style>
