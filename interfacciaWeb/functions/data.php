<?php
  function get_hotels()
  {
    // apre il file csv degli hotel, crea un array associativo con gli hotel (unici)
    $hotels = array();

    if(($handle = fopen("source/hotel.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $hotel_name = $data[6];

        if(!isset($hotels[$hotel_name]) && $hotel_name != ''){
          $hotels[$hotel_name] = array(
            'city'    => $data[2],
            'cap'     => $data[7]
          );
        }
      }

      fclose($handle);
    }

    unset($hotels['name']);

    return $hotels;
  }

  function get_users()
  {
    // apre il file csv degli hotel, crea un array associativo con gli utenti (unici)
    $users = array();

    if(($handle = fopen("source/hotel.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 5000, ",")) !== FALSE) {
        $data = array_map("utf8_encode", $data);

        $user_name = $data[17];

        if(!isset($users[$user_name]) && $user_name != ''){
          $users[$user_name] = array(
            'city'     => $data[18]
          );
        }
      }

      fclose($handle);
    }

    unset($users['reviews.username']);

    return $users;
  }


  function get_final_results()
  {
    $finals = array();

    if(($handle = fopen("../source/finale.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if($data[0]){
          $finals[] = $data;
        }
      }

      fclose($handle);
    }

    unset($data[0]);

    return $finals;
  }

  function get_casmin_results()
  {
    $casmin = array();

    if(($handle = fopen("../source/casmin.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if($data[0]){
          $values = explode('/$/$/', $data[0]);

          $casmin[] = array($values[0],$values[1],$data[1]);
        }
      }

      fclose($handle);
    }

    unset($casmin[0]);

    return $casmin;
  }

  function get_scsp_results()
  {
    $scsp = array();

    if(($handle = fopen("../source/vincoliSoft.csv", "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if($data[0]){
          $values = explode('/$/$/', $data[0]);

          $scsp[] = array($values[0],$values[1],$data[1]);
        }
      }

      fclose($handle);
    }

    unset($scsp[0]);

    return $scsp;
  }

?>