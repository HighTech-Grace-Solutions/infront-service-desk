/* -------------------------------------------------------------------------- */
/*                             INCIDENT REPORT JS                             */
/* -------------------------------------------------------------------------- */

/* ------------------------- FILEPOND INITIALISATION ------------------------ */

FilePond.parse(document.body);

/* ---------------------- INITIALISE BOOTSTRAP POPOVER ---------------------- */

$(function () {
    $('[data-toggle="popover"]').popover()
})

/* ---------------- SUMMERNOTE WYSIWYG EDITOR INITIALISATION ---------------- */

$(document).ready(function () {
    $('#summernote').summernote({
        height: 300, // set editor height
        minHeight: 300, // set minimum height of editor
        maxHeight: 500, // set maximum height of editor
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
            ['insert', ['link', 'picture', 'video']],
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

/* ------------------------------ SLA COUNTDOWN ----------------------------- */

// $(document).ready(function () {
//     $(function () {
//         // set the date we're counting down to
//         var target_date = new Date('September, 4, 2020').getTime();
        
//         // variables for time units
//         var days, hours, minutes, seconds;

//         // get tag element
//         var countdown = document.getElementById('countdown');

//         // update the tag with id "countdown" every 1 second
//         setInterval(function () {

//             // find the amount of "seconds" between now and target
//             var current_date = new Date().getTime();
//             var seconds_left = (target_date - current_date) / 1000;

//             //     days = parseInt(seconds_left / 86400);
//             //     seconds_left = seconds_left % 86400;

//             hours = parseInt(seconds_left / 3600, 10);
//             var hours_str, mins_str, secs_str = "";
//             seconds_left = seconds_left % 3600;

//             minutes = parseInt(seconds_left / 60, 10);
//             seconds = parseInt(seconds_left % 60, 10);

//             if (hours < 10)
//                 hours_str = "0" + hours;
//             else
//                 hours_str = hours;

//             if (minutes < 10)
//                 mins_str = "0" + minutes;
//             else
//                 mins_str = minutes;

//             if (seconds < 10)
//                 secs_str = "0" + seconds;
//             else
//                 secs_str = seconds;

//             // format countdown string + set tag value
//             // countdown.innerHTML = '<strong style="font-size: 24px;"><span class="hours">' + hours_str + '<label>:</label></span><span class="minutes">'
//             //     + mins_str + '<label>:</label></span><span class="seconds">' + secs_str + '<label></label></span></strong>';

//             countdown.innerHTML = '<strong style="font-size: 24px;"><span class="hours">' + hours_str + '<label>:</label></span><span class="minutes">'
//                 + mins_str + '<label></label></span></strong>';

//         }, 1000);
//     });
// });

/* ------------------------ MULTI-LEVEL DROPDOWN MENU ----------------------- */

$(document).ready(function () {
    // $(document).on('click', '.dropdown-menu', function (e) {
    //     e.stopPropagation();
    // });

    // make it as accordion for smaller screens
    if ($(window).width() < 992) {
        $('.dropdown-menu a').click(function (e) {
            e.preventDefault();
            if ($(this).next('.submenu').length) {
                $(this).next('.submenu').toggle();
            }
            $('.dropdown').on('hide.bs.dropdown', function () {
                $(this).find('.submenu').hide();
            })
        });
    }

});

$(".dropdown-item").click(function () {
    filter = $(this).attr("data-custom-id");
    filter_type = $(this).attr("id");

    // OPTIMISED CODE
    document.getElementById("sg-header").innerHTML = document.getElementById(filter_type).innerHTML;

});

// function filterFunction() {
// 	var input, filter, a, i;
// 	input = document.getElementById("filter-dropdown-search");
//     filter = input.value.toUpperCase();

//     div = document.getElementById("sg-filter");
//     a = div.getElementsByTagName("a");

// 	for (i = 0; i < a.length; i++) {
//         txtValue = a[i].textContent || a[i].innerText;
//         console.log(txtValue);
// 		if (txtValue.toUpperCase().indexOf(filter) > -1) {
// 			a[i].style.display = "";
// 		} else {
// 			a[i].style.display = "none";
// 		}
//     }
// }

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

    $('#inputImpact, #inputUrgency').change(function () {
        var impact_val = $("#inputImpact").val();
        var urgency_val = $("#inputUrgency").val();

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

    var impact_val = $("#inputImpact").val();
    var urgency_val = $("#inputUrgency").val();

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

