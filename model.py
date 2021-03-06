"Models and database for Recipe Storage"""

from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

##################################################################################################
# Model definitions

class Recipe(db.Model):
	""" Recipes found in search """

	__tablename__ = "recipes"

	recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	recipe_name = db.Column(db.String(200), nullable=False)
	recipe_image = db.Column(db.String(200), nullable=True)
	recipe_url = db.Column(db.String(200), nullable=False)
	blog_url = db.Column(db.String(200), nullable=True)
	ingredients_list = db.Column(db.String(2000), nullable=False)

	# can covert to 'blob'
	recipe_yield = db.Column(db.Integer, nullable=True)
	calories = db.Column(db.Integer, nullable=False)
	carbohydrates = db.Column(db.Integer, nullable=True)
	protein = db.Column(db.Integer, nullable=True)
	fiber = db.Column(db.Integer, nullable=True)
	fat = db.Column(db.Integer, nullable=True)
	potassium = db.Column(db.Integer, nullable=True)
	phosphorus = db.Column(db.Integer, nullable=True)
	sodium = db.Column(db.Integer, nullable=True)
	iron = db.Column(db.Integer, nullable=False)
	saturated_fat = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<Recipe recipe_id={} recipe_name={} recipe_image={} recipe_url={} blog_url ={} ingredients_list={} recipe_yield ={} calories={} \
		carbohydrates={} protein ={} fiber={} fat={} potassium={} phosphorus={} sodium={}, iron={}, saturated_fat={}>".format(self.recipe_id, 
			self.recipe_name.encode('ascii', 'ignore'), self.recipe_image.encode('ascii', 'ignore'), self.recipe_url.encode('ascii', 'ignore'), self.blog_url.encode('ascii', 'ignore'), self.ingredients_list.encode('ascii', 'ignore'), self.recipe_yield, self.calories, 
			self.carbohydrates, self.protein, self.fiber, self.fat, self.potassium, self.phosphorus, self.sodium, self.iron, self.saturated_fat) # pragma: no cover

class RecipeLabel(db.Model):
	""" Nutrition and Diet Labels on Recipes """

	__tablename__ = "recipes_labels"

	recipes_nutrition_label_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
	diet_label = db.Column(db.String(30), nullable=True)

	recipe = db.relationship("Recipe", backref="recipes_labels")

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<RecipeLabel recipes_nutrition_label_id={} recipe_id={} diet_label ={}>".format(
			self.recipes_nutrition_label_id, self.recipe_id, self.diet_label) # pragma: no cover


class Ingredient(db.Model):
	""" Ingredient in recipes """

	__tablename__ = "ingredients"

	ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	ingredient_name = db.Column(db.String(200), nullable=False)

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<Ingredient ingredient_id={} ingredient_name={}>".format(self.ingredient_id, self.ingredient_name) # pragma: no cover


class RecipeToIngredient(db.Model):
	""" Association table to connect recipes and ingredients """

	__tablename__ = "recipes_to_ingredients"

	recipe_to_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)

	recipe = db.relationship("Recipe", backref="recipes_to_ingredients")
	ingredient = db.relationship("Ingredient", backref="recipes_to_ingredients")

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<RecipeToIngredient recipe_to_ingredient_id={} recipe_id={} ingredient_id={}>".format(
			self.recipe_to_ingredient_id, self.recipe_id, self.ingredient_id) # pragma: no cover


class Amount(db.Model):
	""" Amount that an ingredient can have """

	__tablename__ = "amounts"

	amount_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	ingredient_amount = db.Column(db.String(10), nullable=False)

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<Amount amount_id={} ingredient_amount={}>".format(self.amount_id, self.ingredient_amount) # pragma: no cover


class AmountToIngredient(db.Model):
	""" Middle table between amounts and ingredients """

	__tablename__ = "amounts_to_ingredients"

	amount_to_ingredients_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	amount_id = db.Column(db.Integer, db.ForeignKey('amounts.amount_id'), nullable=False)
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)

	amount = db.relationship("Amount", backref="amounts_to_ingredients")
	ingredient = db.relationship("Ingredient", backref="amounts_to_ingredients")

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<AmountToIngredient amount_to_ingredients_id={} amount={} ingredient_id={}>".format(
			self.amount_to_ingredients_id, self.amount, self.ingredient_id) # pragma: no cover


class User(db.Model):
	""" class of users and passwords """

	__tablename__ = "users"
	
	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	fname = db.Column(db.String(20), nullable=False)
	lname = db.Column(db.String(20), nullable=False)
	user_email = db.Column(db.String(60), nullable=False)
	user_password = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<User user_id={} fname={} lname ={} user_name={} user_password={}>".format(self.user_id, 
			self.fname, self.lname, self.user_email, self.user_password) # pragma: no cover

class UserToAllergy(db.Model):
	""" class of users and allergies """

	__tablename__ = "user_to_allergies"
	
	user_allergy_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
	allergy_name = db.Column(db.String(20), nullable=False)

	user = db.relationship("User", backref="user_to_allergies")

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<UserToAllergy user_allergy_id={} user_id={} allergy_name ={}".format(self.user_allergy_id, 
			self.user_id, self.allergy_name) # pragma: no cover


class UserToDiet(db.Model):
	""" class of users and allergies """

	__tablename__ = "user_to_diets"
	
	user_diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
	nutrient_name = db.Column(db.String(20), nullable=False)
	high_or_low = db.Column(db.String(20), nullable=False)
	nutrient_goal = db.Column(db.Integer, nullable=False)


	user = db.relationship("User", backref="users_to_diets")

	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<UserToDiet user_diet_id={} user_id={} nutrient_name ={} high_or_low = {} nutrient_goal = {}".format(self.user_diet_id, 
		self.user_id, self.nutrient_name, self.high_or_low, self.nutrient_goal) # pragma: no cover



class UserToRecipe(db.Model):
	""" Middle table connecting users and recipes """

	__tablename__ = "users_to_recipes"

	user_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

	user = db.relationship("User", backref="users_to_recipes")
	recipe = db.relationship("Recipe", backref=db.backref("users_to_recipes", order_by=user_recipe_id))


	def __repr__(self):
		""" Provide helpful representation of recipe object when printed"""

		return "<UserToRecipe user_recipe_id={} recipe_id={} user_id={}>".format(
			self.user_recipe_id, self.recipe_id, self.user_id) # pragma: no cover

###########################################################################################################
# Testing   

def example_data():
	"""Create some sample data, and test models"""

	pizza = Recipe(recipe_name='pizza', recipe_image='pizza.jpg', recipe_url='pizza.com', blog_url='pizza.blog.com',  
		ingredients_list="[]", recipe_yield=12, calories= 500, carbohydrates=60, protein=10, fiber=1, fat=30, potassium=200, phosphorus=230, sodium=1000,
		iron=4, saturated_fat=3)
	fruit_salad = Recipe(recipe_name='fruit salad', recipe_image='fruit.jpg', recipe_url='fruit.com', blog_url='fruit.blog.com', 
		ingredients_list="[]", recipe_yield=12, calories= 100, carbohydrates=15, protein=2, fiber=3, fat=10, potassium=190, phosphorus=200, sodium=50, 
		iron=1, saturated_fat=0)
	olive = Ingredient(ingredient_name='olive')
	onecan = Amount(ingredient_amount='1 can')
	harry = User(fname='Harry', lname='Potter', user_email='hpotter@hogwarts.edu', user_password='hufflepuff')
	user_to_pizza = UserToRecipe(recipe=pizza, user=harry)
	halfcup_to_milk = AmountToIngredient(amount=onecan, ingredient=olive)
	pizza_to_olive = RecipeToIngredient(recipe=pizza, ingredient=olive)
	low_fat = RecipeLabel(recipe=pizza, diet_label="low-fat") 
	sushi = Recipe(recipe_name='sushi', recipe_image='sushi.jpg', recipe_url='sushi.com', blog_url='sushi.blog.com', ingredients_list="[]", recipe_yield=9, 
	 calories= 500, carbohydrates=60, protein=10, fiber=1, fat=30, potassium=200, phosphorus=230, sodium=1000, iron=4, saturated_fat=3)
	user_to_lowcarb = UserToDiet(user=harry, nutrient_name="carbohydrates", high_or_low="high", nutrient_goal = 200)
	user_to_egg = UserToAllergy(user=harry, allergy_name="egg")



	db.session.add_all([pizza, olive, onecan, harry, user_to_pizza, halfcup_to_milk, pizza_to_olive, low_fat, sushi, user_to_egg, user_to_lowcarb])
	db.session.commit()

###########################################################################################################
def connect_to_db(app, uri='postgresql:///recipesdb'): # pragma: no cover
	""" Connect the database to our Flask App"""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = uri  
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # pragma: no cover
	app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
	db.app = app
	db.init_app(app)
	db.create_all()

if __name__ == "__main__":

	from server import app  # pragma: no cover
	connect_to_db(app)  # pragma: no cover
	print "Connected to DB."  # pragma: no cover








