<?php
  include_once('../functions/data.php');

  $casmin_results = get_scsp_results();
?>
<table class="table table-bordered dtable" id="usersTable" width="100%" cellspacing="0">
  <thead>
    <tr>
      <td>Username</td>
      <td>Hotel</td>
      <td>Risultato combinazione</td>
    </tr>
  </thead>
  <tbody>
    <?php foreach($casmin_results as $data) : ?>
      <?php if(strlen(trim($data[0])) > 0) : ?>
        <tr>
          <th scope="row"><?php echo $data[0]; ?></th>
          <td><?php echo $data[1]; ?></td>
          <td><?php echo $data[2]; ?></td>
        </tr>
      <?php endif; ?>
    <?php endforeach; ?>
  </tbody>
</table>