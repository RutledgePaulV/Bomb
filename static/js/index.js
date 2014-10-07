var FORM, PROGRESS_BAR;

/**
 * This handler allows us to kick off the progress bar and it will
 * make the appropriate requests and update itself until it reaches
 * one hundred percent.
 *
 * @param taskId
 */
var updateProgressBar = function (taskId) {
	_.registry.GET_PROGRESS.fire({taskId: taskId}, function (data) {
		var percentComplete = data.results[0].percentageComplete;
		PROGRESS_BAR.progressbar('value', percentComplete);

		if(percentComplete > 90) {
			$('.sending').hide();
			$('.complete').show();
		}
		else{
			setTimeout(function(){updateProgressBar(taskId);}, 1000);
		}
	});
};


/**
 * This handler submits the form and then begins updating the progress bar.
 */
var submitForm = function () {
	_.registry.QUEUE_TEXTS.fire(FORM.serialize(), function (data) {
		if (data.status === 'SUCCESS') {
			FORM.hide();
			$('.sending').show();
			updateProgressBar(data.results[0].taskId);
		}
	});
};

$(document).ready(function () {

	/**
	 * Inject CSRF token into all ajax requests.
	 */
	$.ajaxSetup({
			crossDomain: false, beforeSend: function (xhr, settings) {
				if (!Utils.csrfSafeMethod(settings.type)) {
					xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
				}
			}
		}
	);

	/**
	 * Request the available ajax commands.
	 */
	_.UpdateDefinitions();

	// setting a couple globals for reference in callbacks
	FORM = $('.form');
	PROGRESS_BAR = $('#progress');

	// initializing the progress bar.
	PROGRESS_BAR.progressbar({value: 0});

	// hiding currently irrelevant areas
	$('.complete').hide();
	$('.sending').hide();

	/**
	 * Adding the click handler onto the submit button.
	 */
	$('#send').click(submitForm);

});