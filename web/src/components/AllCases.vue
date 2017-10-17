<template>
  <div id="all_cases">
    <h1>Hi {{ name }},<br>here are all of your cases</h1>

    <ul class="no-list-style">
      <li v-for="caseFile in caseFiles.objects">
        <router-link :to="getRouterLink(caseFile.id)">
          <a>
            <span>{{ caseFile.id }} <strong>{{ caseFile.title }}</strong></span>
            <br>
            <span>{{ caseFile.description | truncate(50) }}</span>
          </a>
        </router-link>
      </li>
    </ul>
    <button v-on:click="addCase">Add a case</button>
  </div>
</template>

<script>
  import Filters from '../Filters'

  export default {
    name: 'AllCases',
    data: function () {
      return {
        name: 'there',
        caseFiles: {}
      }
    },
    filters: Filters,
    methods: {
      getCases: function () {
        this.$http.get('/api/casefile').then(function (response) {
          this.caseFiles = response.data
        }, function (error) {
          console.log('error fetching casefiles', error)
        })
      },
      getRouterLink: function (id) {
        return '/case/' + id
      },
      addCase: function () {
        let params = {
          title: 'My new case',
          description: '',
          status_solved: false
        }
        this.$http.post('/api/casefile', params).then(function (response) {
          this.getCases()
        }, function (error) {
          console.log('error adding case', error)
        })
      }
    },
    beforeMount: function () {
      this.getCases()
    }
  }
</script>

<style scoped>

</style>