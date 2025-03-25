# 1 to 10 ,, total

# total = 0
# i = 1
# while i <= 10:
#     total = total + i
#     i += 1
# print(total)


# start , end | start<end
#  start,end ---total
total = 0
start: int = int(input("enter start = "))
end: int = int(input("enter end = "))

i: int = start
while i <= end:
    total = total + i
    i += 1
print(f"addition of all number from {start} to {end} is {total}")
