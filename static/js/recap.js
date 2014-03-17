var recap = {
	
	init : function() {
		this.csrftoken = $("input[name='csrfmiddlewaretoken']").val();
	},
	
	getReqId : function(requirement) {
		var data = requirement.attr("id").split("_");
		return data[1];
	},
	
	updateCategory : function(requirement) {
		var category = requirement.closest(".category-column").data("category");
		var id = this.getReqId(requirement);
		requirement.attr("id", category + "_" + id);
		console.log(requirement.attr("id"));
	},

	updateIndexes : function(sortable) {
		var self = this;
		var url = 'updateindexes/';
		var data = $(sortable).sortable("serialize");
		$.ajax({
			type : "POST",
			url : url,
			data : {
				"data" : data,
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				console.log(msg);
			}
		});
	},
	
	changeStatus : function(requirement, status) {
		var self = this;
		var reqid = this.getReqId(requirement);
		$.ajax({
			type : "POST",
			url : 'changestatus/',
			data : {
				"req_id" : reqid,
				"status" : status,
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				msg = msg.split("#");
				var style_class = msg[0];
				var status = msg[1];
				var label = requirement.children(".status-label").removeClass().addClass("status-label " + style_class);
				label.children("small").html(status);
				console.log(msg);

			}
		});
	},
	
	changeAssignment : function(requirement) {
		var self = this;
		var reqid = this.getReqId(requirement);
		$.ajax({
			type : "POST",
			url : 'assign/',
			data : {
				"req_id" : reqid,
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				console.log(msg);

			}
		});
	},
	
	deleteReq : function(requirement) {
		var self = this;
		var reqid = this.getReqId(requirement);
		$.ajax({
			type : "POST",
			url : 'delete/',
			data : {
				"req_id" : reqid,
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				requirement.remove();
				console.log(msg);

			}
		});
	},
	
	addParticipant : function(participant, project) {
		var self = this;
		$.ajax({
			type : "POST",
			url : project + '/addparticipant/',
			data : {
				"new_user" : participant,
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				console.log(msg);
				var html = "<li>" + msg + "</li>";
				$("#newpartinputs").prepend(html); 
			}
		});
	},

	doAjax : function(requirement) {
		var self = this;
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
				"csrfmiddlewaretoken" : self.csrftoken,
			},
			success : function(msg) {
				console.log(msg);
			}
		});
	},
	
};

recap.init();

$(function() {
	$(".inner-container").sortable({
		connectWith : ".inner-container",
		containment : $("#content"),
		update : function(event, ui) {
			//prevent calling calling the method twice
			if (!ui.sender) {
				recap.updateCategory(ui.item);
				recap.doAjax(ui.item);
			}
			recap.updateIndexes(this);
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

//Attach event listeners for context menu actions.
$(function() {
	$(".inner-container").on("click", ".dropdown-item", function(event) {
		var action = $(event.target).data("action");
		var requirement = $(event.target).closest(".requirement-container");
		switch(action) {
			case "delete":
				recap.deleteReq(requirement);
				break;
			case "edit":
				console.log("Edit Action!");
				break;
			case "assign_to_self":
				recap.changeAssignment(requirement);
				console.log("Assign to Self Action!");
				break;
			case "status_not_started":
			case "status_in_progress":
			case "status_impeded":
			case "status_done":
				console.log("Status: " + action);
				recap.changeStatus(requirement, action);
				break;
			default:
		}
	});
});

$(function() {
	$("#searchfield").keyup(function(event) {
		if(event.which == 13) {
			var participant = $(this).val();
			var project = $(this).data("project");
			recap.addParticipant(participant, project);
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
				position : ['auto', 40]
			});
		});
	});
})(jQuery);

//Slide in panel
$(document).ready(function() {
	$(".trigger").click(function() {
		$(".panel").toggle("fast");
		$(this).toggleClass("active");
		return false;
	});
});
