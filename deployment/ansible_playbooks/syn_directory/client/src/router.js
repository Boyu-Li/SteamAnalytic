import Vue from 'vue'
import Router from 'vue-router'


//Components
import home from './components/home';
import gameDetail from './components/gameDetail';
import mapChart from './components/compareRecentTimeView';
import vicChart from './components/RecentTimeBarChartView';
import testMap from './components/testMap';
import testMapGameNum from './components/testMapGameNum';
import testMapRecentTime from './components/testMapRecentTime';
import testMapTotalTime from './components/testMapTotalTime';
import testMapReviewNum from './components/testMapReviewNum';
import GameNumBarChartView from './components/GameNumBarChartView';
import RecentTimeBarChartView from './components/RecentTimeBarChartView';
import ReviewNumChartView from './components/ReviewNumBarChartView';
import TotalTimeBarChartView from './components/TotalTimeBarChartView';
import compareTotalTimeView from './components/compareTotalTimeView';
import testMapSingle from './components/testMapSingle';
import testMapMulti from './components/testMapMulti';
import testMapSingleRecent from './components/testMapSingleRecent';
import testMapMultiRecent from './components/testMapMultiRecent';

Vue.use(Router)
 
export default new Router({
  routes: [
    { path: '/', name: 'home', component: home },
    { path: '/gameDetail/:id', name: 'gameDetail', component: gameDetail },
    { path: '/mapChart', name: 'mapChart', component: mapChart },
    { path: '/vicChart', name: 'vicChart', component: vicChart },
    { path: '/testMap', name: 'testMap', component: testMap },
    { path: '/testMapRecentTime', name: 'testMapRecentTime', component: testMapRecentTime },
    { path: '/testMapGameNum', name: 'testMapGameNum', component: testMapGameNum },
    { path: '/testMapTotalTime', name: 'testMapTotalTime', component: testMapTotalTime },
    { path: '/testMapReviewNum', name: 'testMapReviewNum', component: testMapReviewNum },
    { path: '/GameNumBarChartView', name: 'GameNumBarChartView', component: GameNumBarChartView },
    { path: '/RecentTimeBarChartView', name: 'RecentTimeBarChartView', component: RecentTimeBarChartView },
    { path: '/ReviewNumChartView', name: 'ReviewNumChartView', component: ReviewNumChartView },
    { path: '/TotalTimeBarChartView', name: 'TotalTimeBarChartView', component: TotalTimeBarChartView },
    { path: '/compareTotalTimeView', name: 'compareTotalTimeView', component: compareTotalTimeView },
    { path: '/testMapSingle', name: 'testMapSingle', component: testMapSingle },
    { path: '/testMapMulti', name: 'testMapMulti', component: testMapMulti },
    { path: '/testMapSingleRecent', name: 'testMapSingleRecent', component: testMapSingleRecent },
    { path: '/testMapMultiRecent', name: 'testMapMultiRecent', component: testMapMultiRecent },
  ]
})
