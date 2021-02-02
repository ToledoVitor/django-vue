<template>
  <div>
    <timeline :jogos="jogos" />
  </div>
</template>

<script>

import timeline from '~/components/Timeline.vue'
// import newjogo from '~/components/Newjogo.vue' #TODO

export default {
  components: {
    timeline
  },
  props: ['jogos'],
  data () {
    return {}
  }
}
</script>

<style>
  .column_wrapper{
    column-count: 4;
  }
</style>
