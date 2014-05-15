<?php
	$to = "yourmail@provider.com"; /*Your Email*/
	$subject = "Messsage from the landing"; /*Issue*/
	$date = date ("l, F jS, Y"); 
	$time = date ("h:i A"); 
	
		
	$Email= $_REQUEST['Email'];
	$firstName = $_REQUEST['Firstname'];
	$lastName = $_REQUEST['Lastname'];
	$country = $_REQUEST['Country'];

	$msg="
	Name: $firstName $lastName
	Email: $Email
	Country: $country
	Education Level: $_REQUEST[education]
	Courses: $_REQUEST[courses]
	
	Message sent from website on date  $date, hour: $time.\n
	
	$_REQUEST[Message]";

	if ($Email=="") {
		echo "<div class='alert alert-error'>
  				<a class='close' data-dismiss='alert'>×</a>
  				<strong>Warning!</strong> Please enter your email.
			</div>
		
		";
	}	
	elseif ($firstName=="" or $lastName=="" or $country=="") {
		echo "<div class='alert alert-error'>
  				<a class='close' data-dismiss='alert'>×</a>
  				<strong>Warning!</strong> Please fill all the fields.
			</div>";
	}	
	else{
		mail($to, $subject, $msg, "From: $_REQUEST[Email]");
		echo "<div class='alert alert-success'>
  				<a class='close' data-dismiss='alert'>×</a>
  				<strong>Thank you for your message!</strong>
			</div>
		
		
		";	
	}
	
?>
