<html>
<head>
    <title>Form Data Diri</title>
</head>
</html>
<h1>Identitas</h1>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
<pre>
Isikan Nama     : <input type="text" name="nama">
Isikan No Telp  : <input type="text" name="notelp">
Isikan Alamat   : <textarea name="alamat" rows="5" cols="40"></textarea>
<input type="submit" value="TAMPIL"><input type="reset" value="BATAL">
</pre>
<?php
$nim = $_POST['nama'];
$telp = $_POST['notelp'];
$alamat = $_POST['alamat'];
if(!empty($nim)){
    echo "nama : $nim <br>";}
if(!empty($telp)){
    echo "nama : $telp <br>";}
if(!empty($alamat)){
    echo "nama : $alamat <br>";}
?>
</form>