# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# exercise 1
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["TikTok", "Snapchat"])
it_companies.remove("Oracle")

# exercise 2
c = A.union(B)
print(c)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B

# exercise 3
age_set = set(age)
print("length of age set:", len(age_set))
print("length of age list:", len(age))
print("length of age set is less than length of age list:", len(age_set) < len(age))

string = "Hello, I am a teacher and I love to inspire and teach people"
string_list = string.split()
string_set = set(string_list)
print("length of string set:", len(string_set))
print("length of string list:", len(string_list))
print(
    "length of string set is less than length of string list:",
    len(string_set) < len(string_list),
)
print(string_set)
