<?php
$defaultdata = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff")); 
function xor_decrypt($in) {
  if ($in != ''){
  	$text = $in;
  	$key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));}
  else{
  	$text = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
  	$key = "qw8J";}
  
  // Iterate through each character
  $outText = '';
  for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
  }
return $outText;
}
 
print "Key is currently unknown.\n OriginalData ^ Key = CipherText\n\t";
print " so that also means,\n OriginalData ^ Ciphertext = Key\n Therefore the key will repeat itself: ";
print xor_decrypt(base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="));
print "\nNow that we know the key lets create a new cookie to display the password: \n";
print base64_encode(xor_decrypt(""));
print "\n";
?>