lst = []
lst5 = ["apple", "banana", "orange", "mango", "lemon"]
print(len(lst5))
print((lst5[0]), (lst5[2]), (lst5[4]))
mixed_data_types = ["Imam", 21, 165, "single", "E26QP"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[6])
it_companies.pop(4)
print(it_companies)
it_companies.insert(4, "Twitter")
it_companies[0] = "FACEBOOK"
print("#".join(it_companies))
print("Twitter" in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
del it_companies[4:]
print(it_companies)
del it_companies[1:3]
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
print(it_companies)
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)
full_stack = front_end.copy()
print(full_stack)
