
$(document).ready( main );

var reportTimer = null;
var interval = 1500;

function main() {
    pollReports();
}

function pollReports() {
    reportTimer = setTimeout(function() {
        fetchReports();
        pollReports();
    }, interval);
}

function resetTimer() {
    clearTimeout(reportTimer);
}

function fetchReports() {
    $.ajax({
        url: '/api/reports/',
        type: 'GET',
        dataType: 'json'
    }).done(function(json) {
        for (var i = 0; i < json.length; i++) {
            var time = JSON.parse(json[i].location);
            createMarkers({lat: time[0], lng: time[1]}, map, json[i]);
        }
        // make data something useful
    }).fail(function(xhr, status, error) {
        console.log('Error: ', error);
        console.log('Status: ', status);
        console.dir(xhr);
    });
}
