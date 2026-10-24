from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- Home Page ----------
@app.route('/')
def home():
    return render_template('home.html')


# ---------- Predict Page ----------
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        # Get form data
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        activity = request.form['activity']
        goal = request.form['goal']

        # ---------------- BMI ----------------
        bmi = weight / ((height / 100) ** 2)

        # BMI Category
        if bmi < 18.5:
            bmi_status = "Underweight"
        elif bmi < 25:
            bmi_status = "Normal Weight"
        elif bmi < 30:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obese"

        # ---------------- Calories ----------------
        if activity == "low":
            calories = weight * 25
        elif activity == "moderate":
            calories = weight * 30
        else:
            calories = weight * 35

        if goal == "loss":
            calories -= 500
        elif goal == "gain":
            calories += 500

        calories = int(calories)

        # ---------------- Protein ----------------
        if goal == "loss":
            protein = round(weight * 1.8, 1)
        elif goal == "gain":
            protein = round(weight * 2.2, 1)
        else:
            protein = round(weight * 1.5, 1)

        # ---------------- Meal Plan ----------------

        if goal == "loss":

            breakfast = [
                "2 Boiled Eggs",
                "1 Bowl Oats",
                "1 Apple"
            ]

            lunch = [
                "2 Chapati",
                "Grilled Chicken / Paneer",
                "Mixed Vegetable Salad"
            ]

            snack = [
                "Green Tea",
                "Roasted Chickpeas"
            ]

            dinner = [
                "Grilled Fish / Paneer",
                "Steamed Vegetables",
                "1 Bowl Soup"
            ]

            recommendations = [
                "Drink at least 3 liters of water.",
                "Avoid sugary drinks.",
                "Walk 30-45 minutes daily.",
                "Eat more protein and fiber."
            ]

        elif goal == "gain":

            breakfast = [
                "Peanut Butter Sandwich",
                "Milk",
                "Banana"
            ]

            lunch = [
                "Rice",
                "Chicken Breast / Paneer",
                "Dal",
                "Vegetables"
            ]

            snack = [
                "Protein Shake",
                "Dry Fruits"
            ]

            dinner = [
                "Rice or Chapati",
                "Chicken/Fish/Paneer",
                "Curd"
            ]

            recommendations = [
                "Eat every 3-4 hours.",
                "Lift weights regularly.",
                "Sleep 8 hours daily.",
                "Increase healthy calories."
            ]

        else:

            breakfast = [
                "Oats",
                "Milk",
                "Banana"
            ]

            lunch = [
                "2 Chapati",
                "Dal",
                "Vegetables"
            ]

            snack = [
                "Fruits",
                "Nuts"
            ]

            dinner = [
                "Soup",
                "Paneer / Chicken",
                "Salad"
            ]

            recommendations = [
                "Maintain a balanced diet.",
                "Exercise regularly.",
                "Stay hydrated.",
                "Sleep well."
            ]

        return render_template(
            "result.html",
            bmi=round(bmi, 2),
            bmi_status=bmi_status,
            calories=calories,
            protein=protein,
            breakfast=breakfast,
            lunch=lunch,
            snack=snack,
            dinner=dinner,
            recommendations=recommendations,
            goal=goal
        )

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)