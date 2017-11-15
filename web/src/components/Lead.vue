<template>
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
      <label>New lead name</label>
      <input v-model="newLead.name">
      <label>Place</label>
      <input v-model="newLead.location">
      <label>Description</label>
      <textarea v-model="newLead.description"></textarea>
      <label>New lead type</label>
      <v-select v-model="newLead.lead_type" :options="options"></v-select>
      <br/>
      <button v-on:click="addLead">Add a lead</button>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import vSelect from 'vue-select'

export default {
  name: 'LeadComponent',
  props: ['caseId', 'activeSubNav', 'caseFile'],
  components: {
    vSelect
  },
  data: function () {
    return {
      newLead: {
        name: '',
        location: '',
        description: '',
        lead_type: 'Person',
        case_id: this.caseId
      },
      options: ['Person', 'Place', 'Informant']
    }
  },
  methods: {
    addLead: function (event) {
      let thisLead
      this.newLead.order = this.caseFile.leads.length + 1

      thisLead = _.clone(this.newLead)

      this.$http.post('/api/lead', this.newLead).then(function (response) {
        this.caseFile.leads.push(thisLead)
      }, function (error) {
        console.log('error posting new lead', error)
      }).finally(function () {
        // reset form
        this.resetLeadForm()
      })
    },
    resetLeadForm: function () {
      this.newLead.name = ''
      this.newLead.location = ''
      this.newLead.description = ''
      this.newLead.lead_type = 'Person'
    }
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