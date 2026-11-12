import math
print("==========================================")
print("       ENGINEERING CALCULATION TOOL       ")
print("==========================================")
a = float(input("Enter a numerical value:"))
b = float(input("Enter an exponent:"))
c = float(input("Enter a decimal measurement:"))
p = pow(a,b)
s = math.sqrt(a)
ceil = math.ceil(c)
f = math.floor(c)


print("--- Results ---")
print(f"Value          :{a:.1f}")
print(f"Exponent       :{b:.1f}")
print(f"Power (pow)    :{p:.1f}")
print(f"Square (sqrt)  :{s:.4f}")
print(f"Decimal value  :{c}")
print(f"Ceil value     :{ceil}")
print(f"Floor value    :{f}")


