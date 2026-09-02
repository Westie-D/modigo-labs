def bmi_report(weight_kg, height_m):
   bmi = weight_kg / (height_m ** 2)
   bmi = round(bmi, 1) # TODO: calculate bmi, round it to 1 decimal place, determine the category,
   if bmi < 18.5:
      category = "Underweight"
   elif 18.5 <= bmi <= 24.9:
      category = "Normal weight"
   elif 25.0 <= bmi <= 29.9:
      category = "Overweight"
   else:
      category = "Obese"
   return f"BMI: {bmi}, Category: {category}"