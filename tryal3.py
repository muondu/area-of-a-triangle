# def student_info(*args):
    # print(args)
# student_info('math','english')

# def gaming_info(*args):
#     print(args)
# gaming_info('minecraft','roblox','my life as a youtuber','Fortnite','Lords mobile','Make Sharon a gamer')
while True:
    input1 = input("Enter your name: ")
    input2 = input("Enter your age: ")
    def name_age(*kwargs):
        print(kwargs)
    name_age({input1:input2})