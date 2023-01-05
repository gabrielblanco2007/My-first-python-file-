### Strings ###

my_string = "Mi String"
my_other_string = "My other String"

## count ##

print(len(my_string))
print(len(my_other_string))

##plus + plus math##

print(my_string + " " + my_other_string)

#line break method 
my_new_line_string = "This is a string\nwith a line break"
print(my_new_line_string)

#with a space in the sentence start 

my_new_line_string = "\tThis is a string with a tabulation"
print(my_new_line_string)

#with tabulation and line break

my_new_line_string = "\tThis is a string with \na tabulation"
print(my_new_line_string)

# Format

name, surname, age = "Gabriel", "Blanco", 15

print("My name is %s %s and my age is %s".format(name, surname, age))
print("My name is %s %s and my age is %s" %(name, surname, age))
