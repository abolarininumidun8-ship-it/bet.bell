
string_var = "Python"
print("Q1:", string_var)

print("Q2:", "Programming"[0])

print("Q3:", "Python"[-1])

print("Q4:", "Programming"[3:7])

print("Q5:", "Hello World"[::-1])

print("Q6:", "ABCDEFGH"[::2])

print("Q7:", "hello".upper())

print("Q8:", "PYTHON".lower())

print("Q9:", "  Ada Lovelace  ".strip())

print("Q10:", "Ada Lovelace".replace("Ada", "Grace"))


print("Q11:", "apple,banana,cherry".split(","))

print("Q12:", "-".join(["2026", "10", "28"]))


name = "Alice"
age = 25
print("Q13:", f"My name is {name} and I am {age} years old.")

print("Q14:", f"{95.5678:.1f}")

print("Q15:", "Hello\nWorld")

print("Q16:", "Name:\tAda")


print("Q17:", '"Hello"')


print("Q18:", "\\")

path = r"C:\Users\Ada"
print("Q19:", path)

print("Q20:", "Python".startswith("P"))

print("Q21:", "banana".count("a"))

print("Q22:", "Hello World".find("World"))


empty_list = []
print("Q23:", empty_list)


numbers = [10, 20, 30, 40]
print("Q24:", numbers)

mixed_list = ["hello", 42, True]
print("Q25:", mixed_list)

print("Q26:", ["apple", "banana", "cherry"][1])

print("Q27:", ["apple", "banana", "cherry"][-1])

print("Q28:", [10, 20, 30, 40, 50][1:3])

print("Q29:", [1, 2, 3, 4, 5][::-1])

lst_30 = ["apple", "banana"]
lst_30.append("mango")
print("Q30:", lst_30)

lst_31 = ["apple", "banana"]
lst_31.insert(1, "orange")
print("Q31:", lst_31)

lst_32 = ["apple"]
lst_32.extend(["kiwi", "grape"])
print("Q32:", lst_32)

lst_33 = ["apple", "banana", "cherry"]
lst_33.remove("banana")
print("Q33:", lst_33)


lst_34 = [1, 2, 3]
popped_last = lst_34.pop()
print("Q34:", popped_last)


lst_35 = [10, 20, 30]
popped_index = lst_35.pop(1)
print("Q35:", popped_index)

lst_36 = [1, 2, 3]
del lst_36[0]
print("Q36:", lst_36)

lst_37 = [5, 2, 9, 1]
lst_37.sort()
print("Q37:", lst_37)

lst_38 = [1, 2, 3, 4]
lst_38.reverse()
print("Q38:", lst_38)

print("Q39:", [1, 2, 2, 3, 2].count(2))


print("Q40:", ["apple", "banana", "cherry"].index("cherry"))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Q41:", matrix)

print("Q42:", [[1, 2, 3], [4, 5, 6], [7, 8, 9]][1][2])

print("Q43:", [x**2 for x in range(1, 6)])

print("Q44:", [x for x in range(11) if x % 2 == 0])

print("Q45:", [x for x in range(1, 21) if x % 3 == 0])

print("Q46:", [word[0] for word in ["Python", "Java", "C++"]])

print("Q47:", [x for x in range(1, 11) if x > 5])

print("Q48:", [char for char in "hello"])

print("Q49:", [x**2 for x in range(1, 11) if x % 2 == 0])

print("Q50:", [len(word) for word in ["apple", "banana", "cherry"]])