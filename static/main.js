

function loadAnotherPage(){
    var pageNumber = this.dataset.page;
    var URL = "/?page="+pageNumber;
    window.location.href = URL;
    // var xhr = new XMLHttpRequest(); ez miért nem működött? Hogy működik ez? meg egyáltalán :)
    // xhr.open('GET', URL, true);
    // xhr.send();
    
}

var list = document.getElementsByClassName("page-btn");
for(let i =0; i < list.length; i++) {
    list[i].addEventListener("click", loadAnotherPage);
}
