a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
print(a == 0 or b == 0 or c == 0 or "нет нулевых значений")
print(a or b or c or "введены все нули")
if a > b + c:
    print("a - b - c = ",  a - b - c)
if a < b + c:
    print("b + c - a = ",  b + c - a)
if a > 50 and (b > a or c > a):
    print("Marty")
if a > 5 or (b, c == 7):
    print("Bruno")