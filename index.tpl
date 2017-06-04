<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form id="form1" method="POST">
					<center><h1>Reddit Clone</h1><br></center>
				<div style="float:left; width:50%;">
					<h2>Please Submit the Topic here:</h2>
				
					<textarea name="topictxt" id="topictxt" rows="4" cols="50" maxlength="255">
					</textarea>
					<br><br/>
					<input type="submit" name="Submit_Topic" id="Submit_Topic" value="Submit Topic">
					<br><br>
					<div id="ajaxresponse">
						<!-- Sorted Table contains the Topic in descending order will be Created dynamically-->
					</div>
				</div>
	</form>
</body>
</html>