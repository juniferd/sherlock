<template>
  <div id="case">
    <div class="sticky-header" v-sticky="{ zIndex: 10, stickyTop: 0 }">
      <div>
        <h1>
          Case #{{ caseFile.id }}
          <span v-if="caseFile.status_solved" class="badge solved">Solved!</span>
          <span v-else class="badge">Unsolved</span>
          {{ caseFile.title }}
        </h1>
      </div>
    </div>
    <p>Last updated {{ getDate(caseFile.date_updated) }}</p>
    <label for="name">Case name</label>
    <input v-model="caseFile.title" name="name" placeholder="case name">
    <br/>
    <label for="description">Case description</label>
    <textarea v-model="caseFile.description" name="description" placeholder="description"></textarea>
    <label>Case status</label>
    <div class="switch" v-on:click="caseFile.status_solved = !caseFile.status_solved">
      <input type="checkbox" v-model="caseFile.status_solved">
      <span class="slider"></span>
    </div>
    <br/>
    <div v-show="caseFile.status_solved">
      <label>Points</label>
      <input v-model="caseFile.points">
    </div>
    <br/>
    <button v-on:click="updateCaseFile">Save changes</button>
    <!-- subnav here for LEADS, CLUES, SUSPECTS, TIMELINE -->
    <div class="sticky-header" v-sticky="{ zIndex: 9, stickyTop: 40}">
      <div>
        <ul class="sub-nav no-list-style">
          <li v-for="subNav in subNavs"
            v-bind:class="{ 'active' : subNav.isActive }"
            v-on:click="toggleSubNav(subNav.name)">
            {{ subNav.name }}
          </li>
        </ul>
      </div>
    </div>
    <lead-component
      v-bind:case-id="id"
      v-bind:active-sub-nav="activeSubNav"
      v-bind:case-file="caseFile"/>
    
    <clue-component
      v-bind:case-id="id"
      v-bind:active-sub-nav="activeSubNav" 
      v-bind:case-file="caseFile" />
    
   <!--  <suspect-component
      v-bind:case-id="id"
      v-bind:active-sub-nav="activeSubNav"
      v-bind:case-file="caseFile" /> -->

  </div>
</template>

<script>
import moment from 'moment'
import _ from 'lodash'
import VueSticky from 'vue-sticky'

import ClueComponent from '@/components/Clue'
import LeadComponent from '@/components/Lead'
// import SuspectComponent from '@/components/Suspect'

export default {
  name: 'CaseComponent',
  props: ['id'],
  components: {
    ClueComponent,
    LeadComponent
  },
  data: function () {
    return {
      leads: [],
      newLeadName: '',
      newLeadPlace: '',
      newLeadDescription: '',
      newLeadType: '',
      caseFile: {},
      subNavs: [
        { name: 'Leads', isActive: true },
        { name: 'Clues', isActive: false }
      ],
      activeSubNav: 'Leads'
    }
  },
  methods: {
    updateCaseFile: function (event) {
      let thisCaseFile = _.omit(this.caseFile, 'leads')

      this.$http.put('/api/casefile/' + this.caseFile.id, thisCaseFile).then(function (response) {
        console.log('successfully updated case file', response)
      }, function (error) {
        console.log('error posting casefile', error)
      })
    },
    getCase: function (id) {
      this.$http.get('/api/casefile/' + id).then(function (response) {
        this.caseFile = response.data
      }, function (error) {
        console.log('error fetching casefile', error)
      })
    },
    getDate: function (dateTime) {
      return moment(dateTime).format('DD MMM YYYY, h:mm:ss a')
    },
    toggleSubNav: function (name) {
      _.forEach(this.subNavs, function (subNav) {
        subNav.isActive = subNav.name === name
      })
      this.activeSubNav = name
    }
  },
  beforeMount: function () {
    this.getCase(this.id)
  },
  directives: {
    'sticky': VueSticky
  }
}
</script>

<style scoped>
  .sticky-header {
    background: #ffffff;
    padding: 0;
  }
  .sticky-header h1 {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    max-height: 1.5em;
    text-overflow: ellipsis;
    overflow: hidden;
    margin: 5px 0;
  }
  .sticky-header ul {
    margin: 0;
  }
</style>
