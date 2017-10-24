<template>
  <section class="subnav-section"
    id="suspect_component"
    v-bind:class="{ 'active' : activeSubNav === 'Suspects' }">
    <h2>Suspects</h2>
    <p> {{ test }}</p>
  </section>
</template>

<script>
export default {
  name: 'SuspectComponent',
  props: ['caseId', 'activeSubNav', 'caseFile'],
  data: function () {
    return {
      test: 'test test' + this.caseId
    }
  },
  methods: {
    addSuspect: function (event) {
      return event
    }
  }
}
</script>

<style scoped>

</style>