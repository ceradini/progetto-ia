<?php
  include_once('functions/data.php');

  $users = get_users();
?>
<table class="table table-bordered dtable" id="usersTable" width="100%" cellspacing="0">
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
        <td><?php echo $user_data['city'] != 'nan' ? $user_data['city'] : ''; ?></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>