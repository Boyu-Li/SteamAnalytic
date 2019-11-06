<template><div>
    <div id="chart">
      <apexchart type=area height=350 :options="chartOptions" :series="series" />
    </div>
          </div>
</template>

<script>
export default {
         props: ['Ararat','Ballarat','Benalla','Bendigo','Colac','Geelong','Horsham','Lara','Melbourne','Melton','Mildura','Wangaratta','Warrnambool','Wodonga','AraratSleep','BallaratSleep','BenallaSleep','BendigoSleep','ColacSleep','GeelongSleep','HorshamSleep','LaraSleep','MelbourneSleep','MeltonSleep','MilduraSleep','WangarattaSleep','WarrnamboolSleep','WodongaSleep'],
       data: function() {
      return {
        series: [{
          name: 'Recent Game Time',
          data: [this.Ararat,this.Ballarat,this.Benalla,this.Bendigo,this.Colac,this.Geelong,this.Horsham,this.Lara,this.Melbourne,this.Melton,this.Mildura,this.Wangaratta,this.Warrnambool,this.Wodonga]
        }, {
          name: 'Aurin Sleep Time',
          data: [this.AraratSleep,this.BallaratSleep,this.BenallaSleep,this.BendigoSleep,this.ColacSleep,this.GeelongSleep,this.HorshamSleep,this.LaraSleep,this.MelbourneSleep,this.MeltonSleep,this.MilduraSleep,this.WangarattaSleep,this.WarrnamboolSleep,this.WodongaSleep]
        }],
        chartOptions: {
          dataLabels: {
            enabled: false
          },
          stroke: {
            curve: 'smooth'
          },


          xaxis: {
            categories: ['Ararat','Ballarat','Benalla','Bendigo','Colac','Geelong','Horsham','Lara','Melbourne','Melton','Mildura','Wangaratta','Warrnambool','Wodonga'],
          },
          tooltip: {
           

          }
        }

      }

       }
}
  
</script>