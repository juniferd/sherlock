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
</style>
