var updateCategory = function(requirement) {
	var category = requirement.closest(".category-column").data("category");
	requirement.data("category", category);
	console.log(requirement.data("category"));
};

var doAjax = function(requirement) {
	var url = 'changecategory/';
	var reqid = requirement.data("id");
	var category = requirement.data("category");
	$.ajax({
		type : "POST",
		url : url,
		data : {
			"req_id" : reqid,
			"category" : category,
			"csrfmiddlewaretoken" : $("input[name='csrfmiddlewaretoken']").val(),
		},
		success : function(msg) {
			console.log(msg);
		}
	});
};

$(function() {
	$(".inner-container").sortable({
		connectWith : ".inner-container",
		revert : true,
		containment : $("#content"),
		update : function(event, ui) {
			//prevent calling calling the method twice
			if (!ui.sender) {
				updateCategory(ui.item);
				doAjax(ui.item);
			}
		}
	}).disableSelection();
});

//Create new popup
;
(function($) {
	$(function() {
		$('#create_new_button').bind('click', function(e) {
			e.preventDefault();
			$('#create_new_prompt').bPopup({
				easing : 'easeOutBack', //uses jQuery easing plugin
				speed : 450,
				transition : 'slideDown'
			});
		});
	});
})(jQuery);

//slide in panel
$(document).ready(function() {
	$(".trigger").click(function() {
		$(".panel").toggle("fast");
		$(this).toggleClass("active");
		return false;
	});
});
