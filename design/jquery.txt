/* jquery to list blog detail */

$(document).ready(function() {
	
	$('#blogs a').click(function(e) {
		var url = $(this).attr('href');
		console.log('query log at: ' + url);
		//$('#biography').load(url);
		e.preventDefault();
	});
	
});