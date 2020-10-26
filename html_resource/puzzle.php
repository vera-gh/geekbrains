<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css"> 
	<script type="text/javascript">

		var score = 0;

		function checkAnswer(inputId, answers){
			var userAnswer = document.getElementById(inputId).value;
			userAnswer = userAnswer.toLowerCase();
			for(var i = 0; i < answers.length; i++){
				if(userAnswer == answers[i]){
					score++;
					break;
				}
			}
		}
		
		function checkAnswers() {

			checkAnswer("userAnswer1", ["0", "ни одного"]);
			checkAnswer("userAnswer2", ["крапива", "ожог крапивы"]);
			checkAnswer("userAnswer3", ["сапоги", "обувь","ботинки"]);

			alert("Поздравляем! Вы отгадали " + score + " загадок");

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
				
				<h1>Игра в загадки</h1>

				<div class="box">

					<?php 

						if(isset($_GET['userAnswer1']) && isset($_GET['userAnswer2']) && isset($_GET['userAnswer3'])){

							$userAnswer = $_GET["userAnswer1"];
							$score = 0;
							if($userAnswer == "0" || $userAnswer == "ни одного" ){
								$score++;
							}

							$userAnswer = $_GET["userAnswer2"];
							
							if($userAnswer == "крапива" || $userAnswer == "ожег крапивы" ){
								$score++;
							}

							$userAnswer = $_GET["userAnswer3"];
							
							if($userAnswer == "сапоги" || $userAnswer == "ботинки" ){
								$score++;
							}
							echo "Вы угадали"  . $score .  "загадки.";
						}



					 ?>

					<form method="GET">
						<p>Росло 3 берёзы.На каждой берёзе по 7 веток.На каждой ветке — по 3 яблока.Сколько всего яблок?</p>
						<input type="text" name="userAnswer1">

						<p>Ах, не трогайте меня: Обожгу и без огня!</p>
						<input type="text" name="userAnswer2">

						<p>Пустые отдыхаем,а полные шагаем.</p>
						<input type="text" name="userAnswer3">

						<br>
						<input type="submit" value="Ответить">
					</form>

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