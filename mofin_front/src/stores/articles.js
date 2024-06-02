import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountsStore } from './accounts'

export const useArticlesStore = defineStore('articles', () => {
  // const router = useRouter()
  const accountsstore = useAccountsStore()
  const articles = ref([])
  const token = computed(() => accountsstore.token)

  // const token = ref(accountsstore.token)
  // const isLogin = computed(() => {
  //   if (token.value === null) {
  //     return false
  //   } else {
  //     return true
  //   }
  // })

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/articles/',
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      articles.value = res.data
      // console.log(accountsstore.token)
      // console.log(token.value)
      // console.log(token)
      console.log('게시물 불러오기 성공!')
      console.log(res.data)
    })
    .catch((err) => {
      // console.log(route.params.article_id)
      console.log(err)
    })
  }
  
  return { articles, getArticles, token }
}, { persist: true })
