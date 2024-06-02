import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// accounts
import LoginView from '../views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '../views/ProfileUpdateView.vue'
import ChangePasswordView from '@/views/ChangePasswordView.vue'

// map
import MapView from '@/views/MapView.vue'

// exchange
import ExchangeView from '@/views/ExchangeView.vue'

// article
import ArticleView from '@/views/article/ArticleView.vue'
import ArticleCreateView from '@/views/article/ArticleCreateView.vue'
import ArticleDetailView from '@/views/article/ArticleDetailView.vue'
import ArticleUpdateView from '@/views/article/ArticleUpdateView.vue'

//Finance
import FinanceView from '@/views/FinanceView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingView from '@/views/SavingView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'
import RecommendView from '@/views/RecommendView.vue'

//chat
import ChatBot from '@/components/ChatBot.vue'
import ChatBot2 from '@/components/ChatBot2.vue'

import { useAccountsStore } from '@/stores/accounts'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // accounts
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },

    // exchange
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },

    // article
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/article/:id',
      name: 'detail',
      component: ArticleDetailView
    },
    {
      path: '/article/update',
      name: 'update',
      component: ArticleUpdateView
    },

    // map
    {
      path: '/search',
      name: 'search',
      component: MapView
    },
    //profile
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profileupdate',
      name: 'profileupdate',
      component: ProfileUpdateView
    },
    {
      path: "/changepassword",
      name: "changepassword",
      component: ChangePasswordView,
    },
    //finance
    {
      path: "/finance",
      name: "finance",
      component: FinanceView,
    },
    {
      path: "/deposit",
      name: "deposit",
      component: DepositView,
    },
    {
      path: '/deposit/detail/:id',
      name: 'DepositDetail',
      component: DepositDetailView,
    },
    {
      path: "/saving",
      name: "saving",
      component: SavingView,
    },
    {
      path: "/saving/detail/:id",
      name: "SavingDetail",
      component: SavingDetailView,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView,
      meta: { requiresAuth: true }
    },
    
    // 챗봇
    {
      path: "/chatbot",
      name: "chatbot",
      component: ChatBot,
    },
    {
      path: "/chatbot2",
      name: "chatbot2",
      component: ChatBot2,
    }
  ]
})

router.beforeEach((to, from, next) => {
  const store = useAccountsStore()
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.isLogin) {
      alert('로그인이 필요합니다. 로그인 페이지로 이동합니다.')
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
