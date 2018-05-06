// get value on change select

function getValue(){
  value = document.querySelector("select").value;
  getDataPie(value);
  getDataTable(value);
  getDataGuage(value);
  getDataBubble(value);
}

// populate the select dropdown on load
function dropDown(){
  // data route
  var url="/names";

  var list = Plotly.d3.select("#sampleList").append('select').attr("onchange","getValue()")

  Plotly.d3.json(url,function(error,nameList){
    if (error) return console.warn(error)

    list.selectAll('option')
    .data(namesList)
    .enter()
    .append('option')
    .text(function(d) {return d;});

  });
}

// call back funtion to get data on change selectmto update the getDataTable

function getDataTable(sample_id){
  var url_meta = "/metadata/" + sample_id;

  Plotly.d3.select("tbody").html("");

  Plotly.d3.json(url_meta, function(error, initDataMeta){
    Plotly.d3.select("tbody").selectAll("tr")
              .data(initDataMeta)
              .enter()
              .append("tr")
              .html(function(d){
                return `<td>${Object.keys(d)}</td><td>${d[Object.keys(d)]}</td>`
              })
            });



}
