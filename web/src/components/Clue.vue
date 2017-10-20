<template>
  <section class="subnav-section"
    id="clue_component"
    v-bind:class="{ 'active' : activeSubNav === 'Clues'}">
    <h2>Clues</h2>
    <p> {{ test}} </p>
    <ul class="clue-type clue-direct">
      <li v-for="clue in caseFile.clues">
        {{ clue }}
      </li>
    </ul>
    <ul class="clue-type clue-hearsay">

    </ul>
    <ul class="clue-type clue-circumstantial">

    </ul>
    <ul class="clue-type clue-other">

    </ul>

    <div class="panel">
      <label for="newClueTitle">New clue name</label>
      <input v-model="newClue.title" name="newClueTitle">

      <label for="newClueDescription">Description</label>
      <textarea v-model="newClue.description" name="newClueDescription"></textarea>

      <label for="newClueType">Clue type</label>
      <select v-model="newClue.clue_type">
        <option disabled value="">Please select one</option>
        <option>Direct</option>
        <option>Hearsay</option>
        <option>Circumstantial</option>
        <option>Other</option>
      </select>

      <label for="newClueSource">Clue source</label>
      <input v-model="newClue.clue_source">

      <label>Date started</label>
      <input v-model="newClue.date_started">

      <label>Date ended</label>
      <input v-model="newClue.date_ended">
      <!-- TODO add suspects? -->
      <br/>
      <button v-on:click="addClue">Add a clue</button>
    </div>

  </section>
</template>

<script>

export default {
  name: 'ClueComponent',
  props: ['caseId', 'activeSubNav', 'caseFile'],
  data: function () {
    return {
      test: 'hi there' + this.caseId,
      newClue: {
        title: '',
        description: '',
        clue_type: '',
        clue_source: '',
        date_started: null,
        date_ended: null,
        case_id: this.caseId
      }
    }
  },
  methods: {
    addClue: function (event) {
      this.$http.post('/api/clue', this.newClue).then(function (response) {
        console.log('yay success clues', this.newClue)
        this.caseFile.clues.push(this.newClue)
      }, function (error) {
        console.log('error posting new clue', error)
      })
    }
  }
}
</script>

<style scoped>
</style>