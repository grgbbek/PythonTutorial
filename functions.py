# a collection of instructions
# collection of code

def function1():
    print("This is function first statement");
    print("second statement");
print("this is from outside the function");

# call a function
function1()

# a mapping
def function2(x):
    return 2*x

a = function2(3)

# if no arguments is passed to a function, it will return error
# b = function2()

# multiple arguments
def function3(x, y):
    return x + y

e = function3(2, 4)

def function4(x):
    print(x)
    print("still inside this function")
    return 3*x

f = function4(4)


# BMI Calculator
print("**********BMI Calculator**********")
name1 = "Bibek"
height1 = 2
weight_kg1 = 90

name2 = "Ram"
height2 = 1.8
weight_kg2 = 80

name3 = "Shyam"
height3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("BMI: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height1, weight_kg1)
result2 = bmi_calculator(name2, height2, weight_kg2)
result3 = bmi_calculator(name3, height3, weight_kg3)

print(result1)
print(result2)
print(result3)

# miles to km
print("******** Miles to km *********")
miles = input("Enter the miles")

def convertMileToKm(miles):
    km = 1.6*float(miles)
    print(km)

convertMileToKm(miles)
