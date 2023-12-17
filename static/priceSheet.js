//get all pricesheet tables
var tables = document.querySelectorAll('[id^="prcieSheetTable_"]');

function saveOrdering(table,formInput) {
    const rows = document.getElementById(table).querySelectorAll('tr');
    let ids = [];
    for (let row of rows) {
        console.log(row.dataset)
        ids.push(row.dataset.lookupid);
    }
    formInput.value = ids.join(',');
    console.log(formInput.value)
    // orderingForm.submit();
  }

  tables.forEach((table, index) => {
    
    const tableId = 'prcieSheetTable_'+(index+1);
    const buttonId = 'saveOrdering_'+(index+1);
    const orderingFormId = 'priceSheetOrderingForm_'+(index+1);
    const formInputId = '#priceSheetOrderingInput_'+(index+1);
    console.log(tableId);

    const SaveOrderingButton = document.getElementById(buttonId);
    const orderingForm = document.getElementById(orderingFormId);
    const tableFormInput = orderingForm.querySelector(formInputId);
    const rowOrder = document.getElementById(tableId);
    console.log(rowOrder);

    let bomSortable = Sortable.create(rowOrder, {
          animation: 150,
          handle: '.handle',
          dragClass: 'dragged',
          chosenClass: 'sortableChosen',
          onChange: () => {
              SaveOrderingButton.disabled = false;
            saveOrdering(tableId, tableFormInput);
        }
        });
  });
  