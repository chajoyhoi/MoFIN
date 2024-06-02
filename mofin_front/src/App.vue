<template>
  <div id="app">
    <header>
      <div>
        <nav class="navbar navbar-expand-lg navcolor">
          <div class="container-fluid mx-5">
            <RouterLink to="/"><img alt="Vue logo" src="@/assets/mofin_logo.png" width="180"/></RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <RouterLink :to="{name:'recommend'}" class="nav-link" href="#">추천받기</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{name:'finance'}" class="nav-link" href="#">예적금보기</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{name:'exchange'}" class="nav-link" href="#">환율계산기</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{name:'search'}" class="nav-link" href="#">은행찾기</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{name:'article'}" class="nav-link" href="#">커뮤니티</RouterLink>
                </li>
              </ul>
              <ul class="navbar-nav ms-auto">
                <li class="nav-item" v-if="!store.isLogin">
                  <RouterLink :to="{name:'login'}" class="nav-link" href="#">로그인</RouterLink>
                </li>
                <li class="nav-item" v-else>
                  <span class="nav-link">{{ store.userdata?.username }}님 환영합니다</span>
                </li>
                <li class="nav-item" v-if="!store.isLogin">
                  <RouterLink :to="{name:'signup'}" class="nav-link" href="#">회원가입</RouterLink>
                </li>
                <li class="nav-item" v-if="store.isLogin">
                  <RouterLink :to="{name:'profile'}" class="nav-link" href="#">프로필</RouterLink>
                </li>
                <li class="nav-item" v-if="store.isLogin">
                  <span class="nav-link" @click="store.logOut">로그아웃</span>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>
    <RouterView />

    <footer class="footer " v-show="showFooter">
      <div class="footer-content">
        <p>&copy; 2024. All rights reserved. MoFIN</p>
      </div>
    </footer>

    <ChatBot />
  </div>


</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAccountsStore } from './stores/accounts';
import ChatBot from './components/ChatBot.vue';

const store = useAccountsStore()

import { ref, onMounted } from 'vue';

const showFooter = ref(false);

onMounted(() => {
  window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
      showFooter.value = true;
    } else {
      showFooter.value = false;
    }
  });
});
</script>

<style scoped>

.navcolor {
  background: #fdf8dc;
  /* background: rgba(255, 255, 210, 0.8) */
}
</style>

<style>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fdf8dc;
  color: #ffa647; 
  text-align: center;
  padding: 15px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
}

.footer p {
  margin: 0; 
}

@font-face {
  font-family: 'S-CoreDream-3Light';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: 'S-CoreDream-3Light';
  padding-bottom: 60px;
}

</style>
