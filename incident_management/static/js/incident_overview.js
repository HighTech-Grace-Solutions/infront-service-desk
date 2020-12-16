/* -------------------------------------------------------------------------- */
/*                            INCIDENT OVERVIEW JS                            */
/* -------------------------------------------------------------------------- */

/* -------------------------- INITIALISE DATATABLE -------------------------- */

$(document).ready(function () {
	var table = $("#overview-table").DataTable({
		// Set limit of rows displayed
		lengthMenu: [
			[5, 10, 20, -1],
			[5, 10, 20, "All"],
		],
		// Hide Source, SG, Reported By fields by default
		'columnDefs': [
			{ 'visible': false, 'targets': [7, 8] },
			{ "width": "5%", "targets": 0 },
			{ "width": "8%", "targets": 1 },
			{ "width": "20%", "targets": 3 },
			{ "width": "10%", "targets": [5, 6, 9, 10] },6
		],
		scrollX: true,

	});


	// Toggle via checkbox
	$("input.toggle-vis").on("change", function (e) {
		e.preventDefault();

		// Get the column API object
		var column = table.column($(this).attr("data-column"));

		// Toggle the visibility
		column.visible(!column.visible());

	});
});

/* ---------------- SUMMERNOTE WYSIWYG EDITOR INITIALISATION ---------------- */

$(document).ready(function () {
	$('#summernote').summernote({
		height: 200, // set editor height
		minHeight: null, // set minimum height of editor
		maxHeight: null, // set maximum height of editor
		// focus: true // set focus to editable area after initializing summernote
		placeholder: 'Description of incident',

		toolbar: [
			['style', ['style']],
			['font', ['bold', 'underline', 'clear']],
			['fontname', ['fontname']],
			['fontsize', ['fontsize']],
			['color', ['color']],
			['para', ['ul', 'ol', 'paragraph']],
			['height', ['height']],
			['table', ['table']],
			['insert', ['link', 'picture']],
			['view', ['fullscreen', 'codeview', 'help']],
		],
	});
});


/* ------------------- CLICKABLE TABLE ROW (LINK REDIRECT) ------------------ */

// Clickable Table Row (leads to outside link using data-href)
// Alternative 1: Universal clickable rows
$(document).ready(function ($) {
	$(document.body).on("click", "tr[data-href]", function () {
		console.log("mweowowo")
		window.location.href = this.dataset.href;
	});
});

// Alternative (specifiying clickable rows using using class)
// $(document).ready(function($) {
//     $(".table-row").click(function() {
//         window.document.location = $(this).data("href");
//     });
// });

/* ---------------------- CUSTOM SEARCH BAR (OBSOLETE) ---------------------- */

$(document).ready(function () {
	$("#search-input").on("keyup", function () {
		var value = $(this).val().toLowerCase();
		$("#incident-table tr").filter(function () {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
		});
	});
});

/* ----------------------- CLICKABLE TABLE ROW (MODAL) ---------------------- */

$(document).on("click", "#modal-pop", function () {
	$("#modal_aside_left").modal("show");
	// setTimeout(function () {
	//     $('#modal_aside_left').modal('show');
	// }, 500);
});

/* -------------------- CLICKABLE TABLE ROW (OFF-CANVAS) -------------------- */

$(document).on("click", "#off-canvas-preview-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#off-canvas-preview").html(data);
			// setTimeout(function () {
			// 	$(".screen-overlay-preview").toggleClass("show");
			// 	$("#ticket-preview").toggleClass("show");
			// }, 5);
			$(".screen-overlay-preview").toggleClass("show");
			$("#ticket-preview-off-canvas").toggleClass("show");
		}
	});
});

$(document).ready(function () {
	$("[data-trigger]").on("click", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var offcanvas_id = $(this).attr("data-trigger");
		$(offcanvas_id).toggleClass("show");
		$("body").toggleClass("offcanvas-active");
		$(".screen-overlay-preview").toggleClass("show");
	});

	// Close menu when pressing ESC
	$(document).on("keydown", function (event) {
		if (event.keyCode === 27) {
			// $(".offcanvas").removeClass("show");
			// $("body").removeClass("overlay-active");
			$(".screen-overlay-preview").removeClass("show");
			$(".offcanvas-preview").removeClass("show");
			$("body").removeClass("offcanvas-active");
		}
	});

	// Close menu when either button or screen overlay is clicked
	$("#close-preview, .screen-overlay-preview").click(function (e) {
		$(".screen-overlay-preview").removeClass("show");
		$(".offcanvas-preview").removeClass("show");
		$("body").removeClass("offcanvas-active");
	});
});

function closePreview() {
	document.getElementById("screen-overlay-preview").classList.remove("show");
	document.getElementById("ticket-preview").classList.remove("show");
}

/* ----------------------- TABLE FILTER DROPDOWN MENU ----------------------- */

// Auto-filter tickets based on current user's tickets
$(document).ready(function () {
	document.getElementById("filter-assigned-to").click();
});

$(".filter").click(function (e) {
	let table, rows, headers, cells, country, filter;
	table = document.getElementById("overview-table");
	rows = table.getElementsByTagName("tr");
	headers = table.getElementsByTagName("th");
	filter = $(this).attr("data-custom-id");
	filter_type = $(this).attr("id");

	// Reset any previous column/global search filters
	$("#overview-table").DataTable().columns().search('').search('').draw();

	// Filter selections
	if (filter == 'All' || filter_type == 'filter-general') {
		$("#overview-table").DataTable().columns().search('').search('').draw();
	}
	else if (filter_type == 'filter-assigned-to') {
		$("#overview-table").DataTable().columns('.assigned-to-col').search(filter, true, false).draw();
	}
	else if (filter_type == 'filter-support-group') {
		$("#overview-table").DataTable().columns('.support-group-col').search(filter, true, false).draw();
	}
	else {
		$("#overview-table").DataTable().search(filter, true, false).draw();
	}

	// Changing dropdown headers based on filter selected
	if (filter_type == "filter-general")
		document.getElementById("incident-header").innerHTML =
			filter + " Tickets <i class='fas fa-caret-down fa-xs'></i>";
	else if (filter_type == "filter-state")
		document.getElementById("incident-header").innerHTML =
			filter + " Tickets <i class='fas fa-caret-down fa-xs'></i>";
	else if (filter_type == "filter-assigned-to")
		document.getElementById("incident-header").innerHTML =
			"My Open Tickets <i class='fas fa-caret-down fa-xs'></i>";
	else if (filter_type == "filter-priority")
		document.getElementById("incident-header").innerHTML =
			"High Priority Tickets <i class='fas fa-caret-down fa-xs'></i>";
	else if (filter_type == "filter-support-group")
		document.getElementById("incident-header").innerHTML =
			"My Support Group Tickets <i class='fas fa-caret-down fa-xs'></i>";

});

function filterFunction() {
	var input, filter, ul, li, a, i;
	input = document.getElementById("filter-dropdown-search");
	filter = input.value.toUpperCase();
	div = document.getElementById("filter-dropdown-content");
	a = div.getElementsByTagName("a");
	flag = false;

	$("div[id=divider]").addClass("dropdown-divider");
	$("h6[id=header]").css("display", "");

	for (i = 0; i < a.length; i++) {
		txtValue = a[i].textContent || a[i].innerText;
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		} else {
			a[i].style.display = "none";
			$("div[id=divider]").removeClass("dropdown-divider");
			$("h6[id=header]").css("display", "none");
		}
	}
}
