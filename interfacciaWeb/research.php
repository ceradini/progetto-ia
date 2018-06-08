<!DOCTYPE html>
<html lang="it">

<?php
  include('components/header.php');
  include_once('functions/data.php');

  $users = get_users();
?>
<link href="css/select2.min.css" rel="stylesheet" />

<body class="fixed-nav sticky-footer bg-dark" id="page-top">
  <?php include('components/menu.php'); ?>
  <div class="content-wrapper">
    <div class="container-fluid">
      <!-- Breadcrumbs-->
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="index.php">Dashboard</a>
        </li>
        <li class="breadcrumb-item active">ricerca dettagliata</li>
      </ol>
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-random"></i> Selezione dettagliata</div>
        <div class="card-body">
          <div class="row">
            <div class="col-sm-12">
              <h4>Seleziona l'utente:</h4>
              <select class="select2" id="usersSelect">
                <?php foreach($users as $user_name => $val) : ?>
                  <option val="<?php echo $user_name; ?>"><?php echo $user_name; ?></option>
                <?php endforeach; ?>
              </select>
            </div>
          </div>
          <br />
          <button class="btn btn-success" id="btnGetResearchResult">VISUALIZZA <i class="fa fa-arrow-circle-right"></i></button>
        </div>
      </div>
      <div class="card mb-3 d-none" id="searchResult">
        <div class="card-header">
          <i class="fa fa-bar-chart"></i> Risultati</div>
        <div class="card-body">
          <table class="table table-bordered">
            <tbody>
              <tr>
                <th>Username</th>
                <td id="username"></td>
              </tr>
              <tr>
                <th>Hotel consigliato utilizzando opinione soggettive</th>
                <td id="casmin"></td>
              </tr>
              <tr>
                <th>Hotel consigliato utilizzando vincoli soft</th>
                <td id="scsp"></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <!-- /.container-fluid-->
    <!-- /.content-wrapper-->
    <?php include('components/footer.php'); ?>
    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fa fa-angle-up"></i>
    </a>
    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
    <!-- Page level plugin JavaScript-->
    <script src="vendor/chart.js/Chart.min.js"></script>
    <script src="vendor/datatables/jquery.dataTables.js"></script>
    <script src="vendor/datatables/dataTables.bootstrap4.js"></script>
    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin.min.js"></script>
    <!-- Custom scripts for this page-->
    <script src="js/sb-admin-datatables.min.js"></script>
    <script src="js/select2.min.js"></script>
    <script src="js/research.js"></script>
  </div>
</body>

</html>