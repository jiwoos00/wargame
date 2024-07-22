<?php
$val_id="admin";
$val_pw="nimda";
for($i=0;$i<20;$i++){
	$val_id=base64_encode($val_id);
    	$val_pw=base64_encode($val_pw);
}
$val_id=str_replace("1","!",$val_id);
$val_id=str_replace("2","@",$val_id);
$val_id=str_replace("3","$",$val_id);
$val_id=str_replace("4","^",$val_id);
$val_id=str_replace("5","&",$val_id);
$val_id=str_replace("6","*",$val_id);
$val_id=str_replace("7","(",$val_id);
$val_id=str_replace("8",")",$val_id);

$val_pw=str_replace("1","!",$val_pw);
$val_pw=str_replace("2","@",$val_pw);
$val_pw=str_replace("3","$",$val_pw);
$val_pw=str_replace("4","^",$val_pw);
$val_pw=str_replace("5","&",$val_pw);
$val_pw=str_replace("6","*",$val_pw);
$val_pw=str_replace("7","(",$val_pw);
$val_pw=str_replace("8",")",$val_pw);

$id = $val_id;
$pw = $val_pw;

echo $id."\n";
echo $pw."\n";

$decode_id=$id;
$decode_pw=$pw;

$decode_id=str_replace("!","1",$decode_id);
$decode_id=str_replace("@","2",$decode_id);
$decode_id=str_replace("$","3",$decode_id);
$decode_id=str_replace("^","4",$decode_id);
$decode_id=str_replace("&","5",$decode_id);
$decode_id=str_replace("*","6",$decode_id);
$decode_id=str_replace("(","7",$decode_id);
$decode_id=str_replace(")","8",$decode_id);

$decode_pw=str_replace("!","1",$decode_pw);
$decode_pw=str_replace("@","2",$decode_pw);
$decode_pw=str_replace("$","3",$decode_pw);
$decode_pw=str_replace("^","4",$decode_pw);
$decode_pw=str_replace("&","5",$decode_pw);
$decode_pw=str_replace("*","6",$decode_pw);
$decode_pw=str_replace("(","7",$decode_pw);
$decode_pw=str_replace(")","8",$decode_pw);

for($i=0;$i<20;$i++){
  $decode_id=base64_decode($decode_id);
  $decode_pw=base64_decode($decode_pw);
}


echo $decode_id;
echo $decode_pw;
?>
