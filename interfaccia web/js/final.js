$(document).ready(function() {
    var container = $('#finalTable');

    $.ajax( {
        type: 'GET',
        url: location.origin + '/components/tables_final.php'
    }).done(function(data) {
        container.html(data);
        $(".dtable").DataTable()
        $('.sk-cube-grid').addClass('d-none');
    });
});