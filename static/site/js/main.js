var $page = $('html, body');
$('a[href*="#"]').click(function() {
	var section = $(this).attr('href');
	section = section.replace('#','');
    $page.animate({
        scrollTop: $('a[name*="'+section+'"]').next().offset().top
    }, 800);
    return false;
});

$(function() {
	if (!/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
		// alert(navigator.userAgent);
    	$.scrollify({
        	section : ".content-block, .intro-header ",
    	});
	} else {
        // alert(navigator.userAgent);
        $.scrollify({
            section : "",
        });
    }

});