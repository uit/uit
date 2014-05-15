jQuery(document).ready(function($) {
		
     
	/* Tool tip */
	
	if( $.fn.tooltip() ) {
		$('[class="tooltip_hover"]').tooltip();
	}





	/* Carousel */

	$(".carousel").jCarouselLite({
		btnNext : ".next",
		btnPrev : ".prev",
		easing : "swing", 
		vertical : true,
		auto : 4000,
		speed : 500,
		visible : 3,
		scroll : 1,
		mouseWheel : true
	});



	/* Contact form */	

	$("#contact").submit(function() {
		$.ajax({
			type : "POST",
			url : "send_mail.php",
			dataType : "html",
			data : $(this).serialize(),
			beforeSend : function() {
				$("#loading").show();
			},
			success : function(response) {
				$("#response").html(response);
				$("#loading").hide();
			}
		})
		return false;
	});
	
	


		
	/* Newsleter form */	

	$("#newsletter").submit(function() {
		$.ajax({
			type : "POST",
			url : "newsletter.php",
			dataType : "html",
			data : $(this).serialize(),
			beforeSend : function() {
				$("#loadingNews").show();
			},
			success : function(response) {
				$("#responseNews").html(response);
				$("#loadingNews").hide();
			}
		})
		return false;
	});




	/* Responsive Video */	

	$(".video").fitVids();
	$('input, textarea').placeholder();
	
	




	/* Slider */	
	
	$('.bxslider').bxSlider({
	  auto: true,
	});
	
	

});

