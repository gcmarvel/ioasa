// Read More js

let content = document.querySelectorAll('.article-content'),
    expand = document.querySelectorAll('.button-expand'),
    collapse = document.querySelectorAll('.button-collapse');

expand[0].addEventListener('click', function() {readMore(0)});
expand[1].addEventListener('click', function() {readMore(1)});

collapse[0].addEventListener('click', function() {readLess(0)});
collapse[1].addEventListener('click', function() {readLess(1)});

function readMore(i) {
    content[i].style.maxHeight = 'inherit';
    expand[i].style.display = 'none';
    collapse[i].style.display = 'inline';
}

function readLess(i) {
    content[i].style.maxHeight = '50vw';
    expand[i].style.display = 'inline';
    collapse[i].style.display = 'none';
}

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