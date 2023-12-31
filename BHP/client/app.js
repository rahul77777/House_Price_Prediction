function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var area_in_sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var locality = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      area_in_sqft: parseFloat(area_in_sqft.value),
      bhk: bhk,
      bath: bathrooms,
      locality: locality.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_locality_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_locality_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locality = data.locality;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locality) {
              var opt = new Option(locality[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;