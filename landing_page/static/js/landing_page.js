/* ------------------------------ ANNOUNCEMENTS ----------------------------- */

$(document.body).on('hidden.bs.modal', function () {
    $('body').css('padding-right','0');
});

$(document).ready(function () {
	$(".flip1").click(function () {
		$($(this).nextAll(".panel1")[0]).slideToggle("fast");
	});
});

var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
	close[i].onclick = function () {
		var div = this.parentElement;
		div.style.opacity = "0";
		setTimeout(function () { div.style.display = "none"; }, 600);
	}
}

$('.collapse').collapse();
/* ---------------------------- POPULAR SOLUTIONS --------------------------- */

$(document).ready(function () {
	$(".flip").click(function () {
		$($(this).nextAll(".panel")[0]).slideToggle("fast");
	});
});

