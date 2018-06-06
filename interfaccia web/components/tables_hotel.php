<?php
  // apre il file csv degli hotel, crea un array associativo con gli hotel (unici)
  $hotels = array();

  if(($handle = fopen("source/hotel.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
      $hotel_name = $data[6];

      if(!isset($hotels[$hotel_name]) && $hotel_name != ''){
        $hotels[$hotel_name] = array(
          'country' => $data[3],
          'city'    => $data[2],
          'cap'     => $data[7]
        );
      }
    }

    fclose($handle);
  }
?>
<table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
  <thead>
    <tr>
      <td>Name</td>
      <td>Stato</td>
      <td>Città</td>
      <td>Codice postale</td>
    </tr>
  </thead>
  <tbody>
    <?php foreach($hotels as $hotel_name => $hotel_data) : ?>
      <tr>
        <th scope="row"><?php echo $hotel_name ?></th>
        <td><?php echo $hotel_data['country'] ?></td>
        <td><?php echo $hotel_data['city'] ?></td>
        <td><?php echo $hotel_data['cap'] ?></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>