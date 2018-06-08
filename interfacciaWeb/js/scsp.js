$(document).ready(function() {
    var container = $('#scspTable');

    $.ajax( {
        type: 'GET',
        url: location.origin + '/components/tables_scsp.php'
    }).done(function(data) {
        container.html(data);
        $(".dtable").DataTable();
        $('.sk-cube-grid').addClass('d-none');
    });
});