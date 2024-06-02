import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useFinanceStore } from './finance'


export const useAccountsStore = defineStore('accounts', () => {
  const API_URL = "http://127.0.0.1:8000";
  const router = useRouter()
  const token = ref(null)
  
  const financeStore = useFinanceStore()

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  // const isLogin = computed(() => token.value !== null)
  
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    }) .then(res => {
      alert(`${username} 님 반갑습니다!`)
      console.log(res.data)
      token.value = res.data.key
      console.log(token.value)
      console.log('로그인 성공')
      getUserdata();
      financeStore.saveDeposit();
      financeStore.getDeposit();
      financeStore.saveSaving();
      financeStore.getSaving();
      // token = token.value
      // console.log('===')
      // console.log(token)

      // 로그인 성공 후 accountstore.user 설정
      axios({
        method: "get",
        url: 'http://127.0.0.1:8000/accounts/profile/get_userdata/',
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          // accountstore.user에 사용자 데이터 설정
          // accountstore.user = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      }) 
      .then(() => {
        router.push({name:'home'})
      })
      .catch((err) => {
        alert("아이디 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요.")
        console.log(err);
      });
    
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
      headers: { Authorization: `Token ${token.value}`}
    })
      .then(res => {
        alert('로그아웃이 완료되었습니다.')
        console.log(res.data)
        token.value = null  // token 초기화
        // userProfile.value = null
        router.push({ name: 'home' })
      })
      .catch(err => {
        console.log(err)
      })
  }


  const signUp = function (payload) {
    const { username, password1, password2, email, nickname, age, salary, money, name } = payload
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/registration/',
      data: {
        username, password1, password2, email, nickname, age, salary, money, name
      }
    })
    .then((response) => {
      console.log('회원가입 성공')
      const password = password1
      logIn({username, password})
      router.push({name:'home'})
    })
    .catch((err) =>{
      // alert('정보를 모두 입력해주세요')
      console.log(err)
    })
  };


  const userdata = ref(null)
  const getUserdata = function () {
    axios({
      method: "get",
      url: 'http://127.0.0.1:8000/accounts/profile/get_userdata/',
      headers: { Authorization: `Token ${token.value}` },
    })
      .then((res) => {
        userdata.value = res.data
        console.log('프로필 불러오기 성공!')
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const updateProfile = function (payload) {
    const { nickname, email, age, money, salary } = payload;
    axios({
      method: "put",
      url: `${API_URL}/accounts/profile/update/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: {
        nickname,
        email,
        age,
        money,
        salary
      },
    })
      .then((res) => {
        alert("프로필이 수정되었습니다.");
        console.log(res.data);
        // getUserdata()
        userdata.value = res.data 
        // router.push({name: 'home'}); // 한 페이지 앞으로 
        router.go(-1)
      })
      // .then(() =>
      // )
      .catch((err) => {
        console.log(err);
      });
  };

  const changePassword = function (payload) {
    const { old_password, new_password1, new_password2 } = payload;
    axios({
      method: "post",
      url: `${API_URL}/accounts/password/change/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: {
        old_password,
        new_password1,
        new_password2,
      },
    })
      .then(() => {
        console.log("비밀번호 변경 성공");
        alert("비밀번호가 변경되었습니다. 다시 로그인해주세요.");
        logOut();
      })
      .catch(() => {
        console.log("비밀번호 변경 실패");
        alert("비밀번호 변경에 실패했습니다. 다시 시도해 주세요");
      });
  };

  const deleteAccount = function() {
    if (confirm("정말로 탈퇴하시겠습니까?")) {
      axios({
        method: 'delete',
        url: `${API_URL}/accounts/profile/delete_account/`,
        headers: { Authorization: `Token ${token.value}` }
      })
      .then((response) => {
        console.log(response.data)
        token.value = null
        userdata.value = null
        alert('탈퇴가 완료되었습니다')
        router.push({name: 'home'})
      })
      .catch((error) => {
        alert('탈퇴 중 오류가 발생했습니다.')
        console.log(error)
      })
    }
  }

  // const deleteAccount = function () {
  //   axios({
  //     method: "delete",
  //     url: `${API_URL}/accounts/delete_account/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`,
  //     },
  //   })
  //     .then(() => {
  //       // token.value = null;
  //       alert("회원 탈퇴가 완료되었습니다.");
  //       router.push({ name: 'home' });
  //     })
  //     .catch(err => {
  //       console.log('회원 탈퇴 중 오류 발생', err);
  //       alert("회원 탈퇴 중 오류가 발생했습니다.");
  //     });
  // };


  return { logIn, signUp, token, isLogin, logOut, userdata, getUserdata, updateProfile, changePassword, deleteAccount }
}, { persist: true })