<template>
   <div class="chart-wrap">
        <div id="chart">
          <apexchart type=donut width=500 :options="chartOptions" :series="series" />
        <div>{{gamePos}}</div>
           <div>{{gameNeg}}</div>
        </div>
   </div>
        
</template>

<script>
export default {
   props: ['gamePos','gameNeg'],
    data: function() {
      return {
       
       series: [this.gamePos,this.gameNeg],
       
        chartOptions: {
          labels:['positive comment','negative comment'],

          responsive: [{
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                show: false
              }
            }
          }],
          legend: {
              position: 'right',
              offsetY: 0,
              height: 230,
          }
        }
      }
    }, methods: {
   
    }
};
</script>