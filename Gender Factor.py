# create the initial variables below
age = 28
sex = 0
bmi = 26.2 
num_of_children = 3
smoker = 0
# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Male vs. Female Factor
sex = 1
new_insurance_cost = 50 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("This person's insurance cost is " + str(new_insurance_cost) + " dollars.")
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")