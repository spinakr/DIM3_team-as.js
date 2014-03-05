$(function() {
	$( ".inner-container" ).sortable({
	  connectWith: ".inner-container",
      revert: true,
      containment: $("#content"),
    }).disableSelection();
});



//Create new popup
;(function($) {
    $(function() {
        $('#create_new_button').bind('click', function(e) {
            e.preventDefault();
            $('#create_new_prompt').bPopup({
                easing: 'easeOutBack', //uses jQuery easing plugin
                speed: 450,
                transition: 'slideDown'
            });
        });
    });
})(jQuery);

