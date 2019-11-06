<template>
<div id = "mapView">
 
<AusMap></AusMap>
  
</div>
</template>

<script>
import AusMap from './mapBoxChart.vue'
export default {
  name: 'mapView',
  props: ['mapView'],
  components: {
  AusMap
  },
  
  data: function(){
    return{
    
    }
    },
    
};



</script>

