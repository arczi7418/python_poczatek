#zadanie 1
# import speed_calculator
#
# running_distance = int(input("Ile km przebiegłeś/przebiegłaś ?"))
# running_time = int(input("Ile godzin Ci to zajęło"))
#
#
# avg_speed = speed_calculator.speed_calculations(running_distance, running_time)
#
# print(f"Twoja prędkość biegu to: {avg_speed:.2f} km/h")
#
#
# #zadanie 2
import math

def calculate_c_len(a_len,b_len):
    return math.sqrt((a_len**2)+(b_len**2))

a = float(input("Podaj długość boku a "))
b = float(input("Podaj długość boku b "))

c = calculate_c_len(a,b)

print(f"Długość przeciwprostokątnej to {c:.1f} cm")
# zadanie 3

import calculations.investment
def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)
print("Kalkulator wartości lokaty z roczną kapitalizacją")

entry_value = ask_for_int_value("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
percentage = ask_for_int_value("Jakie jest oprocentowanie(%)?  ")
years = ask_for_int_value("Ile lat trwa lokata")

final_value = calculations.investment.calculate_deposit(entry_value, percentage, years)
print(f"Po {years} latach twoja lokata będzie warta {final_value:.2f} ")





