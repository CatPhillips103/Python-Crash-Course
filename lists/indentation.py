# Exercises

# Pizzas: Think of a least three kinds of your favourite pizza. Store these pizza names in a list, and then use a for loop
# to print the name of the pizzas.

# Modify your for loop to print a sentence using the name of the pizza instead of print just the name of the pizza. For each
# pizza you should have one line of output containing a simple statement like I like pepperoni pizza.

# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of
# three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas = ['Chicago', 'Neopolitan', 'St Louis', 'Detriot', 'Califonia']

for pizza in pizzas:
    print(f"I like {pizza}")

print(f"Pizza is my favourite dish of all time")
print(f"I like {pizzas[0]}")
print(f"I like {pizzas[-2]}")
print(f"I like {pizzas[-1]}")
print(f"I really love pizza!")
