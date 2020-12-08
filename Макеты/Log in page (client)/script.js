function reg_form() {
	document.getElementById('log-text').style.display = 'block';
	document.getElementById('reg-text').style.display = 'none';
	document.getElementById('fio').style.display = 'block';
	document.getElementById('confirm-pass').style.display = 'block';
	document.getElementById('reg-btn').style.display = 'block';
	document.getElementById('log-btn').style.display = 'none';
}
function log_form() {
	document.getElementById('log-text').style.display = 'none';
	document.getElementById('reg-text').style.display = 'block';
	document.getElementById('fio').style.display = 'none';
	document.getElementById('confirm-pass').style.display = 'none';
	document.getElementById('reg-btn').style.display = 'none';
	document.getElementById('log-btn').style.display = 'block';
}