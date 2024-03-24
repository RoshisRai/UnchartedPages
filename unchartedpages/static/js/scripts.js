// FOR NAV
jQuery( document ).ready(function( $ ) {
	"use strict";

        // Page loading animation
        $("#preloader").animate({
            'opacity': '0'
        }, 600, function(){
            setTimeout(function(){
                $("#preloader").css("visibility", "hidden").fadeOut();
            }, 300);
        });  
});

window.onscroll = function() { myFunction() };
var navbar = document.getElementById("navbar");
var addMargin = document.getElementById("add-margin");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
        addMargin.classList.add("add-margin")
    } else {
        navbar.classList.remove("sticky");
        addMargin.classList.remove("add-margin");
    }
}

$(document).ready(function(){
    //Nav Search Toggle
    $(".nav-dropdown").on("click", function(){
        $(".navlinks").addClass("navlinks-show")
        $(".nav-shadow").addClass("nav-shadow-show")
        $(this).toggleClass('dropped')
        $(".cross-icon").addClass('cross-icon-rotate')
    })
    $(".cross-icon").on("click", function(){
        $(".navlinks").removeClass("navlinks-show")
        $(".nav-shadow").removeClass("nav-shadow-show")
        $(".nav-dropdown").toggleClass('dropped')
        $(".cross-icon").removeClass('cross-icon-rotate')
    })
    $("#nav-shadow").on("click", function(){
        $(".navlinks").removeClass("navlinks-show")
        $(".nav-shadow").removeClass("nav-shadow-show")
        $(".nav-dropdown").toggleClass('dropped')
    })

    //Nav Search Toggle
    $(".nav-search-toggle").on("click", function(){
        $(".search-body").toggleClass("nav-search-active")
        $(this).toggleClass("fa-solid fa-magnifying-glass")
        $(this).toggleClass("fa-solid fa-xmark")
    })

    $(window).on("scroll", function (e) {
        $(".search-body").removeClass("nav-search-active")
        if($(".nav-search-toggle").hasClass('fa-magnifying-glass')){
            $(".nav-search-toggle").removeClass("fa-magnifying-glass")
            $(".nav-search-toggle").addClass("fa-xmark")
        }
        if(!$(".nav-search-toggle").hasClass('fa-magnifying-glass')){
            $(".nav-search-toggle").addClass("fa-magnifying-glass")
            $(".nav-search-toggle").removeClass("fa-xmark")
        }
    });
    $(window).on("resize", function (e) {
        $(".search-body").removeClass("nav-search-active")
        if(!$(".nav-search-toggle").hasClass('fa-magnifying-glass')){
            $(".nav-search-toggle").addClass("fa-magnifying-glass")
            $(".nav-search-toggle").removeClass("fa-xmark")
        }
    });
}) 


var differencex =0, differencey=0

// Creating a function that will give us the position of the mouse cursor
function getCursorPosition(canvas, event) {
  const rect = canvas.getBoundingClientRect()
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  return [x,y]
}

// Creating a function that will give us the cursor distance
function cursor_distane(xm, xn, ym, yn){

  var before_pos = [differencex, differencey];

//   differencex = ((xn-xm) + differencex)/2;
//   differencey = ((yn-ym) + differencey)/2;
  differencex = ((xn-xm) + differencex)/4;
  differencey = ((yn-ym) + differencey)/4;

  // Now we will give it transform as we move the mouse

  var shape = document.getElementById('shape');

  var changex = 'rotateY('+ differencex +'deg)';
  var changey = 'rotateX('+ differencey +'deg)';

  shape.style.transform = changex + ' ' + changey;
}

var getmousePos = function (e) {
  var after = getCursorPosition(canvas, e);

  var afterx = after[0]
  var aftery = after[1]

  // Now we want the distance between the position we had clicked the mouse and now when we are moving the mouse

  cursor_distane(beforex, afterx, beforey, aftery)

}

const canvas = document.getElementById('particles-js');
canvas.addEventListener('mouseover' ,(e) => {
  var before = getCursorPosition(canvas, e);

  beforex = before[0]
  beforey = before[1]

  canvas.addEventListener('mousemove', getmousePos);
});

canvas.addEventListener('mouseup', (e)=>{
  canvas.removeEventListener('mousemove', getmousePos)
});

let dateobj = new Date();
let currentyear = dateobj.getFullYear()
document.querySelector('.currentyear').innerText = currentyear;