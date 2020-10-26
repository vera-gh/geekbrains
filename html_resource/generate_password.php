<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css">
	<script type="text/javascript">
		function readInt(){
			var number = document.getElementById("userVar").value;
			return parseInt(number);
			
		}
		function passwordResult(){
			var userVar = readInt()
			var password = Math.random().toString(36).slice(-parseInt(userVar))
			alert(password);
		}
		
	</script>
</head>
<body>
	<div class="content">
		<?php
			include "menu.php"
		?>
				<div class="contentWrap">
		    <div class="content">
		        <div class="center">
					<h1>Генератор пароля</h1>
					<div class="box"> 
						<p id="info">Введите длину желаемого пароля</p>
						<input type="text" id="userVar">
						<br>
						<a href="#" onClick="passwordResult();" id="button">Сгенерировать</a>
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="footer">
		Copyright &copy; Andreeva Vera
	<div>
</body>
</html>