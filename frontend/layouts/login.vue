<template>
  <html>
    <v-app id="inspire">
      <v-content>
        <v-container style="padding: 0;" fluid>
          <nuxt />
        </v-container>
      </v-content>
      <le-footer />
    </v-app>
  </html>
</template>

<script>
import footer from '~/components/footer.vue'
export default {
  components: {
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: true
    }
  }),
  computed: {
    snack () {
      return JSON.parse(JSON.stringify(this.$store.state.snack.snack))
    }
  },
  methods: {
    closeSnack () {
      this.$store.commit('snack/hide')
    }
  }
}
</script>

<style>
</style>
