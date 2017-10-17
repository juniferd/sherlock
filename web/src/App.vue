<template>
  <div id="app">
    <sidebar/>
    <div id="main_content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'

export default {
  name: 'app',
  components: {
    Sidebar
  }
}
</script>

<style>
body {
  padding: 0;
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px 0;
}
#main_content {
  margin: 0 20px 0 220px;
}
h1, h2, h3, h4, h5, p {
  text-align: left;
}
input {
  margin: 0 0 20px;
  border: none;
  border-bottom: 1px solid #3A8AD3;
  font-size: 1.5em;
  display: block;
  width: 100%;
  background-color: transparent;
}

textarea {
  margin: 0 0 20px;
  border: none;
  border-bottom: 1px solid #3A8AD3;
  font-size: 1.5em;
  display: block;
  width: 100%;
  background-color: transparent;
}
label {
  font-size: 1em;
  display: block;
  text-align: left;
}
select {
  margin: 0 0 20px;
}
.panel {
  background: #eee;
  padding: 20px;
}
button {
  padding: 10px;
  border: none;
  background: #3A8AD3;
  color: #fff;
  border-radius: 5px;
  font-weight: bold;
  margin: 0 auto;
}
button:hover {
  cursor: pointer;
  background: #84C4E4;
}
ul.no-list-style {
  list-style: none;
  text-align: left;
  padding: 0;
  margin: 0;
}
ul.no-list-style li {
  margin-bottom: 20px;
}
.badge {
  background: #ccc;
  color: #fff;
  padding: 5px;
  font-size: .75em;
}
.badge.solved {
  background: #12938C;
}
.switch {
  position: relative;
  width: 60px;
  height: 34px;
}
.switch input {
  display: none;
}
.switch .slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  border-radius: 17px;
  -webkit-transition: .4s;
  transition: .4s;
}
.switch .slider:before {
  position: absolute;
  content: '';
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: #fff;
  border-radius: 13px;
  -webkit-transition: .4s;
  transition: .4s;
}
.switch input:checked + .slider {
  background-color: #3a8ad3;
}
.switch input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}
</style>
