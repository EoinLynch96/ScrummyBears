def CtoF(C):
    Fahrenheit = 9.0 / 5.0 * C + 32
    return Fahrenheit

def main():
    Celsius = int(raw_input("Enter Celsius: "))
    print CtoF(Celsius)

if __name__ =='__main__':main()