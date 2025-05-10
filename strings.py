origin = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг челов\
ека. А у нас управдом — друг человека!"

#number of simbols
print(len(origin))
#reverse
print(origin[::-1])
#first big letter
print(origin.title())
#all symbols are low
print(origin.lower())
#Найти число вхождений "нд", "ам", "о" в строку
print(origin.count("нд"))
print(origin.count("ам"))
print(origin.count("о"))
s = origin.split(" ")
print(s)
s = s[::-1]
print(s)
s = " ".join(s)
print(s)