

function loadAnotherPage(){
    var pageNumber = this.dataset.page;
    var URL = "/?page="+pageNumber;
    window.location.href = URL;
    // var xhr = new XMLHttpRequest(); ez miért nem működött? Hogy működik ez? meg egyáltalán :)
    // xhr.open('GET', URL, true);
    // xhr.send();
    
}

function showResidents(){
    var modalTitle = this.dataset.modalTitle;
    document.getElementById("residents-title").innerHTML = modalTitle;
    var headerKeys = ["name", "height", "mass", "skin_color", "hair_color", "eye_color", "birth_year", "gender"];
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

function registerUser() {
    var userName = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var password2 = document.getElementById("password2").value;
    if (userName === "") {
        alert("Welcome Terence Hill! Or should we call you Nobody?")
    }
    if (password !== password2) {
        alert("The passwords are not the same.")
    }
}

function initNavbar() {
    var userName = sessionStorage.getItem("user");
    if (userName === null) {
        document.getElementById("nav-registration").style.display = "block";
        document.getElementById("nav-login").style.display = "block";
        document.getElementById("nav-logout").style.display = "none";
        document.getElementById("nav-user").style.display = "none";
    } else {
        document.getElementById("nav-registration").style.display = "none";
        document.getElementById("nav-login").style.display = "none";
        document.getElementById("nav-logout").style.display = "block";
        document.getElementById("nav-user").style.display = "block";

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

var regSendBtn = document.getElementById("reg-send")
if (regSendBtn !== null){
    regSendBtn.addEventListener("click", registerUser);
}

// initNavbar();