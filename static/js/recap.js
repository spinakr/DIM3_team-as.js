$(function() {
	$( ".inner-container" ).sortable({
	  connectWith: ".inner-container",
      revert: true,
      containment: $("#content"),
    }).disableSelection();
}); 