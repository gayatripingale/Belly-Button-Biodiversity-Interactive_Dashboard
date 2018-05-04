// Getting referances

function updateMetaData(data){
  // Reference to Panel element for sample updateMetaData
  var PANEL = document.getElementById("sample-metadata");

  //clear any existing updateMetaData
  PANEL.innerHTML = '';
  //Loop through all of the keys in the json resposnse
  // and create new metadata tags
  for( var key in data){
    h6tag = documnet.createElement("h6");
    h6text = document.createTextNode(`${key}:${data[key]}`);
    h6tag.append(h6Text);
    PANEL.appendChild(h6tag);
  }
}

function buildCharts(sampleData,otuData){
  
}
