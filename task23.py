# Напишите функцию котрый будет определять введенный год, высокосный или нет

# year = int(input("Enter your year: "))

# if year % 4 == 0:
#     print(f"Yes {year} is Yeap year! ")
# else:
#     print(f"No {year} is not Yeap year! ") 
       
def year(a):
    if a % 4 == 0:
        print(f"Yes {a} is Yeap year! ")
    else:
        print(f"No {a} is not Yeap year! ") 
print(year(a = int(input("Enter your year: "))))
