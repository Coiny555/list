def main():
    HowMany = int(input("Enter how many numbers you want in this list: "))
    x = []
    for i in range(HowMany):
        num = int(input("Enter the number: "))
        x.append(num)
    
    for i in range(HowMany):
        if(x[i] < 5):
            print(x[i])

main()