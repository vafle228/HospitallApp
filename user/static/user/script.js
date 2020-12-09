// Закрыть форму записи
function close_add_form() {
	var form = document.getElementById('add-session-form');
	form.style.display = 'none';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.display = 'none';
}

// Открыть форму записи
function open_add_form() {
	var form = document.getElementById('add-session-form');
	form.style.display = 'block';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.display = 'none';
}

// Поиск специалиста
function filterFunction() {
	document.getElementById("myDropdown").style.display = 'block';
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

// Выбор специалиста
function search_fill(a) {
	var input = document.getElementById("myInput");
	input.value = a.textContent;
	document.getElementById("myDropdown").style.display = 'none';
}

// Меню подробнее
function more_info(referral) {
	var form = document.getElementById('add-session-form');
	if (form.style.display != 'block'){
		var menu = document.getElementById('more-detailed-menu');
		menu.style.display = 'block';
		var specialist = document.getElementById('specialist-name');
		specialist.innerText = referral.childNodes[9].innerHTML;
		var time = document.getElementById('time&date');
		time.innerText = referral.childNodes[3].innerHTML + '    ' + referral.childNodes[5].innerHTML;
	}
}