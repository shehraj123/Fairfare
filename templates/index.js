import OSM from 'ol/source/OSM';
import TileLayer from 'ol/layer/Tile';
import {Map, View} from 'ol';
import {fromLonLat} from 'ol/proj';

// new Map({
//   target: "map",
//   layers: [
//     new TileLayer({
//       source: new OSM(),
//     }),
//   ],
//   view: new View({
//     center: fromLonLat([0, 0]),
//     zoom: 2,
//   }),
// });

var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');

mapboxgl.accessToken = 'pk.eyJ1IjoiZnJpZW5kbHliYWtlciIsImEiOiJja3lnZnE5dnkxMGt3MnJtazMzdzV2NXZsIn0.M1eGhDgpm4VzVswVRExBxQ';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11'
});