def func():
    try:
        l = [1,5,6,7]
        i = int(input("Enter: "))
        print(l[i])
        return 1
    except:
        print("Some error")
        return 0
    finally:
        print("I am always executed")
    
x = func()
print(x)
