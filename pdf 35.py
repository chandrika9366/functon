# Q35. Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".
def children():
    age=int(input("enter age"))
    if age<14:
        return "toddy"
    elif age<18:
        return "coke" 
    elif age<21:
        return "beer"
    else:
        return "whisky"
print(children())                       