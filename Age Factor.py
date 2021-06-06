# create the initial variables below
age = 28
sex = 0
bmi = 26.2 
num_of_children = 3
smoker = 0
# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(new_insurance_cost) + " dollars.")
# Difference
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("People who are four years older have estimated insurance costs that are " + str(change_in_insurance_cost) + " dollars different, where the sign of " + str(change_in_insurance_cost) + " tells us whether the cost is higher or lower.")