<html>
  <head>
  
    
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="author" content="colorlib.com">
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="css/main.css" rel="stylesheet" />
  </head>
  <body>



    <div class="s130">
<?php


$servername = "localhost";
$username = "root";
$password = "";
$database="raval";


// Create connection
$conn = new mysqli($servername, $username, $password,$database);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql ="SELECT total,positives FROM ray";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    
    $a = $row["total"];
    $b = $row["positives"];
    
    
  }
} else {
  echo "0 results";
}
$conn->close();


?>
<table height="350">
  <tr  height="50px" align="center">
    <td width="100px">
    Test Cases
    </td>
    <td width="150px">
    Failed Test Cases
    </td>
  </tr>
  <tr height="50px" align="center">
  <td width="100px"> <?php echo "$a" ?> </td>
    <td width="100px"> <?php echo "$b" ?> </td>

  </tr>
  <tr align="center">
    <td colspan="2" >
      <?php
      if($b < 1)
      {
        $filepath= 'images/congratulation.png'; 
      echo '<img src="'.$filepath.'">'; 
      }
      else
      {
        $filepath= 'images/warning.gif'; 
      echo '<img src="'.$filepath.'">'; 
      }
      ?>
    </td>
  </tr>
  <tr align="center">
  <td colspan="2" >
      <?php
      if($b < 1)
      {
        echo "This URL is Safe, you can proceed";
      }
      else
      {
        echo "This URL is UnSafe";
      }
      ?>
    </td>
    
  </tr>
  <tr height="50px">"</tr>
  <tr height="50px"></tr>
  <tr height="50px">
    <td style="font-size: 10px;" colspan="2"> Do check out my<a href="https://github.com/yagnaraval"> GitHub </a></td>
    
  </tr>
</table >

    </div>
    <script src="js/extention/choices.js"></script>
    
  </body>
</html>

