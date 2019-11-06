<script src='https://api.mapbox.com/mapbox-gl-js/v1.4.1/mapbox-gl.js'></script>
<template>
<div>
  <MglMap :accessToken="accessToken" 
          :mapStyle="mapStyle" 
          style="position: absolute; top: 0px; bottom : 0px; height: 800px; swidth:100%" />
          <div id='map'></div>
          <div class='map-overlay' id='features'>
          <h2>Au Player density</h2><div id='pd'>
          <p>Hover over a state!</p>
          </div></div>
          <div class='map-overlay' id='legend'></div>

</div>
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
      mapStyle: "mapbox://styles/yimingz12/ck2463cdg1jip1cp62kop4qil" // your map style
    };
  },

  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
  },
  
  
};
</script>
<style scoped>
body {
  margin: 0;
  padding: 0;
}

h2,
h3 {
  margin: 10px;
  font-size: 1.2em;
}

h3 {
  font-size: 1em;
}

p {
  font-size: 0.85em;
  margin: 10px;
  text-align: left;
}

/**
* Create a position for the map
* on the page */
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}

/**
* Set rules for how the map overlays
* (information box and legend) will be displayed
* on the page. */
.map-overlay {
  position: absolute;
  bottom: 0;
  right: 0;
  background: rgba(255, 255, 255, 0.8);
  margin-right: 20px;
  font-family: Arial, sans-serif;
  overflow: auto;
  border-radius: 3px;
}

#features {
  top: 0;
  height: 100px;
  margin-top: 20px;
  width: 250px;
}

#legend {
  padding: 10px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  line-height: 18px;
  height: 150px;
  margin-bottom: 40px;
  width: 100px;
}

.legend-key {
  display: inline-block;
  border-radius: 20%;
  width: 10px;
  height: 10px;
  margin-right: 5px;
}
</style>