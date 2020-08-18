import time
input1 = int(input("Enter the base: "))
input2 = int(input("Enter the height: "))    
def area_of_triangle(base,height):
    area = base * height / 2
    print("Calculating the area...")

    time.sleep(2.5)
    return area
    

triangle = area_of_triangle(input1,input2)

"""If the area is greater than 10000"""
# if triangle > 1000:
#     triangle = input1 - input2
#     c = str(triangle)
#     print("The number is " + c)
# else:
#     c = str(triangle)
#     print("The number is " + c)
c = str(triangle)
print("The number is " + c)
