dict = {
    "aditi" : "human being",
    "table" : "an object"
}
print(dict["aditi"])

info = {"a": "f", "b": "g", "c" : "u"}
# print(info['j'])
# print(info.get('a'))
print(info.keys())

# for key in info.keys():
#     print(info[key])
print(info.items())


for key,value in info.items():
    print(f"the value corresponding the key {key} is{info[key]}")