<template>
  <div id="case">
    <h1>
      Case #{{ caseFile.id }} 
      <span v-if="caseFile.status_solved" class="badge solved">Solved!</span>
      <span v-else class="badge">Unsolved</span>
    </h1>
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
    <ul class="sub-nav no-list-style">
      <li v-for="subNav in subNavs"
        v-bind:class="{ 'active' : subNav.isActive }"
        v-on:click="toggleSubNav(subNav.name)">
        {{ subNav.name }}
      </li>
      
    </ul>
    <!-- TODO move leads to its own component -->
    <section class="subnav-section"
      v-bind:class="{ 'active' : activeSubNav === 'Leads' }">
      <h2>Leads</h2>
      
      <ul class="leads">
        <li v-for="lead in caseFile.leads">
          <div class="number">{{ lead.order }}</div>
          <div class="name">
            {{ lead.name }} <strong>{{ lead.location }}</strong>
            {{ lead.description }}
          </div>
        </li>
      </ul>
      <div class="panel">
        <label for="newLeadName">New lead name</label>
        <input v-model="newLeadName" name="newLeadName">
        <label for="newLeadPlace">New lead place</label>
        <input v-model="newLeadPlace" name="newLeadPlace">
        <label for="newLeadDesc">New lead description</label>
        <textarea v-model="newLeadDescription" name="newLeadDesc"></textarea>
        <label for="newLeadType">New lead type</label>
        <select v-model="newLeadType">
          <option disabled value="">Please select one</option>
          <option>Person</option>
          <option>Place</option>
          <option>Informant</option>
        </select>
        <br/>
        <button v-on:click="addLead">Add a lead</button>
      </div>
    </section>
    
    <clue-component
      v-bind:case-id="id"
      v-bind:active-sub-nav="activeSubNav" 
      v-bind:case-file="caseFile" />
    
    <section class="subnav-section"
      v-bind:class="{ 'active' : activeSubNav === 'Test' }">
      blah blah blah test
    </section>

    {{ caseFile }}
  </div>
</template>

<script>
import moment from 'moment'
import _ from 'lodash'
import ClueComponent from '@/components/Clue'

export default {
  name: 'CaseComponent',
  props: ['id'],
  components: {
    ClueComponent
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
        { name: 'Clues', isActive: false },
        { name: 'Test', isActive: false }
      ],
      activeSubNav: 'Leads'
    }
  },
  methods: {
    addLead: function (event) {
      let newLead = {}
      newLead.name = this.newLeadName
      newLead.order = this.caseFile.leads.length + 1
      newLead.location = this.newLeadPlace
      newLead.description = this.newLeadDescription
      newLead.lead_type = this.newLeadType
      newLead.case_id = this.caseFile.id

      this.$http.post('/api/lead', newLead).then(function (response) {
        this.caseFile.leads.push(newLead)
      }, function (error) {
        console.log('error posting new lead', error)
      })

      // reset form
      this.newLeadName = ''
      this.newLeadPlace = ''
      this.newLeadDescription = ''
      this.newLeadType = ''
    },
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
  }
}
</script>

<style scoped>
  ul.leads {
    text-align: left;
    list-style: none;
    margin: 20px 0;
    padding: 0;
  }
  ul.leads li {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 20px;
    position: relative;
  }
  ul.leads li:before{
    content: '';
    position: absolute;
    left: 14px;
    top: 30px;
    display: block;
    width: 2px;
    height: 100%;
    background: #2c3e50;
  }
  ul.leads li:last-child:before {
    background: none;
    display: none;
  }
  ul.leads li div {
    line-height: 30px;
  }
  ul.leads li div.number {
    background: #73BFB8;
    color: #2c3e50;
    width: 30px;
    min-width: 30px;
    height: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 12px;
    margin: 0 10px 0 0;

  }
</style>