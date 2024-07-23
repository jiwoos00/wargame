<?php
for($i=0;;$i++){
	$ck=md5($i,true);
	if(strpos($ck, "'='")){
		echo $i."\n";
		echo $ck."\n";
		break;
	}
}
?>
