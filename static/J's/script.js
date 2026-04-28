console.log("Site start");
console.log("Server load");

let darkMode = localStorage.getItem("darkMode") === "true";
let menu_status = false;

var eror = document.getElementById("eror_dash");

setTimeout(() => {
  eror.style.display = "block";
}, 3000);

var notif_ad = document.getElementById("notif_admin");

setTimeout(() => {
  notif_ad.style.top = "-400px";
  notif_ad.style.transition = "0.5s";
}, 2000);


function applyTheme(showNotif) {
  if (darkMode) {
    document.body.style.backgroundColor = "#1a0b2e";
    document.body.style.color = "#ffffff";

    if (showNotif) {
      let data = document.getElementById("notif_on");
      if (data) {
        data.style.top = "40px";
        setTimeout(() => {
          data.style.top = "-420px";
        }, 3000);
      }
    }

    console.log("status : okay");
  } else {
    document.body.style.backgroundColor = "#ffffff";
    document.body.style.color = "#000000";

    if (showNotif) {
      let data1 = document.getElementById("notif_off");
      if (data1) {
        data1.style.top = "40px";
        setTimeout(() => {
          data1.style.top = "-420px";
        }, 3000);
      }
    }

    console.log("status : okay");
  }
}

function Change_tem() {
  darkMode = !darkMode;
  localStorage.setItem("darkMode", darkMode);
  applyTheme(true);
}

function open_menu() {
  var data = document.getElementById("main_menu");
  if (!data) return;

  if (menu_status === false) {
    data.style.right = "10px";
    data.style.transition = "0.6s";
    menu_status = true;
  } else {
    data.style.right = "-400px";
    data.style.transition = "0.6s";
    menu_status = false;
  }
}

function Copy(el){
  navigator.clipboard.writeText(el.innerText);
  let data = document.getElementById("copy_text");
  data.style.display = "block";
  data.style.transition = "0.6s";
  data.style.textDecoration = "underline";
  setTimeout(() => {
    data.style.display = "none";
    data.style.textDecoration = "none";
    data.style.transition = "0.6s";
  }, 3000);
}

applyTheme(false);
