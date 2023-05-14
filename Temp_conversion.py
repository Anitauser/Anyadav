def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# main code starts here
temperature = float(input("Enter temperature: "))
unit = input("Enter temperature unit (C or F): ")

if unit == 'C':
  fahrenheit = celsius_to_fahrenheit(temperature)
  #print(temperature,unit, "is equal to",fahrenheit ,'F')
  print("{:.2f}°C is equal to {:.2f}°F".format(temperature, fahrenheit))
elif unit == 'F':
  celsius = fahrenheit_to_celsius(temperature)
  #print(temperature,unit, "is equal to",'c')
  print("{:.2f}°F is equal to {:.2f}°C".format(temperature, celsius))
else:
  print("Invalid unit entered. Please enter 'C' or 'F'.")