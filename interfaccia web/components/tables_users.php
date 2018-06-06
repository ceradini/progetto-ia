<?php
  // apre il file csv degli hotel, crea un array associativo con gli hotel (unici)
  $users = array();

  if(($handle = fopen("source/hotel.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
      $user_name = $data[17];

      if(!isset($users[$user_name]) && $user_name != ''){
        $users[$user_name] = array(
          'city' => $data[18]
        );
      }
    }

    fclose($handle);
  }
?>
<table class="table table-bordered" id="usersTable" width="100%" cellspacing="0">
  <thead>
    <tr>
      <td>Username</td>
      <td>Città</td>
    </tr>
  </thead>
  <tbody>
    <?php foreach($users as $user_name => $user_data) : ?>
      <tr>
        <th scope="row"><?php echo $user_name ?></th>
        <td><?php echo $user_data['city'] ?></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>