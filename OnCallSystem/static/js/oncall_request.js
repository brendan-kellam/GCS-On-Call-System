
//handles submit button
$(document).on("click", ".submit_button", function(e) {

	//pull data from form
	var date = getComp("inputDate");
	var week_id = getChoiceComp("inputWeek_id");
	var period = getChoiceComp("inputPeriod");
	var course_code = getChoiceComp("inputCourse_code");
	var slot = getChoiceComp("inputSlot");
	var description = getComp("inputDescription");

	//build confirm message
	var msg = "<b>Oncall Data:</b><br><br>"
	+ "<b>Date: </b> " + date + "<br>"
	+ "<b>Week: </b> " + week_id + "<br>"
	+ "<b>Period: </b>" + period + "<br>"
	+ "<b>Course: </b>" + course_code + "<br>"
	+ "<b>Slot: </b>" + slot + "<br>"
	+ "<b>Description: </b><br>  " + description + "<br>";

	//handle the confirm dialog (handled using bootbox)
	bootbox.dialog({

		//set prelim data
		message: msg,
		title: "Confirm Request",
		buttons: {

			//create cancel button
			cancel: {
				label: "Cancel",
				className: "btn-danger"
			},

			//create submit button
			submit: {
				label: "Submit",
				className: "btn-success", 
				callback: function() {

					//onclick, submit and process form
					document.getElementById("main-form").submit();
				}
			}
		}
	});

});

//returns the value of a html component
function getComp(id){
	return document.getElementById(id).value;
}

//returns value of select html component
function getChoiceComp(id){
	var index = document.getElementById(id).selectedIndex;
	var value = document.getElementById(id).options[index].innerHTML;
	return value;
}

$(function() {
    $( "#id_date_select" ).datepicker();
});