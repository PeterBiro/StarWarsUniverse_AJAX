

function loadAnotherPage(){
    var pageNumber = this.dataset.page;
    var URL = "/?page="+pageNumber;
    window.location.href = URL;
    // var xhr = new XMLHttpRequest(); ez miért nem működött? Hogy működik ez? meg egyáltalán :)
    // xhr.open('GET', URL, true);
    // xhr.send();
    
}

function showResidents(){
    var headerKeys = ["name", "height", "mass", "skin_color", "hair_color", "eye_color", "birth_year", "gender"];

    // making of residents(and their datas) list

    var residentsUrlList = this.dataset.residentsUrl;
    residentsUrlList = residentsUrlList.replace("]", "").replace("[", "").replace(/'/g, "").split(",");
    document.getElementById("tbody").innerHTML = ""; 
    for(let i =0; i < residentsUrlList.length; i++) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {             
                var tbody = document.getElementById("tbody");
                var row, cell;
                row = tbody.insertRow();
                var responseJSON = JSON.parse(this.response);
                for (var n = 0; n < headerKeys.length; n++) {
                    cell = row.insertCell();
                    if(headerKeys[n] == "height"){
                        var height = parseInt(responseJSON[headerKeys[n]]);
                        cell.innerHTML = (height/100).toString(); 
                    } else {
                        cell.innerHTML = responseJSON[headerKeys[n]];
                    }

                }
                
            }
        };
        xhttp.open("GET", residentsUrlList[i], true);
        xhttp.send();
    }

}


var list = document.getElementsByClassName("page-btn");
for(let i = 0; i < list.length; i++) {
    list[i].addEventListener("click", loadAnotherPage);
}
var resBtnList = document.getElementsByClassName("resident-btn");
for(let i = 0; i < resBtnList.length; i++) {
    resBtnList[i].addEventListener("click", showResidents);
}