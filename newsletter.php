<?php
	$to = "yourmail@provider.com"; /*Your Email*/
	$subject = "Suscription from the landing - Newsletter "; /*Issue*/
	$date = date ("l, F jS, Y"); 
	$time = date ("h:i A"); 	
	$Email=$_REQUEST['Email'];

	$msg="
	Name: $_REQUEST[Name]
	Email: $_REQUEST[Email]
	
	Suscription from website on date  $date, hour: $time.";

	if ($Email=="") {
		echo "<div class='alert alert-error'>
  				<a class='close' data-dismiss='alert'>×</a>
  				<strong>Warning!</strong> Please enter your email.
			</div>
		
		";
	}	
	else{
		mail($to, $subject, $msg, "From: $_REQUEST[Email]");
		echo "<div class='alert alert-success'>
  				<a class='close' data-dismiss='alert'>×</a>
  				<strong>Thank you for your Suscription!</strong>
			</div>
		
		
		";	
	}
	
?>
