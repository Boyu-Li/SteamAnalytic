
<template>
    <div>
  
    <div class="display-3" style ="color:green">Review Number Analysis</div>
    <v-row>
      <v-col>
      <router-link to ="/testMap" tag="p"><v-btn text class = "title" style ="color:red">Australian User</v-btn></router-link>
       <router-link to ="/testMapRecentTime" tag="p"><v-btn text class = "title" style ="color:red">Recent time</v-btn></router-link>
        <router-link to ="/testMapReviewNum" tag="p"><v-btn text class = "title" style ="color:red">Review number</v-btn></router-link>
         <router-link to ="/testMapTotalTime" tag="p"><v-btn text class = "title" style ="color:red">Total played time</v-btn></router-link>
          <router-link to ="/testMapSingle" tag="p"><v-btn text class = "title" style ="color:red">Single total time</v-btn></router-link>
           <router-link to ="/testMapMulti" tag="p"><v-btn text class = "title" style ="color:red">multiple total time</v-btn></router-link>
           <router-link to ="/testMapSingleRecent" tag="p"><v-btn text class = "title" style ="color:red">Single Recent time</v-btn></router-link>
           <router-link to ="/testMapMultiRecent" tag="p"><v-btn text class = "title" style ="color:red">multiple Recent time</v-btn></router-link>
      </v-col>
     <div class="hello" ref="chartdiv"> </div>
    </v-row>
       
     </div>
</template>
<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4geodata_australiaLow from "@amcharts/amcharts4-geodata/australiaLow"

am4core.useTheme(am4themes_animated);
export default {
    data: function(){
    return{
        ACTUser:"",
        NSWUser:"",
        NTUser:"",
        QLDUser:"",
        SAUser:"",
        TASUser:"",
        VICUser:"",
        WAUser:""


    }
    },
     mounted() {
           this.$axios({method:"GET", url:"http://localhost:3000/gameDistribute"
    }).then(response => {this.info = response.data
    var i;
   //response.data.data.rows
    this.ACTUser = this.info.ACT.review_num
    this.NSWUser = this.info.NSW.review_num
    this.NTUser = this.info.NT.review_num
    this.QLDUser = this.info.QLD.review_num
    this.SAUser = this.info.SA.review_num
    this.TASUser = this.info.TAS.review_num
    this.VICUser = this.info.VIC.review_num
    this.WAUser = this.info.WA.review_num
    let map = am4core.create(this.$refs.chartdiv, am4maps.MapChart);
    map.geodata = am4geodata_australiaLow;
    map.projection = new am4maps.projections.Miller()
    var polygonSeries = map.series.push(new am4maps.MapPolygonSeries())
    polygonSeries.useGeodata = true
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}: {value}";
    polygonTemplate.fill = am4core.color("#74B266");

    // Create hover state and set alternative fill color
    var hs = polygonTemplate.states.create("hover");
    hs.properties.fill = am4core.color("#41ab5d");

    // Add heat rule
    polygonSeries.heatRules.push({
    "property": "fill",
    "target": polygonSeries.mapPolygons.template,
    "min": am4core.color("#deebf7"),
    "max": am4core.color("#08306b")
});



polygonSeries.data = [
    { id: "AU-NT", value: this.NTUser },
    { id: "AU-WA", value: this.WAUser },
    { id: "AU-ACT", value: this.ACTUser },
    { id: "AU-NSW", value: this.NSWUser },
    { id: "AU-SA", value: this.SAUser },
    { id: "AU-VIC", value: this.VICUser },
    { id: "AU-TAS", value: this.TASUser },
    { id: "AU-QLD", value: this.QLDUser },
       
  ]
       
        
    });
    
   
     
  },
  beforeDestroy() {
    if (this.map) {
      this.map.dispose()
    }
  }
    

    


}
</script>
<style scoped>
.hello {
  width: 900px;
  height: 600px;
}
</style>