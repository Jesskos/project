{% extends 'base.html' %}

{% block title %}Find Recipes {% endblock %}

{% block content %}
<script src="https://code.jquery.com/jquery-3.2.1.min.js"> </script>

<h2> Hello, {{ session["name"] }} . Please find recipes here! </h2>
<h3> Please search for recipes using our cool API! </h3>

<button id="lowpotassium"> Low Potassium </button>
<p> 
	<ul>
		<li><b>Recipe Name: </b><span id='recipename'></span></li>
		<li><b>Recipe Link: </b><span id='recipelink'></span></li>

     </ul>
	</p>

<script>

	function showLowPotassiumRecipes(results) {

		$('#recipename').html(results["q"]);
		$('#recipelink').html(results["hits"][0]["recipe"]["label"])

	}

	function getLowPotassiumRecipes(evt) {
		$.get('https://api.edamam.com/search?q=tofu&app_id=701b2057&app_key=9f957ee3872be9ddfbadfd3ee005f3a2&nutrients[K]=200', showLowPotassiumRecipes);
	}

	$("#lowpotassium").on('click', getLowPotassiumRecipes);

</script>

{% endblock %}