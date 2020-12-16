
$(document).on("click", "#modal-popup", function () {
	$.ajax({
		url: $(this).attr("data-url"),

		success: function (data) {
			$("#priorty_matrix_popup").html(data);
            $('#Matrix').modal('toggle');
		}
	});
});

$(document).on("click", "#modal-popup-calendar", function () {
	$.ajax({
		url: $(this).attr("data-url"),

		success: function (data) {
			$("#calendar_popup").html(data);
            $('#Calendar').modal('toggle');
		}
	});
});



$.fn.modal.Constructor.prototype.enforceFocus = function() {};

$(document).ready(function() {
    $('.js-example-basic-multiple').select2();
    theme: "classic"
    width: 'resolve'
});


var counter = -1;

function moreFields() {

	counter++;
  if (counter > 0){
    console.log("meow")
    var newFields = document.getElementById('readroot').cloneNode(true);
    newFields.id = '';
    newFields.style.display = 'block';
    var newField = newFields.childNodes;
    for (var i=0;i<newField.length;i++) {
      var theName = newField[i].name
      if (theName)
        newField[i].name = theName + counter;
    }
    var insertHere = document.getElementById('writeroot');
    insertHere.parentNode.insertBefore(newFields,insertHere);
    console.log(counter);
  }
  }


window.onload = function(){
    document.getElementById('moreFields').onclick = function(){ moreFields(); }
    moreFields();
}
