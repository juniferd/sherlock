import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import CaseComponent from '@/components/Case'
import TimelineComponent from '@/components/Timeline'
import Sidebar from '@/components/Sidebar'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
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
