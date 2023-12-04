console.log("hello there")

function calculateColumnSum(columnIndex) {
    var table = document.getElementById("billTable");
    var sum = 0;
    var value=0;

    //start from row 2 with value
    for (var i = 2; i < table.rows.length; i++) {
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
var marginQuoted=(1-totalCostEstimate/quote)*100

document.getElementById("totalCostEstimate").innerText = totalCostEstimate.toLocaleString();
document.getElementById("totalCostActual").innerText = totalCostActual.toLocaleString();
document.getElementById("totalSale").innerText = totalSale.toLocaleString();
document.getElementById("listAdjusted").innerText = listAdjusted.toLocaleString();//add commas to thousand
document.getElementById("marginEst").innerText = marginEst.toFixed(2);
document.getElementById("marginAdj").innerText = marginAdj.toFixed(2);
document.getElementById("marginActual").innerText = marginActual.toFixed(2);
document.getElementById("marginQuoted").innerText = marginQuoted.toFixed(2);

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

  for (var i = 2; i < table.rows.length; i++) {
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


function projectDelete(pk) {
  if (confirm("Are you sure you want to delete this project?")) {
    window.location.href = "/budgetTool/" + pk + "/delete";
  }
}

function deleteRow(button) {
  // Implement row deletion logic here
  var row = button.parentNode.parentNode;
  row.parentNode.removeChild(row);
  console.log('Form deleted!');
}

function redirectToCurrentPage() {
  window.location.reload(true);
}

function saveOrdering(rowId,formInput) {
  const rows = document.getElementById(rowId).querySelectorAll('tr');
  let ids = [];
  for (let row of rows) {
      console.log(row.dataset)
      ids.push(row.dataset.lookupid);
  }
  formInput.value = ids.join(',');
  console.log(formInput.value)
  // orderingForm.submit();
}

// bom ordering part
const bomSaveOrderingButton = document.getElementById('bomSaveOrdering');
const bomOrderingForm = document.getElementById('bomOrderingForm');
const bomFormInput = bomOrderingForm.querySelector('#bomOrderingInput');
const bomRowOrder = document.getElementById('bomRow');

let bomSortable = Sortable.create(bomRowOrder, {
  animation: 150,
  handle: '.handle',
  dragClass: 'dragged',
  chosenClass: 'sortableChosen',
  onChange: () => {
    bomSaveOrderingButton.disabled = false;
    saveOrdering("bomRow", bomFormInput);
}
});

//service order part
const saveOrderingButton = document.getElementById('saveOrdering');
const serviceOrderingForm = document.getElementById('serviceOrderingForm');
const serviceformInput = serviceOrderingForm.querySelector('#serviceOrderingInput');
const serviceRowOrder = document.getElementById('serviceRow');
  
let sortable = Sortable.create(serviceRowOrder, {
  animation: 150,
  handle: '.handle',
  dragClass: 'dragged',
  chosenClass: 'sortableChosen',
  onChange: () => {
    saveOrderingButton.disabled = false;
    saveOrdering("serviceRow", serviceformInput);
}
});
// saveOrderingButton.addEventListener('click', saveOrdering);
  



// htmx.onLoad(function(content) {
//   var sortables = content.querySelectorAll("tbody");
//   for (var i = 0; i < sortables.length; i++) {
//     var sortable = sortables[i];
//     var sortableInstance = new Sortable(sortable, {
//         animation: 150,
//         handle: '.handle',
//         dragClass: 'dragged',
//         chosenClass: 'sortableChosen',
//         ghostClass: 'blue-background-class',

//         // Make the `.htmx-indicator` unsortable
//         filter: ".htmx-indicator",
//         onMove: function (evt) {
//           return evt.related.className.indexOf('htmx-indicator') === -1;
//         },

//         // Disable sorting on the `end` event
//         // onEnd: function (evt) {
//         //   this.option("disabled", true);
//         // }
//     });

//     // Re-enable sorting on the `htmx:afterSwap` event
//     sortable.addEventListener("htmx:afterSwap", function() {
//       sortableInstance.option("disabled", false);
//     });
//   }
// })




// function submitBill() {
//   var form = document.getElementById('billForm');
//   console.log(form)
//   var formData= new FormData(form)
//   event.preventDefault();  // Prevent default submission

//   // var table = document.getElementById('billTable');
//   // var rowCount = table.rows.length;  
//   // var lastRow = table.rows[rowCount - 1];
//   // console.log(lastRow)
//   // var form = lastRow.querySelector('form');
//   // console.log(form)
//   // var formData= new FormData(form)  

  
  
//   fetch(form.action, {
//       method: 'POST',
//       body: formData,
//       headers: {
//           'X-CSRFToken': "{{ csrf_token }}", 
//       },
//   })
//   .then(response => response.json())
//   .then(data => {
//       console.log('Form submitted information:', data);
//       if(data.status=='error'){
//         alert('Save item failed. Please check your input.');
//         // appendAlert('Form submission failed. Please check your input.', 'success')
//         console.error('Error submitting form:', error);
//       }
      
//   })
//   .catch(error => {});
// }

// document.body.addEventListener('htmx:configRequest', (event) => {
//   event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
// });

