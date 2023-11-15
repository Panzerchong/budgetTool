console.log("hello there")

function calculateColumnSum(columnIndex) {
    var table = document.getElementById("billTable");
    var sum = 0;
    var value=0;

    for (var i = 1; i < table.rows.length; i++) {
      var cell = table.rows[i].cells[columnIndex];
      if(cell){
        //replace comma
        var content = cell.innerText.replace(',', '');
        //get numeric value
        var numbers = content.match(/(\d+\.\d+|\d+)/g);
        number=parseFloat(numbers)
        sum+=number
      }
  }

    return sum;
}


var adjustString=document.getElementById('adjustComplexityBOM').getAttribute('adjustComplexityBOM')
var quoteString = document.getElementById('quoteValue').getAttribute('data-quote')
var quote=parseInt(quoteString)
// var adjust=parseFloat("{{project.adjust_bom}}")
var adjust=parseFloat(adjustString)


var totalCostEstimate = calculateColumnSum(5);
var totalCostActual = calculateColumnSum(8);
var totalSale=calculateColumnSum(6);
var listAdjusted=Math.round(totalSale*(1+adjust))
var marginEst=(1-totalCostEstimate/totalSale)*100
var marginAdj=(1-totalCostEstimate/listAdjusted)*100
var marginActual=(1-totalCostActual/quote)*100

document.getElementById("totalCostEstimate").innerText = totalCostEstimate.toLocaleString();
document.getElementById("totalCostActual").innerText = totalCostActual.toLocaleString();
document.getElementById("totalSale").innerText = totalSale.toLocaleString();
document.getElementById("listAdjusted").innerText = listAdjusted.toLocaleString();//add commas to thousand
document.getElementById("marginEst").innerText = marginEst.toFixed(2);
document.getElementById("marginAdj").innerText = marginAdj.toFixed(2);
document.getElementById("marginActual").innerText = marginActual.toFixed(2);

//duplicate values for project summry 
document.getElementById("totalCostEstimate1").innerText = totalCostEstimate.toLocaleString();
document.getElementById("totalCostEstimate2").innerText = totalCostEstimate.toLocaleString();
document.getElementById("totalCostActual1").innerText = totalCostActual.toLocaleString();
document.getElementById("totalSale1").innerText = totalSale.toLocaleString();
document.getElementById("listAdjusted1").innerText = listAdjusted.toLocaleString();//add commas to thousand




//service part

function calculateService(columnIndex) {
  var table = document.getElementById("serviceTable");
  var sum = 0;
  var number=0;

  for (var i = 1; i < table.rows.length; i++) {
      var cell = table.rows[i].cells[columnIndex];
      if(cell){
        //replace comma
        var content = cell.innerText.replace(',', '');
        //get numeric value
        var numbers = content.match(/(\d+\.\d+|\d+)/g);
        number=parseFloat(numbers)
        sum+=number
      }
  }

  return sum;
}

var hours=calculateService(3)
document.getElementById("hours").innerText = hours
var riskHours=calculateService(4)
document.getElementById("riskHours").innerText = riskHours
var labor=calculateService(9)
document.getElementById("labor").innerText = labor.toLocaleString();
var laborAdjusted=calculateService(10)
document.getElementById("laborAdjusted").innerText = laborAdjusted.toLocaleString();
var costEst=calculateService(12)
document.getElementById("costEst").innerText = costEst.toLocaleString();
var costAdjustedEst=calculateService(13)
document.getElementById("costAdjustedEst").innerText = costAdjustedEst.toLocaleString();
var costAct=calculateService(14)
document.getElementById("costAct").innerText = costAct.toLocaleString();

var costMargin=(1-costEst/labor)*100
document.getElementById("costMargin").innerText = costMargin.toFixed(0);
var costAdjustedMargin=(1-costAdjustedEst/laborAdjusted)*100
document.getElementById("costAdjustedMargin").innerText = costAdjustedMargin.toFixed(0);

var serviceQuote=parseInt(document.getElementById("quoteService").getAttribute('quoteService'))
var actualMargin=(1-costAct/serviceQuote)*100
document.getElementById("actualMargin").innerText = actualMargin.toFixed(0);

//duplicate value for project summry
document.getElementById("labor1").innerText = labor.toLocaleString();
document.getElementById("laborAdjusted1").innerText = laborAdjusted.toLocaleString();
document.getElementById("costEst1").innerText = costEst.toLocaleString();
document.getElementById("costAdjustedEst1").innerText = costAdjustedEst.toLocaleString();
document.getElementById("costAct1").innerText = costAct.toLocaleString();
//calculate BoM and Servicesummry
document.getElementById("listSummry").innerText = (labor+totalSale).toLocaleString();
document.getElementById("listAdjustedSummry").innerText = (laborAdjusted+listAdjusted).toLocaleString();
document.getElementById("costEstSummry").innerText = (costEst+totalCostEstimate).toLocaleString();
document.getElementById("costAdjustedEstSummry").innerText = (costAdjustedEst+totalCostEstimate).toLocaleString();
document.getElementById("costActSummry").innerText = (costAct+totalCostActual).toLocaleString();

document.getElementById("totalQuote").innerText = (quote+serviceQuote).toLocaleString();

var listMarginSummry=(1-(costEst+totalCostEstimate)/(labor+totalSale))*100
var listAdjustedMarginSummry=(1-(costAdjustedEst+totalCostEstimate)/(laborAdjusted+listAdjusted))*100
var quotedMarginSummry=(1-(costAdjustedEst+totalCostEstimate)/(quote+serviceQuote))*100
var actualMarginSummry=(1-(costAct+totalCostActual)/(quote+serviceQuote))*100

document.getElementById("listMarginSummry").innerText = listMarginSummry.toFixed(0);
document.getElementById("listAdjustedMarginSummry").innerText = listAdjustedMarginSummry.toFixed(0);
document.getElementById("quotedMarginSummry").innerText = quotedMarginSummry.toFixed(0);
document.getElementById("actualMarginSummry").innerText = actualMarginSummry.toFixed(0);

