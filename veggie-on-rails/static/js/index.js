$(document).ready(function(){
    $("#carousel-slide-1").addClass("active");
    $("#carousel-selector-1").addClass("selected");
    $('.carousel').carousel();
    $('[id^=carousel-selector-]').click( function(){
        var id_selector = $(this).attr("id");
        var id = id_selector.substr(id_selector.length -1);
        id = parseInt(id);
        $('.carousel').carousel(id - 1);
    });
    $('img').click(function(){
	   $('.selected').removeClass('selected'); // removes the previous selected class
	   $(this).addClass('selected'); // adds the class to the clicked image
	});
});

