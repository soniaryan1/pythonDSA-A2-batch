# start = int(input("enter start number =  "))
# end = int(input("enter end number = "))


# for i in range(start, end + 1):
#     print(i,end=" ")


start = int(input("enter start number =  "))
end = int(input("enter end number = "))
total = 0

for i in range(start, end + 1, 1):
    total = total + i
print(total)
