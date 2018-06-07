$(document).ready(function() {
    $('.select2').select2();

    $('body').on('click','#btnGetResearchResult',function(){
    	var user = $('#usersSelect').val();

    	$.ajax( {
            type: 'GET',
            url: location.origin + '/functions/ajax.php',
            data:{
                user: user
            }
        }).done(function(data) {
        	data = JSON.parse(data);
        	var search_result = $('#searchResult');

        	search_result.find('#username').html(data['username']);
        	search_result.find('#casmin').html(data['casmin']);
        	search_result.find('#scsp').html(data['scsp']);
        	search_result.removeClass('d-none');
        });
    });
});