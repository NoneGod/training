sumhard = int(input("hard:"))
sumlog = int(input("log:"))
chicken = 0
rabbit = 0

if sumhard < 1:
    print("no chicken,no rabbit.")
elif sumhard == 1:
    if sumlog == 2:
        print("1 chicken,no rabbit.")
    elif sumlog == 4:
        print("no chicken, 1 rabbit.")
    else:
        print("what the fxxk?")
else:
    while sumlog != chicken * 2 + rabbit * 4:
        chicken += 1
        rabbit = sumhard - chicken
        if sumlog == chicken * 2 + rabbit * 4:
            print(chicken, "chicken", rabbit, "rabbit")
        elif rabbit < 0:
            print("What the FxxK!")
            break
        else:
            print("Not %s chicken,%s rabbit." % (chicken, rabbit))
            pass