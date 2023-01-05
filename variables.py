#THIS IS A BAD EXMP
#'my_variable = "First dd this is a example about "
#'print(my_variable)'

# first use with variables

first_variable_string = "String "
print(first_variable_string)

second_variable = "2"
print(second_variable)

init_str_variable = str(second_variable)
print(init_str_variable)
print(type(init_str_variable))

#concatection with one print
print(first_variable_string, second_variable, init_str_variable)
print("this is value of :", second_variable)

# amount of letters
print(len(first_variable_string))

#variables only 1 line "not use this "

name, lastname, alias, age = "Gabriel", "Blanco", "Gabo" , 15
print("My name is:", name, lastname,"and my alias is", alias, ". and my age is:", age,)


#inputs examples

first_name = input('Como te llamas?: ')
age = input('Cual es tu edad: ? ')
job = input("en donde trabajas: ? ")

print("hola", first_name)
print("tu edad es de", age)
print("trabajas en", job)

