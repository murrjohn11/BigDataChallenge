    function getRandomColors(){
        var letters = "0123456789ABCDEF";
        var color = "#";
        var colors = new Array();
        var i, j;

        for(i = 0; i < 12; i++){
            for(j = 0; j < 6; j++){
                color += letters[Math.floor(Math.random() * 16)];
            }
            colors[i] = color;
            color = "#";
        }

        return colors;
    }


$(document).ready(function() {

    var propertyTypes;
    var first = true;
    var options = {
        legend: {
            position: "bottom",
            labels: {
                padding: 20
            }
        }
    };
    var ctx = $("#pie");


        

    $("#HUMMS").click(function(){
        if(!first){
            propertyTypes.destroy();
        } else {
            first = false;
        }
        // data
        var colors = getRandomColors();
        var data = {
            labels: [
                "Mother Tongue",
                "Filipino",
                "English",
                "Mathematics",
                "Science",
                "Araling Panlipunan",
                "Edukasyon sa Pagpakatao",
                "Music",
                "Arts",
                "Physical Education",
                "Health",
                "Edukasyong Pantahanan at Pangkabuhayan"
            ],
            datasets: [
                {
                    data:[9, 9, 35, 9, 15, 9, 9, 1, 1, 1, 1, 1],
                    backgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ],
                    hoverBackgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ]
                }]

        };

        // Property Type Distribution
        propertyTypes = new Chart(ctx ,{
            type: 'pie',
            data: data,
            options: options
        });

    });

 $("#ABM").click(function(){
        if(!first){
            propertyTypes.destroy();
        } else {
            first = false;
        }
        // data
        var colors = getRandomColors();
        var data = {
            labels: [
                "Mother Tongue",
                "Filipino",
                "English",
                "Mathematics",
                "Science",
                "Araling Panlipunan",
                "Edukasyon sa Pagpakatao",
                "Music",
                "Arts",
                "Physical Education",
                "Health",
                "Edukasyong Pantahanan at Pangkabuhayan"
            ],
            datasets: [
                {
                    data:[0, 15, 15, 30, 15, 5, 5, 3, 3, 3, 3, 3],
                    backgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ],
                    hoverBackgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ]
                }]

        };

        // Property Type Distribution
        propertyTypes = new Chart(ctx ,{
            type: 'pie',
            data: data,
            options: options
        });

    });

    $("#STEM").click(function() {
        if(!first){
            propertyTypes.destroy();
        } else {
            first = false;
        }
        // data
        var colors = getRandomColors();
        var data = {
            labels: [
                "Mother Tongue",
                "Filipino",
                "English",
                "Mathematics",
                "Science",
                "Araling Panlipunan",
                "Edukasyon sa Pagpakatao",
                "Music",
                "Arts",
                "Physical Education",
                "Health",
                "Edukasyong Pantahanan at Pangkabuhayan"
            ],
            datasets: [
                {
                    data:[2, 5, 10, 30, 30, 5, 5, 2, 2, 2, 2, 5],
                    backgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ],
                    hoverBackgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ]
                }]

        };

        // Property Type Distribution
        propertyTypes = new Chart(ctx ,{
            type: 'pie',
            data: data,
            options: options
        });

    });

    $("#GAS").click(function() {
        if(!first){
            propertyTypes.destroy();
        } else {
            first = false;
        }
        // data
        var colors = getRandomColors();
        var data = {
            labels: [
                "Mother Tongue",
                "Filipino",
                "English",
                "Mathematics",
                "Science",
                "Araling Panlipunan",
                "Edukasyon sa Pagpakatao",
                "Music",
                "Arts",
                "Physical Education",
                "Health",
                "Edukasyong Pantahanan at Pangkabuhayan"
            ],
            datasets: [
                {
                    data:[5, 15, 15, 15, 15, 5, 5, 5, 5, 5, 5, 5],
                    backgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ],
                    hoverBackgroundColor: [
                        colors[0],
                        colors[1],
                        colors[2],
                        colors[3],
                        colors[4],
                        colors[5],
                        colors[6],
                        colors[7],
                        colors[8],
                        colors[9],
                        colors[10],
                        colors[11]
                    ]
                }]

        };

        // Property Type Distribution
        propertyTypes = new Chart(ctx ,{
            type: 'pie',
            data: data,
            options: options
        });

    });

});