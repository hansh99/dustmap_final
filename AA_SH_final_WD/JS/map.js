    var width = 800,
        height = 800;

    var svg = d3.select("#chart").append("svg")
        .attr("width", width)
        .attr("height", height);

    var map = svg.append("g").attr("id", "map"),
        places = svg.append("g").attr("id", "places");

    var projection = d3.geo.mercator()
        .center([126.9895, 37.5651])
        .scale(5000)
        .translate([width/2, height/2]);

    var path = d3.geo.path().projection(projection);

    d3.json("dist/maptopo_webD.json", function(error, data) {
      var features = topojson.feature(data, data.objects.skorea_provinces_2018_geo).features;
      map.selectAll('path')
          .data(features)
        .enter().append('path')
          .attr('class', function(d) { console.log(); return 'municipality c' + d.properties.code })
          .attr('d', path);

      map.selectAll('text')
          .data(features)
        .enter().append("text")
          .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
          .attr("dy", ".35em")
          .attr("class", "municipality-label")
          .text(function(d) { return d.properties.name; })
    });

    d3.csv("places.csv", function(data) {
        places.selectAll("circle")
            .data(data)
            .enter().append("circle")
            .attr("cx", function(d) { return projection([d.lon, d.lat])[0]; })
            .attr("cy", function(d) { return projection([d.lon, d.lat])[1]; })
            .attr("r", 10);

        places.selectAll("text")
            .data(data)
            .enter().append("text")
            .attr("x", function(d) { return projection([d.lon, d.lat])[0]; })
            .attr("y", function(d) { return projection([d.lon, d.lat])[1] + 8; })
            .text(function(d) { return d.name });
    });

    