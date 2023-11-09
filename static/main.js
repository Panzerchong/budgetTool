console.log("hello there")

function calculateColumnSum(columnIndex) {
    var table = document.getElementById("billTable");
    var sum = 0;

    for (var i = 1; i < table.rows.length; i++) {
        var cell = table.rows[i].cells[columnIndex];
        if(cell){
          var number = parseInt(cell.innerHTML.replace(/,/g, ''));
          sum+=number
        }
    }

    return sum;
}


var adjustString=document.getElementById('adjustValue').getAttribute('adjustValue')
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


