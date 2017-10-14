<template>
  <div id="all_cases">
    <h1>Hi {{ name }},<br>here are all of your cases</h1>

    <ul class="no-list-style">
      <li v-for="caseFile in caseFiles.objects">
        <router-link :to="getRouterLink(caseFile.id)">
          <a>
            <span>{{ caseFile.id }} <strong>{{ caseFile.title }}</strong></span>
            <br>
            <span>{{ caseFile.description }}</span>
          </a>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'AllCases',
    data: function () {
      return {
        name: 'there',
        caseFiles: {}
      }
    },
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
      }
    },
    beforeMount: function () {
      this.getCases()
    }
  }
</script>

<style scoped>

</style>