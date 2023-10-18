# The 3D Printing Cost Calculator

user_inputs = []
indv_print_cost = []
total_cost = 0


def calculator(number, choice):
  total_cost = 0
  filament_cost = float(input("\n\nPrice of Spool (in USD) >> "))
  filament_weight = int(input("\nWeight of Spool (in grams) >> "))
  print("")
  for i in range(number):
    user_inputs.append(int(input("Weight of Print #" + str(i + 1) + " >> ")))
    cost = round(((user_inputs[i] * filament_cost) / filament_weight),
                 ndigits=2)
    indv_print_cost.append(cost)
  for i in list(indv_print_cost):
    total_cost += i
  if choice == "total":
    return total_cost
  elif choice == "print":
    return indv_print_cost


print("Welcome to the 3D Printing Cost Calculator!")
number = int(input("\nHow many prints would you like to calculate?\n>> "))
choice = input(
  "\n\nWould you like to calculate total cost, or cost per print?\n\n(T) for Total\n(P) for Print\n\n>> "
)
if choice == "T" or choice == "t":
  total_cost = round(calculator(number, "total"), ndigits=2)
  print("\n\n=========RESULTS=========")
  print("Total Print Cost: $" + str(total_cost))
elif choice == "P" or choice == "p":
  print_costs = calculator(number, "print")
  print("\n\n=========RESULTS=========")
  for i in range(len(print_costs)):
    print("Print #" + str(i + 1) + ": $" + str(print_costs[i]))
    total_cost += print_costs[i]
    total_cost = round(total_cost, ndigits=2)
  print("\nTotal Print Cost: $" + str(total_cost))
