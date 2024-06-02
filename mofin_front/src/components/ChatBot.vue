<template>
  <div>
    <button class="fixed-button" @click="toggleChatbot">
      <img src="@/assets/icon/robot_w.png" class="wid" alt="robot">
    </button>
    <div v-if="showChatbot" class="chat-container">
      <div id="chat-messages">
        <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender === '나' ? 'sent' : 'received']">
          {{ msg.sender }}: {{ msg.content }}
        </div>
      </div>
      <div id="user-input">
        <input v-model="userMessage" @keyup.enter="sendMessage" type="text" placeholder="# 궁금한건 MoFINBot 에게 물어보세요!" />
        <button @click="sendMessage">전송</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showChatbot = ref(false);
const messages = ref([]);
const userMessage = ref('');

// const OPENAI_API_KEY = '';

function toggleChatbot() {
  showChatbot.value = !showChatbot.value;
}

async function fetchAIResponse(prompt) {
  const apiEndpoint = 'https://api.openai.com/v1/chat/completions';
  const apiKey = OPENAI_API_KEY;
  let chatHistory = [];

  const fixedPrompts = [
    { keywords: ["환율", "환율 정보", "환율 정보 궁금", "환전"], response: "MoFIN의 환율 계산기 기능을 이용해보세요!" },
    { keywords: ["예금", "예금 정보", "예금 정보 궁금"], response: "MoFIN의 예금 비교 기능을 이용해보세요!" },
    { keywords: ["적금", "적금 정보", "적금 정보 궁금"], response: "MoFIN의 적금 비교 기능을 이용해보세요!" },
    { keywords: ["주변 은행", "주변 은행 정보", "주변 은행 궁금"], response: "MoFIN의 주변 은행 지도를 이용해보세요!" },
    { keywords: ["예적금 추천", "예적금 추천해줘", "금융 상품 추천"], response: "MoFIN의 금융 상품 추천 기능을 이용해보세요!" },
    { keywords: ["결혼", "결혼 예적금 추천"], response: "결혼을 하면 자금이 많이 필요하기 때문에 높은 금리 혜택이 있는 예적금 상품을 추천해요! MoFIN의 예적금 추천 기능을 이용해보세요!" },
  ];

  let adjustedPrompt = prompt;

  if (fixedPrompts[prompt]) {
    adjustedPrompt = fixedPrompts[prompt];
  } else {
    adjustedPrompt = `당신은 금리비교 사이트인 'MoFIN'에서 금융상품을 알려주는 챗봇입니다(은행이 아닙니다). 
    "${prompt}"에 적절히 답하고, 예적금 상품에 대해서 물어보면 잘 대답해주세요. 
    또 금리 비교 하면서 적절한 상품을 알아보라고 홍보해주세요!
    환율에 대해 물어보면 MoFIN 환율계산기 기능 이용하라고 해주세요. 
    주변 은행 위치를 물어보면 MoFIN의 주변 은행 검색 기능을 이용하라고 해주세요.
    묻는 말에만 똑바로 대답해 
    (그리고 모든 답변은 60자 이내로 줄여서 대답해주세요). 
    상품 추천해달라고 하면 조건에 맞는 거 추천해주고, 자세한 정보는 MoFIN 사이트 상품추천 탭에서 확인하라고 홍보해주세요`;
  }

  chatHistory.push({ role: "user", content: adjustedPrompt });

  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: "gpt-3.5-turbo",
      messages: chatHistory,
      temperature: 0.6,
      max_tokens: 300,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0.5,
      stop: ["Human"],
    }),
  };

  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    console.log(data); 

    if (data.choices && data.choices.length > 0) {
      const aiResponse = data.choices[0].message.content;
      chatHistory.push({ role: "assistant", content: aiResponse });
      return aiResponse;
    } else {
      throw new Error('API 응답이 예상한 형식이 아닙니다.');
    }
  } catch (error) {
    console.error('OpenAI API 호출 중 오류 발생:', error);
    return 'OpenAI API 호출 중 오류 발생';
  }
}

function addMessage(sender, message) {
  messages.value.unshift({ sender, content: message });
}

function sendMessage() {
  const message = userMessage.value.trim();
  if (message.length === 0) return;

  addMessage('나', message);
  userMessage.value = '';

  fetchAIResponse(message).then(aiResponse => {
    addMessage('챗봇', aiResponse);
  });
}
</script>

<style scoped>
body {
  background-color: #fff9e6; 
}
.chat-container {
  position: fixed;
  bottom: 60px;
  right: 20px;
  width: 400px;
  height: 600px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  background-color: #fffcf2; 
  z-index: 1000;
}
#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column-reverse;
  background-color: #fffcf2;
}
.message {
  border-top: 1px solid #ccc;
  padding: 10px;
  margin-top: 5px;
  background-color: #fffcf2;
  border-radius: 10px; 
}
.message.sent {
  background-color: #fff9e6; 
  align-self: flex-end;
  color: #000;
}
.message.received {
  background-color: #fff2cc; 
  align-self: flex-start;
  color: #000;
}
#user-input {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
  background-color: #fffcf2; 
}
#user-input input {
  flex: 1;
  padding: 10px;
  outline: none;
  border: 1px solid #ccc;
  border-radius: 5px;
}
#user-input button {
  border: none;
  background-color: #ffa726; 
  color: white;
  padding: 10px 15px;
  cursor: pointer;
  margin-left: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}
#user-input button:hover {
  background-color: #ffcc80; 
}
.fixed-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background-color: #ffa726;
  color: white;
  border: none;
  border-radius: 50%; 
  padding: 10px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  transition: background-color 0.3s;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
}
.fixed-button:hover {
  background-color: #ffcc80;
}

.wid {
  width: 40px;
}
</style>
