<template>
  <main class="container">
    <div class="row">
      <div class="col-lg-8 mt-3">
        <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3500">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <RouterLink :to="{ name: 'recommend' }" class="nav-link" href="#">
                <img src="@/assets/금융상품추천.png" class="d-block w-100 carousel-image" alt="...">
              </RouterLink>
            </div>
            <div class="carousel-item">
              <RouterLink :to="{ name: 'finance' }" class="nav-link" href="#">
                <img src="@/assets/예적금상품보기.png" class="d-block w-100 carousel-image" alt="...">
              </RouterLink>
            </div>
            <div class="carousel-item">
              <RouterLink :to="{ name: 'search' }" class="nav-link" href="#">
                <img src="@/assets/은행지도.png" class="d-block w-100 carousel-image" alt="...">
              </RouterLink>
            </div>
            <div class="carousel-item">
              <RouterLink :to="{ name: 'exchange' }" class="nav-link" href="#">
                <img src="@/assets/환율계산기.png" class="d-block w-100 carousel-image" alt="...">
              </RouterLink>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
      <div class="col-lg-4 mt-5 text-center d-flex d-none d-lg-flex flex-column align-items-center">
        <div class="mb-3">
          <RouterLink :to="{ name: 'deposit' }">
            <button class="btn-round mb-2">
              <img src="@/assets/icon/payments.png" class="wi" alt="payments">
              <p class="fw-bold fs-5">예금</p>
            </button>
          </RouterLink>

          <RouterLink :to="{ name: 'saving' }" class="text-dark text-decoration-none">
            <button class="btn-round">
              <img src="@/assets/icon/wallet.png" class="wi" alt="wallet">
              <p class="fw-bold fs-5">적금</p>
            </button>
          </RouterLink>
        </div>
        <div>
          <RouterLink :to="{ name: 'recommend' }" class="text-dark text-decoration-none">
            <button class="btn-square">
              <img src="@/assets/icon/recommend1.png" class="wid" alt="recommend1">
              <p class="fw-bold">추천받기</p>
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'exchange' }" class="text-dark text-decoration-none">
            <button class="btn-square mb-2">
              <img src="@/assets/icon/calculate.png" class="wid" alt="calculate">
              <p class="fw-bold">환율계산기</p>
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'search' }" class="text-dark text-decoration-none">
            <button class="btn-square">
              <img src="@/assets/icon/map.png" class="wid" alt="map">
              <p class="fw-bold">은행찾기</p>
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'article' }" class="text-dark text-decoration-none">
            <button class="btn-square">
              <img src="@/assets/icon/article.png" class="wid" alt="article">
              <p class="fw-bold">커뮤니티</p>
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'chatbot2' }" class="text-dark text-decoration-none">
            <button class="btn-square mb-2">
              <img src="@/assets/icon/robot.png" class="wid" alt="robot">
              <p class="fw-bold">챗봇</p>
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'home' }" class="text-dark text-decoration-none">
            <button class="btn-square">
              <img src="@/assets/icon/mofin.jpg" class="wid" alt="mofin">
              <p class="fw-bold">MoFIN</p>
            </button>
          </RouterLink>
        </div>
      </div>
    </div>
    <div class="containeraa">
      <ArticleTitleList />
    </div>
    <br>
    <br>
    <br>
    <div class="team-container pd">
      <div class="team-info">
        <h3>MoFIN Project Developer</h3>
        <div class="row mt-1">
          <div class="col-md-6 text-center developer-info">
            <p>팀장</p>
            <img src="@/assets/p_sm.png" class="rounded-circle developer-image" alt="Developer 1">
            <h5 class="mt-3">이승민</h5>
            <p>tmdals77117@naver.com</p>
          </div>
          <div class="col-md-6 text-center developer-info">
            <p>팀원</p>
            <img src="@/assets/p_yr.png" class="rounded-circle developer-image" alt="Developer 2">
            <h5 class="mt-3">차유림</h5>
            <p>c4526@naver.com</p>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import ArticleTitleList from '@/components/ArticleTitleList.vue';
</script>

<style scoped>
.ma-bt {
  margin-bottom: 100px;
}

.pd {
  padding-top: 50px;
  padding-bottom: 100px;
  color: #666666;
}

.team-container {
  background-color: #FFFFE0;
}
.team-info {
  text-align: center; 
}
.containeraa {
  background: #fff4bb;
  padding: 20px;
  border-radius: 10px;
  margin: 20px 0px 0px 0px;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.1);
}

.developer-image {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border: 2px solid #ccc;
}

.carousel-item img {
  width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

.carousel-image {
  object-fit: cover;
  width: 100%;
  height: auto;
  border: 1px solid #ccc; 
}

.btn-round {
  width: 150px;
  height: 150px;
  border: 1px solid #ffffff;
  background-color: rgb(252, 216, 98);
  border-radius: 10px;
  margin: 20px 20px 30px;
  padding-top: 25px;
  color: #fff;
  transition: background-color 0.3s ease;
}

.btn-round:hover {
  background-color: rgba(252, 216, 98, 0.8);
}

.btn-square {
  width: 100px;
  height: 100px;
  border: 1px solid #ffffff00;
  background-color: #fff;
  margin: 5px 5px;
  border-radius: 10px;
  padding-top: 10px;
  color: #666666;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.btn-square:hover {
  background-color: rgba(255, 255, 255, 0.8);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.wi {
  width: 80px;
}

.wid {
  width: 50px;
}

.developer-info p {
  margin-bottom: 5px;
}

.developer-info h5 {
  margin-top: 10px;
}

@media (max-width: 992px) {
  .carousel-image {
    height: 60vh;
  }
}

.row.mt-1 {
  margin-left: -1px; 
  margin-right: -1px; 
}

.col-md-6 {
  padding-left: 1px; 
  padding-right: 1px;
}


</style>
