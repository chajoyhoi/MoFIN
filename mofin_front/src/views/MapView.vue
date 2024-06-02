<template>
  <div class="container text-center mt-5 mb-5">
    <div>
      <h2 class="m-3">
        <span class="material-symbols-outlined">
        travel_explore
        </span>
        주변 은행 검색
      </h2>
      <h4 class="m-3 mb-5">
        <span class="material-symbols-outlined">
        pin_drop
        </span>
        현재 내 주변 은행을 검색해보세요!
      </h4>
    </div>
    <div class="content-map">
      <form class="d-flex flex-column align-items-center" @submit.prevent="search">
        <div class="d-flex flex-wrap justify-content-center gx-2 gy-3 w-100 px-3">
          <div class="col-12 col-md-3 mb-3 mb-md-0">
            <select
              class="form-select form-select-sm"
              name="location1"
              id="location1"
              v-model="mainRegion"
              @change="updateSubRegion"
            >
              <option :value="null" selected hidden>시 / 도 를 선택해주세요</option>
              <option v-for="locate1 in store.sectionList" :value="locate1" :key="locate1">
                {{ locate1 }}
              </option>
            </select>
          </div>
          <div class="col-12 col-md-3 mb-3 mb-md-0">
            <select
              class="form-select form-select-sm"
              name="location2"
              id="location2"
              v-model="subRegion"
            >
              <option :value="null" selected hidden>시 / 군 / 구 를 선택해주세요</option>
              <option v-for="locate2 in store.detailList[mainRegion]" :value="locate2" :key="locate2">
                {{ locate2 }}
              </option>
            </select>
          </div>
          <div class="col-12 col-md-3 mb-3 mb-md-0">
            <select class="form-select form-select-sm" name="bank" id="bank" v-model="selectedBank">
              <option :value="null" selected hidden>은행을 선택해주세요</option>
              <option v-for="bank in store.banks" :value="bank" :key="bank">
                {{ bank }}
              </option>
            </select>
          </div>
        </div>
        <button class="btn btn-pastel-yellow fixed-size mt-3" type="submit">검색</button>
      </form>
      <div id="map" style="width: 70%; height: 600px" class="mx-auto mt-3 mb-5"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { usePlacesStore } from '@/stores/places';

const store = usePlacesStore();

const mainRegion = ref(null);
const subRegion = ref(null);
const selectedBank = ref(null);

const searchword = ref(null);
const API_KEY = '';
let map;

const search = () => {
  if (!mainRegion.value || !subRegion.value || !selectedBank.value) {
    alert('시 / 도, 시 / 군 / 구, 은행을 모두 선택해주세요.');
    return;
  }

  searchword.value = `${mainRegion.value || ''} ${subRegion.value || ''} ${selectedBank.value || ''}`.trim();

  // Kakao 지도 API 스크립트 로드
  if (window.kakao && window.kakao.maps) {
    // 이미 kakao 객체가 정의되어 있을 경우 initMap 호출
    initMap(searchword.value, true);
  } else {
    // kakao 객체가 정의되어 있지 않으면 스크립트 로드
    const script = document.createElement('script');
    script.onload = () => initMap(searchword.value, true); // 로드 후 initMap 호출
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
    document.head.appendChild(script);
  }
};

const initMap = (keyword = '은행', isSearch = false) => {
  // kakao 객체가 정의되어 있는지 확인
  if (typeof kakao === 'undefined' || !kakao.maps) {
    console.error('Kakao 지도 API가 로드되지 않았습니다.');
    return;
  }

  kakao.maps.load(() => {
    var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    var mapContainer = document.getElementById('map'),
      mapOption = {
        center: new kakao.maps.LatLng(36.2683, 127.6358), // 대한민국 중심 좌표
        level: isSearch ? 5 : 14, // 검색 시 확대 레벨, 기본 지도는 전국 레벨
      };

    map = new kakao.maps.Map(mapContainer, mapOption);
    map.setMapTypeId(kakao.maps.MapTypeId.ROADMAP);

    if (isSearch) {
      var ps = new kakao.maps.services.Places();
      ps.keywordSearch(keyword, placesSearchCB);

      function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
          var bounds = new kakao.maps.LatLngBounds();
          for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
          map.setBounds(bounds);
        }
      }

      function displayMarker(place) {
        var marker = new kakao.maps.Marker({
          map: map,
          position: new kakao.maps.LatLng(place.y, place.x),
        });

        kakao.maps.event.addListener(marker, 'click', function () {
          infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
          infowindow.open(map, marker);
        });
      }
    }
  });
};

// 페이지가 로드될 때 기본 지도로 초기화
onMounted(() => {
  // Kakao 지도 API 스크립트 로드
  const script = document.createElement('script');
  script.onload = () => initMap(); // 로드 후 initMap 호출
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
  document.head.appendChild(script);
});
</script>

<style scoped>
/* 스타일링 추가 */
.fixed-size {
  width: 200px;
}

.form-select-sm {
  font-size: 0.875rem;
  padding: 0.25rem 0.5rem;
}

.container {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  background-color: rgba(255, 255, 224, 0.8);
}

.btn-pastel-yellow {
  background-color: #ffd727; 
  border: none;
  color: #000; 
  transition: background-color 0.3s;
}

.btn-pastel-yellow:hover {
  background-color: #FFF9E3; 
}



</style>
