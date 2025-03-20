# class intrest:
#     def calculateamount(amount, percentage, months):
#         percent = (amount * percentage) / 100
#         intrestt = percent * months

#         return intrestt + amount


# x = float(input("enter your amount = "))
# y = float(input("enter your percentt = "))
# z = float(input("enter your months = "))

# result = intrest.calculateamount(x, y, z)
# print(result)


class IntrestCalculater:
    def calculate(amount, percent, months):
        intrest = ((amount * percent) / 100) * months
        finalAmount = intrest + amount

        if intrestOrFinalAmount == "Intrest":
            return intrest
        else:
            return finalAmount


yourAmount = float(input("Enter your Amount :_ "))
yourPercent = float(input("Enter your Percent :_ "))
yourMonth = float(input("Enter your months :_ "))

print("Type any one")
intrestOrFinalAmount = input("Intrest/Final Amount ")

finalResult = IntrestCalculater.calculate(yourAmount, yourPercent, yourMonth)
print(finalResult)
