<template>
    <v-app-bar
      color="#fcb69f"
      dark
      shrink-on-scroll
      src="https://i.imgur.com/j0uabqx.png"
      style="width:100%;height:100%;"
      scroll-target="#scrolling-techniques-2"
    >
     
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(0,0,0,.9), rgba(108, 230, 232,.1)"
        ></v-img>
      </template>


      <v-toolbar-title>Steam Australian User Analysis
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-toolbar-items>
        <router-link to ="/" tag="p"><v-btn text class = "title">Home</v-btn></router-link>
        <router-link to ="/compareTotalTimeView" tag="p"><v-btn text class = "title">AURIN Comparison</v-btn></router-link>
        <router-link to ="/vicChart" tag="p"><v-btn text class = "title">Victoria Analysis</v-btn></router-link>
         <router-link to ="/testMap" tag="p"><v-btn text class = "title">General Analysis</v-btn></router-link>
      </v-toolbar-items>
      <div class="flex-grow-1"></div>

    </v-app-bar>
    
</template>
