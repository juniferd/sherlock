<template>
  <ul id="sidebar">
    <li v-for="item in items">
      <router-link :to="item.route">
        <a>
          {{ item.title | capitalize }}
        </a>
      </router-link>
    </li>
  </ul>
</template>

<script>
  import Filters from '../Filters.js'
  export default {
    name: 'Sidebar',
    filters: Filters,
    data () {
      return {
        items: [
          {
            title: 'all cases',
            route: '/'
          }
          // {
          //   title: 'timeline',
          //   route: '/timeline'
          // },
          // {
          //   title: 'leads',
          //   route: '/leads'
          // }
        ]
      }
    }
  }
</script>

<style scoped>
ul#sidebar {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 200px;
  margin: 0;
  padding: 0;
  background: #eee;
  text-align: left;
}
ul#sidebar li {  
  list-style: none;
  margin: 0;
  padding: 0;
}
ul#sidebar li a {
  padding: 10px;
  margin: 0;
  display: block;
  text-decoration: none;
  color: #73BFB8;
}
ul#sidebar li a.router-link-exact-active,
ul#sidebar li a.router-link-exact-active a {
  background: #73BFB8;
  color: #fff;
}
ul#sidebar li a:hover,
ul#sidebar li a.router-link-exact-active:hover a{
  background: #99D0CB;
  color: #fff;
}
</style>