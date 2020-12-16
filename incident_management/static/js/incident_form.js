/* -------------------------------------------------------------------------- */
/*                              INCIDENT FORM JS                              */
/* -------------------------------------------------------------------------- */

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

		// maximumImageFileSize: 500 * 1024, // 500 KB
        // callbacks: {
        //     onImageUploadError: function (msg) {
        //         console.log(msg + ' (1 MB)');
        //     }
        // }
	});
});

/* -------------------- DEPENDENT/DYNAMIC DROPDOWN MENUS -------------------- */

// Category and Sub-category
var $select1 = $("#inputCategory"),
	$select2 = $("#inputSubcategory"),
	$options = $select2.find("option");

$select1
	.on("change", function () {
		// $select2.html($options.filter('[value="' + this.value + '"]'));
		var type = $('option:selected', this).attr('type');
		$select2.html($options.filter('[type="' + type + '"]'));
		$("#inputSubcategory").selectpicker("refresh");
	})
	.trigger("change");


// Support Group and Assigned To
var $select3 = $("#inputSupportGroup"),
	$select4 = $("#inputAssignee"),
	$options_2 = $select4.find("option");

$select3
	.on("change", function () {
		// $select4.html($options_2.filter('[value="' + this.value + '"]'));
		var type = $('option:selected', this).attr('type');
		$select4.html($options_2.filter('[type="' + type + '"]'));
		$("#inputAssignee").selectpicker("refresh");
	})
	.trigger("change");


$(document).ready(function () {

	if ($(this).val() === "" || $(this).val() === "Not set") {
		// document.getElementById("subcategory").disabled = true;
		// $("#inputSubcategory").prop("disabled");
		$("#inputSubcategory").prop("disabled", true);
		$("#inputSubcategory").selectpicker("refresh");
		
		// Disabled if RR 
		// $("#inputAssignee").prop("disabled", true);
		// $("#inputAssignee").selectpicker("refresh");

		// $("#inputUrgency").prop("disabled", true);
		// $("#inputUrgency").selectpicker("refresh");

	} else {
		$("#inputSubcategory").prop("disabled", false);
		$("#inputSubcategory").selectpicker("refresh");

		// Disabled if RR 
		// $("#inputAssignee").prop("disabled", false);
		// $("#inputAssignee").selectpicker("refresh");

		// $("#inputUrgency").prop("disabled", false);
		// $("#inputUrgency").selectpicker("refresh");
	}

	$("#inputCategory").change(function () {

		if ($(this).val() === "Not set" || $(this).val() === "") {
			//   document.getElementById("subcategory").disabled = true;
			//   $("#inputSubcategory").prop("disabled");
			$("#inputSubcategory").prop("disabled", true);
			$("#inputSubcategory").selectpicker("refresh");

		} else {
			//   document.getElementById("subcategory").disabled = false;
			//   $("#inputSubcategory").prop("enabled");
			$("#inputSubcategory").prop("disabled", false);
			$("#inputSubcategory").selectpicker("refresh");
		}
	});

	$("#inputSupportGroup").change(function () {

		if ($(this).val() === "Not set" || $(this).val() === "") {
			$("#inputAssignee").prop("disabled", true);
			$("#inputAssignee").selectpicker("refresh");
		} else {
			$("#inputAssignee").prop("disabled", false);
			$("#inputAssignee").selectpicker("refresh");
		}
	});

	// $("#inputImpact").change(function () {
	//     // console.log($(this).val());

	//     if ($(this).val() === "Not set" || $(this).val() === "") {
	//         $("#inputUrgency").prop("disabled", true);
	//         $("#inputUrgency").selectpicker("refresh");
	//     } else {
	//         $("#inputUrgency").prop("disabled", false);
	//         $("#inputUrgency").selectpicker("refresh");
	//     }
	// });

	$('#inputImpact, #inputUrgency').change(function () {
		var impact_val = $("#inputImpact").val();
		var urgency_val = $("#inputUrgency").val();
		console.log();

		if (impact_val == 1 && urgency_val == 1) {
			document.getElementById("priority").innerHTML = '<i class="fas fa-arrow-up" style="color: red"></i><strong>&nbsp;1</strong>';
		}
		else if ((impact_val == 2 && urgency_val == 1) || (impact_val == 1 && urgency_val == 2)) {
			document.getElementById("priority").innerHTML = '<i class="fas fa-arrow-up" style="color: orange"></i><strong>&nbsp;2</strong>';
		}
		else if ((impact_val == 1 && urgency_val == 3) || (impact_val == 2 && urgency_val == 2) || (impact_val == 3 && urgency_val == 1)) {
			document.getElementById("priority").innerHTML = '<i class="fas fa-arrow-up" style="color: yellow"></i><strong>&nbsp;3</strong>';
		}
		else if ((impact_val == 3 && urgency_val == 2) || (impact_val == 2 && urgency_val == 3) || (impact_val == 3 && urgency_val == 3)) {
			document.getElementById("priority").innerHTML = '<i class="fas fa-arrow-up" style="color: green"></i><strong>&nbsp;4</strong>';
		}

	});



});

/* ------------------- SET MIN. DATETIME FOR SLA COUNTDOWN ------------------ */

$(document).ready(function () {
	var iso = new Date().toISOString();
	var minDate = iso.substring(0, iso.length - 8);
	// console.log(minDate);
	$("#inputSLA_Response").attr("min", minDate);
	$("#inputSLA_Resolution").attr("min", minDate);

});


