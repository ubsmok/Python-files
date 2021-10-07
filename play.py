import math

# Hediin dotor too sanasniig asuuna
# Garah songoltiig hiih hurtel davtaj ajillana
# 1. Zuv hariult
# 2. Ih too sanasan
# 3. Baga too sanasan
# 4. Garah
ans = " "

while ans not in "4" or ans == "r":
    n = int(input("Ta hediin dotor too sanasan be ?"))

    print(
        "Bi tanii sanasan toog hamgiin ihdee {} udaagiin oroldlogoor oloh bolno".format(
            int(math.log(n, 2)) + 1
        )
    )
    low_n, high_n = 1, n
    i = 1  # Oroldlogo
    print(
        "Oroldlogo {} : Tanii sanasan too {} mun uu ?".format(i, (low_n + high_n) // 2)
    )
    ans = str(
        input("1. Zuw hariult.\n2. Ih too sanasan.\n3. Baga too sanasan.\n4. Garah.\n")
    )

    while ans not in "14":
        if ans not in "1234":
            ans = input(
                "Ta buruu utga oruulsan baina.\n1. Zuw hariult.\n2. Ih too sanasan.\n3. Baga too sanasan.\n4. Garah.\n"
            )
            continue
        i += 1
        if ans == "2":
            low_n = (low_n + high_n) // 2
        elif ans == "3":
            high_n = (low_n + high_n) // 2

        print(
            "Oroldlogo {} : Tanii sanasan too {} mun uu ?".format(
                i, (low_n + high_n) // 2
            )
        )
        ans = str(
            input(
                "1. Zuw hariult.\n2. Ih too sanasan.\n3. Baga too sanasan.\n4. Garah.\n"
            )
        )
    if ans == "1":
        # print("Ta daxin tiglohiig husvel {} tovshiig darna uu !".format("y"))
        ans = str(
            input(
                "Togloomoos garahiig husvel {} tovshiig\nUrgeljluuleh bol duriin too daraad {} darna uu !\n".format(
                    "4", "ENTER"
                )
            )
        )
        if ans == "4":
            ans = "4"
        else:
            ans = " "
