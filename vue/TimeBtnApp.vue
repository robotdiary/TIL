<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>버튼 박스 제작</h1>
    <h2>예약페이지</h2>
    <h3>시간 선택</h3>
    <button 
    class="custom-btn btn-16"
    v-for="(time, index) in times" :key="index"
    @click="clickbtn">
      {{ time }}
    </button>
    <hr>
    <span><strong>선택시간 : </strong></span>
    <span v-for="(time, index) in timelst" :key="index">
      <strong> {{ time }} </strong></span>
  </div>
</template>

<script>
// import TimeBtn from '@/components/TimeBtn'

export default {
  name: 'App',
  // components: {
  //   TimeBtn
  // },
    data: function () {
      return {
        times: [
          "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
          "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
          "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
        ],
        timelst: []
      }
    },
  methods: {
    clickbtn: function (event) {
      if (this.timelst.includes(event.target.innerText)) {
        this.timelst.splice(this.timelst.indexOf(event.target.innerText),1)
        event.target.removeAttribute('disabled', "disabled")
        event.target.classList.toggle('btn-8')
      } else if (this.timelst.length >= 5) {
        alert('5타임까지만 신청할 수 있습니다.')
      } else {
        this.timelst.push(event.target.innerText)
        console.log(event.target)
        event.target.classList.toggle('btn-8')
        // event.target.setAttribute('disabled', "disabled")
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Noto-Sans-Korean, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
button {
  margin: 20px;
}
.custom-btn {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
    box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
    7px 7px 20px 0px rgba(0,0,0,.1),
    4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}
.btn-16 {
  border: none;
  color: #000;
}
.btn-16:after {
  position: absolute;
  content: "";
  width: 0;
  height: 100%;
  top: 0;
  left: 0;
  direction: rtl;
  z-index: -1;
  box-shadow:
    -7px -7px 20px 0px #fff9,
    -4px -4px 5px 0px #fff9,
    7px 7px 20px 0px #0002,
    4px 4px 5px 0px #0001;
  transition: all 0.3s ease;
}
.btn-16:hover {
  color: #000;
}
.btn-16:hover:after {
  left: auto;
  right: 0;
  width: 100%;
}
.btn-16:active {
  top: 2px;
}
.btn-8 {
  background-color: #f0ecfc;
background-image: linear-gradient(315deg, #f0ecfc 0%, #c797eb 74%);
  line-height: 42px;
  padding: 0;
  border: none;
}
.btn-8 span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.btn-8:before,
.btn-8:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  background: #c797eb;
  /*box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);*/
  transition: all 0.3s ease;
}
.btn-8:before{
    height: 0%;
    width: 2px;
}
.btn-8:after {
  width: 0%;
  height: 2px;
}
.btn-8:hover:before {
  height: 100%;
}
.btn-8:hover:after {
  width: 100%;
}
.btn-8:hover{
  background: linear-gradient(315deg, #c797eb 0%, #f0ecfc 74%);
}
.btn-8 span:hover{
  color: #c797eb;
}
.btn-8 span:before,
.btn-8 span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  background: #c797eb;
  /*box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);*/
  transition: all 0.3s ease;
}
.btn-8 span:before {
  width: 2px;
  height: 0%;
}
.btn-8 span:after {
  height: 2px;
  width: 0%;
}
.btn-8 span:hover:before {
  height: 100%;
}
.btn-8 span:hover:after {
  width: 100%;
}
</style>
