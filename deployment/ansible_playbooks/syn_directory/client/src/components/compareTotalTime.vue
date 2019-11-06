<template><div>
    <div id="chart">
      <apexchart type=line height=350 :options="chartOptions" :series="series" />
    </div>
          </div>
</template>

<script>
export default {
         props: ['Ararat','Ballarat','Benalla','Bendigo','Colac','Geelong','Horsham','Lara','Melbourne','Melton','Mildura','Wangaratta','Warrnambool','Wodonga','AraratSleep','BallaratSleep','BenallaSleep','BendigoSleep','ColacSleep','GeelongSleep','HorshamSleep','LaraSleep','MelbourneSleep','MeltonSleep','MilduraSleep','WangarattaSleep','WarrnamboolSleep','WodongaSleep','AraratTotal','BallaratTotal','BenallaTotal','BendigoTotal','ColacTotal','GeelongTotal','HorshamTotal','LaraTotal','MelbourneTotal','MeltonTotal','MilduraTotal','WangarattaTotal','WarrnamboolTotal','WodongaTotal'],
       data: function() {
      return {
        series: [{
            name: 'Recent Game Time',
          data: [this.Ararat,this.Ballarat,this.Benalla,this.Bendigo,this.Colac,this.Geelong,this.Horsham,this.Lara,this.Melbourne,this.Melton,this.Mildura,this.Wangaratta,this.Warrnambool,this.Wodonga]
        }, {
          name: 'Aurin Sleep Time',
          data: [this.AraratSleep,this.BallaratSleep,this.BenallaSleep,this.BendigoSleep,this.ColacSleep,this.GeelongSleep,this.HorshamSleep,this.LaraSleep,this.MelbourneSleep,this.MeltonSleep,this.MilduraSleep,this.WangarattaSleep,this.WarrnamboolSleep,this.WodongaSleep]
        },
        {name: 'Total Game Time',
          data: [this.AraratTotal,this.BallaratTotal,this.BenallaTotal,this.BendigoTotal,this.ColacTotal,this.GeelongTotal,this.HorshamTotal,this.LaraTotal,this.MelbourneTotal,this.MeltonTotal,this.MilduraTotal,this.WangarattaTotal,this.WarrnamboolTotal,this.WodongaTotal]
        }],
      
        chartOptions: {
          chart: {
                height: 350,
                zoom: {
                    enabled: false
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'straight'
            },
            grid: {
                row: {
                    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.5
                },
            },
            xaxis: {
            categories: ['Ararat','Ballarat','Benalla','Bendigo','Colac','Geelong','Horsham','Lara','Melbourne','Melton','Mildura','Wangaratta','Warrnambool','Wodonga'],
            }
        }
      }
       }
}
      
  
  
</script>