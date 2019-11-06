<template>
  <MglMap :accessToken="accessToken" 
          :mapStyle="mapStyle" 
          style="position: absolute; top: 0px; bottom : 0px; height: 800px; swidth:100%" />

</template>

<script>
import Mapbox from "mapbox-gl";
import { MglMap } from "vue-mapbox";

export default {
  components: {
    MglMap
  },
  data() {
    return {
      accessToken: "pk.eyJ1IjoieWltaW5nejEyIiwiYSI6ImNrMXg1ZzR2ZTA3d2Qzb21nNjBoOHc0aHMifQ.VbjXJ4tIKL0cZm8u5h-0Ww", // your access token. Needed if you using Mapbox maps
      mapStyle: "mapbox://styles/yimingz12/ck1ypbz92353k1cpiep33jzx7" // your map style
    };
  },

  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
  }
};
</script>