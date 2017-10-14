import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import CaseComponent from '@/components/Case'
import TimelineComponent from '@/components/Timeline'
import Sidebar from '@/components/Sidebar'
import AllCases from '@/components/AllCases'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      components: { default: AllCases, sidebar: Sidebar },
      props: { default: true, sidebar: true }
    },
    {
      path: '/case/:id',
      name: 'Case',
      components: { default: CaseComponent, sidebar: Sidebar },
      props: { default: true, sidebar: true }
    },
    {
      path: '/timeline',
      name: 'Timeline',
      component: TimelineComponent,
      props: true
    },
    {
      path: '/leads',
      name: 'Leads',
      component: TimelineComponent,
      props: true
    }
  ]
})
