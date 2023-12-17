console.log("rateTable.js loaded");

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
  
  const SaveOrderingButton = document.getElementById('saveOrdering');
  const orderingForm = document.getElementById('rateCostOrderingForm');
  const tableFormInput = orderingForm.querySelector('#costTableOrderingInput');
  const rowOrder = document.getElementById('rateCostRow');

  console.log(rowOrder);
  
  let bomSortable = Sortable.create(rowOrder, {
    animation: 150,
    handle: '.handle',
    dragClass: 'dragged',
    chosenClass: 'sortableChosen',
    onChange: () => {
        SaveOrderingButton.disabled = false;
      saveOrdering("rateCostRow", tableFormInput);
  }
  });
  