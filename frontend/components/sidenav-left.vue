<template>
  <v-navigation-drawer fixed v-model="state.drawer" app>
    <v-list dense>
      <v-list-item @click.stop="state.left = !state.left">
        <v-list-item-action>
          <v-icon>mdi-account</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Ver Meu Perfil</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['state']
}
</script>
