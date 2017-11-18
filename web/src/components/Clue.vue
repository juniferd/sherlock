<template>
  <section class="subnav-section"
    id="clue_component"
    v-bind:class="{ 'active' : activeSubNav === 'Clues'}">
    <h2>Clues</h2>
    <p class="align-left">
      Sort by <select class="align-left"
        v-model.lazy="clueSortBy"
        v-on:change="changeClueSort"
        placeholder="Sort clues by">
        <option v-for="item in clueSorts">{{ item }}</option>
      </select>
    </p>
    <ul>
      <li class="clue" v-for="clue in caseFile.clues">
        <p class="no-margin"><strong>{{ clue.title }}</strong></p>
        <p class="no-margin">{{ clue.description }}</p>
        <p class="no-margin">Source: {{ clue.clue_source }}</p>
        <p class="no-margin">Type: {{ clue.clue_type }}</p>
        <p class="no-margin" v-if="clue.date_started">Date started: {{ clue.date_started }}</p>
        <p class="no-margin" v-if="clue.date_ended">Date ended: {{ clue.date_ended }}</p>
      </li>
    </ul>

    <div class="panel width-50 align-left">
      <label for="newClueTitle">New clue name</label>
      <input v-model="newClue.title" name="newClueTitle">

      <label for="newClueDescription">Description</label>
      <textarea v-model="newClue.description" name="newClueDescription"></textarea>

      <label for="newClueType">Clue type</label>
      <!-- <select v-model="newClue.clue_type">
        <option disabled value="">Please select one</option>
        <option>Direct</option>
        <option>Hearsay</option>
        <option>Circumstantial</option>
        <option>Other</option>
      </select> -->
      <v-select v-model="newClue.clue_type" :options="options"></v-select>
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
import _ from 'lodash'
import vSelect from 'vue-select'
export default {
  name: 'ClueComponent',
  props: ['caseId', 'activeSubNav', 'caseFile'],
  components: {
    vSelect
  },
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
      },
      clueSortBy: 'id',
      clueSorts: ['title', 'type', 'source', 'id'],
      options: ['Direct', 'Hearsay', 'Circumstantial', 'Other']
    }
  },
  methods: {
    addClue: function (event) {
      let thisClue = _.clone(this.newClue)
      this.$http.post('/api/clue', thisClue).then(function (response) {
        console.log('yay success clues', thisClue)
        this.caseFile.clues.push(thisClue)
      }, function (error) {
        console.log('error posting new clue', error)
      }).finally(function () {
        this.resetClueForm()
      })
    },
    resetClueForm: function () {
      this.newClue.title = ''
      this.newClue.description = ''
      this.newClue.clue_type = ''
      this.newClue.clue_source = ''
      this.newClue.date_started = null
      this.newClue.date_ended = null
    },
    changeClueSort: function (event) {
      console.log('>>>>>', this.clueSortBy)
      let clues = this.caseFile.clues

      switch (this.clueSortBy) {
        case 'title':
          clues.sort(function (a, b) {
            if (a.title < b.title) {
              return -1
            }
            if (a.title > b.title) {
              return 1
            }
            return 0
          })
          break
        case 'type':
          clues.sort(function (a, b) {
            if (a.clue_type < b.clue_type) {
              return -1
            }
            if (a.clue_type > b.clue_type) {
              return 1
            }
            return 0
          })
          break
        case 'source':
          clues.sort(function (a, b) {
            if (a.clue_source < b.clue_source) {
              return -1
            }
            if (a.clue_source > b.clue_source) {
              return 1
            }
            return 0
          })
          break
        default:
          clues.sort(function (a, b) {
            return a.id - b.id
          })
      }
    }
  },
  computed: {
    clueSortBy: {
      get () {
        return null
      },
      set (optionValue) {
        this.clueSorts = this.clueSorts.filter(function (o) {
          return o !== optionValue
        })
      }
    }
  }
}
</script>

<style scoped>
ul li.clue {
  text-align: left;
  margin-bottom: 20px;
}
p.no-margin {
  margin: 0;
}
p.align-left {
  text-align: left;
}
select.align-left {
  margin: 0;
  text-align: left;
  display: inline;
}
</style>