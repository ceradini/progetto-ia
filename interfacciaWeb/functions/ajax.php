<?php
  if(isset($_GET['user'])) {
    $user = $_GET['user'];

    $data = get_user_data($user);
  }

  function get_user_data($user)
  {
    if(($handle = fopen("../source/finale.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if(trim($data[0]) == trim($user)){
          $result = array(
            'username' => $user,
            'casmin'   => $data[1],
            'scsp'     => $data[2]
          );

          echo json_encode($result);
          return;
        }
      }
    }
  }

?>