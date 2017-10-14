<template>
  <div id="case">
    <h1>Case #{{ $route.params.id }}</h1>
    <label for="name">Case name</label>
    <input v-model="name" name="name" placeholder="case name">
    <br/>
    <label for="description">Case description</label>
    <textarea v-model="description" name="description" placeholder="description"></textarea>
    
    <h2>Leads</h2>
    
    <ul class="leads">
      <li v-for="lead in leads">
        <div class="number">{{ lead.id }}</div>
        <div class="name">
          {{ lead.name }} <strong>{{ lead.place }}</strong>
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
      <button v-on:click="addLead">Add a lead</button>
    </div>

    <p>case name: {{ name }}</p>
    <p>case description: {{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'CaseComponent',
  props: ['id'],
  data: function () {
    return {
      name: '',
      description: '',
      leads: [],
      newLeadName: '',
      newLeadPlace: '',
      newLeadDescription: ''
    }
  },
  methods: {
    addLead: function (event) {
      let newLead = {}
      newLead.name = this.newLeadName
      newLead.id = this.leads.length + 1
      newLead.place = this.newLeadPlace
      newLead.description = this.newLeadDescription
      this.leads.push(newLead)
      // reset form
      this.newLeadName = ''
      this.newLeadPlace = ''
      this.newLeadDescription = ''
      // TODO: post here to add lead to db
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
    height: 20px;
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
    height: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 12px;
    margin: 0 10px 0 0;

  }
</style>