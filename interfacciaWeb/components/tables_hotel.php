<?php
  include_once('functions/data.php');

  $hotels = get_hotels();
?>
<table class="table table-bordered dtable" id="dataTable" width="100%" cellspacing="0">
  <thead>
    <tr>
      <td>Name</td>
      <td>Città</td>
      <td>Codice postale</td>
    </tr>
  </thead>
  <tbody>
    <?php foreach($hotels as $hotel_name => $hotel_data) : ?>
      <tr>
        <th scope="row"><?php echo $hotel_name ?></th>
        <td><?php echo $hotel_data['city'] ?></td>
        <td><?php echo $hotel_data['cap'] ?></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>