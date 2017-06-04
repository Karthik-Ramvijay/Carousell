<!DOCTYPE html>
<html>
<head>
	<title>Reddit Clone</title>
		<style type="text/css">
			
			table{
				  width: 95%;
				  empty-cells: hide;

			}
			td:hover{
				background: #c8ccc9;
			}

			div#rightdiv{

				float:right; 
				width: 50%;
			}
			div#ajaxresponse{

				float:left; 
				width: 50%;

			}
		</style>

</head>
<script type="text/javascript" src ="static/jquery-3.2.1.min.js" ></script>
<script type="text/javascript" src="static/script.js"></script>
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
				<div id="rightdiv">
						<table id ="nrml" border="5">
								<input id="sort_btn" type="submit" name="vote_calculation" value="Done_Votting">
								<tr>
									<thead><th>Topic</th><th width="1" height="2">UP VOTE</th><th width="1" height="2">Vote</th><th width="1" height="2">Down Vote</th>
									</thead>
								</tr>
								<tbody id="table_content">
								<!-- Topic will be submitted and topic will be added to the table Dynamically-->
								</tbody>
							
						</table>
				</div>
	</form>
</body>
</html>