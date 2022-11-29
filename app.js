let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#1976D2";

let item = "";

let btn1 = document.getElementById("btn1");


btn1.addEventListener("click", function(){
	if (tg.MainButton.isVisible) {
		tg.MainButton.hide();
	}
	else {
		tg.MainButton.setText("Вы выбрали первый товар");
		item = "1";
		tg.MainButton.show();
	}
});



Telegram.WebApp.onEvent("mainButtonClicked", function(){
	tg.sendData(item);
});

let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;


usercard.appendChild(p);


