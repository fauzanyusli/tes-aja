<!DOCTYPE html>
<html>
<head>
    <title>Data Komentar</title>
</head>
<body>
<?php
$nama= $_POST['nama'];
$email= $_POST['email'];
$komentar= $_POST['komentar'];
echo "<h1>Data Komentar Anda</h1>";
echo "<hr>";
if(!empty($nama))
{echo "Nama Anda         : $nama <br>";}
if(!empty($email))
{echo "Email Anda        : $email <br>";}
if(!empty($komentar))
{echo "Komentar anda     : $komentar <br>";}
?>
<a href="formkomentar.php">INPUT DATA LAGI</a>
?>
</body>
</html>