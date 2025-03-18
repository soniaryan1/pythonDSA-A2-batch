a = 10
b = 20
c = 5

result = (a > b) or (not (c > b)) and (a + b == 30)

print(result)

#  (a>b) = false
# (not(c>b)) = (not(false)) = true
#  (a + b == 30) :- (10+20==30) -> true

# false or true = true
#  true and true = true
