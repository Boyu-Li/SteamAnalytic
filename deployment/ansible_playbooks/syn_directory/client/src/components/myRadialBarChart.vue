<template>
<div class="chart-wrap">
    <div id="chart">
      <apexchart type=bar height=350 :options="chartOptions" :series="series" />
     <div>{{gameTotal}}</div>
     <div>{{gameAuPlayer}}</div>
     <div>{{gameRecent}}</div>
     <div>asdasd</div>
    </div>
    
    </div>
   
</template>

<script>
export default {
   props: ['gameAuPlayer','gameTotal','gameRecent'],
    data: function() {
        return{
        series: [{data:[this.gameTotal,this.gameAuPlayer,this.gameRecent ]}],
        chartOptions: {
          plotOptions: {
            bar: {
              horizontal: true,
            }
              },
              dataLabels: {
                enabled: false
              },
               xaxis: {
            categories: ['Global Player', 'Australian Player', '3 hours Recent Player'],
          }
        }
        }
    }
      
};
</script>