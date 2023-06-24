def greet(*name):
   i=0
   while i<len(name):
        i+=1
   print(name)
greet(["Rinki", "Vishal", "Kartik", "Bijender"])


def my_function(**kid):
   print("his last is"+kid["lname"])
my_function(fname="tobias",lname="refsnes")   