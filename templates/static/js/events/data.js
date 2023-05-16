import { Map } from "../map/map.js";
import { Urls } from "../helpers/urls.js";

const eventId = window.location.href.match(/\/(\d+)\/?$/)[1];
const url_api = Urls.events + eventId;

let arr = []

fetch(url_api)
.then(res => res.json())
.then(data => {

    let map = new Map();
    map.setMap(data.coordinates.lat, data.coordinates.lng);
    data.routes_data.forEach((e) => {
        arr.push(e.route)
    })
    map.addRoutes(arr, 0)
    map.addPointsEvent(data.points)
    map.setButtons(arr);
    // map.changeOpacity(arr) //'3007668662019916668'
})