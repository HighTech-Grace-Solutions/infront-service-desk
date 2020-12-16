// $("[data-trigger]").on("click", function (e) {
//     e.preventDefault();
//     e.stopPropagation();
//     var offcanvas_id = $(this).attr('data-trigger');
//     $(offcanvas_id).toggleClass("show");
//     $('body').toggleClass("offcanvas-active");
//     $(".screen-overlay").toggleClass("show");
// });

// $(".btn-close, .screen-overlay").click(function (e) {
//     $(".screen-overlay").removeClass("show");
//     $(".offcanvas").removeClass("show");
//     $("body").removeClass("offcanvas-active");
// });

// Toggle sidebar on upon mouseover at bars
$("#sidebar-bars-toggle").mouseover(function (e) {
    e.preventDefault();
    e.stopPropagation();
    var offcanvas_id = $(this).attr('data-trigger');
    $(offcanvas_id).toggleClass("show");
    $('body').toggleClass("offcanvas-active");
    $(".screen-overlay").toggleClass("show");
});

// Toggle sidebar off upon mouseover to screen overlay
$(".screen-overlay").mouseover(function (e) {
    $(".screen-overlay").removeClass("show");
    $(".offcanvas").removeClass("show");
    $("body").removeClass("offcanvas-active");
});

var dropdown = document.getElementsByClassName("dropdown-btn");
var dropdown_container = document.getElementsByClassName("dropdown-container");
var i;

for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("mouseover", function () {
        // this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }

    });
}