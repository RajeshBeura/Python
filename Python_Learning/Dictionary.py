dict={
    "name":"Rajesh",
    "cgpa":9.2,
    "age":26,

}

print(dict)
print(dict["name"])


info={
    "name":"Rajesh",
    "cgpa":9.2,
    "age":26,
    "score":{
        "chem":98,
        "phy":90,
        "math":95,
    }

}

print(info)
print(info["score"])
print(info.keys())
print(info.values())
print(info.items())

