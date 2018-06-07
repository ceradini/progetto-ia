$(document).ready(function() {
    var container = $('#casminTable');

    $.ajax( {
        type: 'GET',
        url: location.origin + '/components/tables_casmin.php'
    }).done(function(data) {
        container.html(data);
        $(".dtable").DataTable();
        $('.sk-cube-grid').addClass('d-none');
    });
});