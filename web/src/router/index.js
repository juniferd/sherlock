import Vue from 'vue'
import Router from 'vue-router'

import TimelineComponent from '@/components/Timeline'
import Sidebar from '@/components/Sidebar'

import CaseComponent from '@/components/Case'

const AllCases = () => import(/* webpackChunkName: "all-cases-component" */ '@/components/AllCases')
const LeadComponent = () => import(/* webpackChunkName: "lead-component" */ '@/components/Lead')
const ClueComponent = () => import(/* webpackChunkName: "clue-component" */ '@/components/Clue')
// const SuspectComponent = () => import(/* webpackChunkName: "suspect-component" */ '@/components/Suspect')

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
      components: {
        default: CaseComponent,
        sidebar: Sidebar,
        clue: ClueComponent,
        lead: LeadComponent
      },
      props: {
        default: true,
        sidebar: true,
        clue: true
      }
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
