var updateCategory = function(requirement) {
	var category = requirement.closest(".category-column").data("category");
	var currentData = requirement.attr("id");
	var id = currentData.split("_")[1];
	requirement.attr("id", category + "_" + id);
	console.log(requirement.attr("id"));
};

var updateIndexes = function(sortable) {
	var url = 'updateindexes/';
	var data = $(sortable).sortable("serialize");
	$.ajax({
		type : "POST",
		url : url,
		data : {
			"data" : data,
			"csrfmiddlewaretoken" : $("input[name='csrfmiddlewaretoken']").val(),
		},
		success : function(msg) {
			console.log(msg);
		}
	});
};

var deleteReq = function(requirement) {
	var url = 'delete/';
	var data = requirement.attr("id").split("_");
	var reqid = data[1];
	$.ajax({
		type : "POST",
		url : url,
		data : {
			"req_id" : reqid,
			"csrfmiddlewaretoken" : $("input[name='csrfmiddlewaretoken']").val(),
		},
		success : function(msg) {
			requirement.remove();
			console.log(msg);
			
		}
	});
};

var doAjax = function(requirement) {
	var url = 'changecategory/';
	var data = requirement.attr("id").split("_");
	var reqid = data[1];
	var category = data[0];
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
		containment : $("#content"),
		update : function(event, ui) {
			//prevent calling calling the method twice
			if (!ui.sender) {
				updateCategory(ui.item);
				doAjax(ui.item);
			}
			updateIndexes(this);
		}
	}).disableSelection();
});

//Folding columns
$(function() {
	$(".minimize-toggle").click(function() {
		$(this).siblings(".category-column-heading").toggleClass("vertical-rotation");
		var icon = $(this).children();
		icon.toggleClass("icon-minus");
		icon.toggleClass("icon-plus");
		$(this).parent().siblings(".inner-container").fadeToggle(0);
		var catColumn = $(this).closest(".category-column");
		catColumn.toggleClass("span3");
		catColumn.toggleClass("span1");
	});
});

$(function() {
	$(".inner-container").on("click", ".dropdown-item", function(event) {
		var action = $(event.target).data("action");
		if(action === "delete") {
			console.log("Delete Action!");
			var requirement = $(event.target).closest(".requirement-container");
			deleteReq(requirement);
		}
		if(action === "edit") {
			console.log("Edit Action!");
		}
		if(action === "set_status") {
			console.log("Set status Action!");
		}
		if(action === "assign_to_self") {
			console.log("Assign to Self Action!");
		}
		
	});
});

//Create new popup
(function($) {
	$(function() {
		$('#create_new_button').on('click', function(e) {
			e.preventDefault();
			$('#create_new_prompt').bPopup({
				easing : 'easeOutBack', //uses jQuery easing plugin
				speed : 450,
				transition : 'slideDown',
				position: ['auto', 40]
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
