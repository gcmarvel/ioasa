//Catalogue js

const tableRows = document.querySelectorAll('.table-row');

for (var x=0; x<tableRows.length; x+=1) {
    var magnitude = tableRows[x].children[3];
    var value = parseFloat(magnitude.innerHTML);
    if (value < 7){
        tableRows[x].style.background = '#ffb50f'
    }
}

function addHD(input) {
    if (input.value === '') {
        input.value = 'HD ';
    }
}