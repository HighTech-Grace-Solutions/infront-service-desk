
function SetFullName() {
	document.getElementById("full_name").value = "";
	document.getElementById("full_name").value = document.getElementById("first_name").value + " " + document.getElementById("last_name").value;
}

/* --------------------------- AJAX POP-UP MODALS --------------------------- */

// User Update Modal
$(document).on("click", "#user-update-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#user-update-modal-container").html(data);
			$('#user-update-modal').modal('toggle');
		}
	});
});

// User Delete Modal
$(document).on("click", "#user-delete-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#user-delete-modal-container").html(data);
			$('#user-delete-modal').modal('toggle');
		}
	});
});

// User Update Modal (from Group)
$(document).on("click", "#group-user-update-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#group-user-update-modal-container").html(data);
			$('#user-update-modal').modal('toggle');
		}
	});
});

// User Delete Modal (from Group)
$(document).on("click", "#technician-delete-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#technician-delete-modal-container").html(data);
			$('#technician-delete-modal').modal('toggle');
		}
	});
});

// Group Create Modal
$(document).on("click", "#group-create-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#group-user-create-modal-container").html(data);
			$('#group-create-modal').modal('toggle');
		}
	});
});

// Company Update Modal
$(document).on("click", "#company-update-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#company-update-modal-container").html(data);
			$('#company-update-modal').modal('toggle');

		}
	});
});

$(document).on("click", "#company-delete-modal-pop", function () {
	$.ajax({
		url: $(this).attr("data-url"),
		success: function (data) {
			$("#company-delete-modal-container").html(data);
			$('#company-delete-modal').modal('toggle');

		}
	});
});

/* ---------- USERS, GROUPS AND COMPANIES DATATABLES INITIALISATION --------- */

$(document).ready(function () {
	$('#group-table').DataTable({
		"scrollX": true,
		"lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "All"]],
		"info": false,
	});
	rowGroup: {
		dataSrc: 'Group Name'
	}
});

$(document).ready(function () {
	$('#user-table').DataTable({
		"scrollX": true,
		"lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "All"]],
		"info": false,
	});
});

$(document).ready(function () {
	$('#company-table').DataTable({
		"scrollX": true,
		"lengthMenu": [[5, 10, 20, -1], [5, 10, 20, "All"]],
		"info": false,
	});
});

/* ----------------- CHECKBOX VALUE SET (GROUP ROUND-ROBIN) ----------------- */

// when page is ready
$(document).ready(function () {
	// on form submit
	$("#group-create-modal").on('submit', function () {
		// to each unchecked checkbox
		$(this).find('input[type=checkbox]:not(:checked)').prop('checked', true).val(0);
	})
})

/* -------------------- CHECKBOX VALUE SET (COMPANY PIC) -------------------- */

// when page is ready
$(document).ready(function () {
	// on form submit
	$("#company-update-modal").on('submit', function () {
		// to each unchecked checkbox
		$(this).find('input[type=checkbox]:not(:checked)').prop('checked', true).val(0);
	})

})

/* ---------------- function to hide the company input field ---------------- */

// function ShowHideDiv() {
// 	var ddlPassport = document.getElementById("role");
// 	var dvPassport = document.getElementById("company");
// 	dvPassport.style.display = ddlPassport.value == "Customer" ? "block" : "none";
// }