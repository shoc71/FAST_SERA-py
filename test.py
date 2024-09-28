dict_div = {
    "L0" : {
        "General Topics" : {
        "Personal Notes" : [],
        "Music" : {
            "flute" : "hi"
        },
        "Gaming" : []
        }
    },
    "L1" : "Resources",
    "L2" : "think"
}

for key, value in dict_div.items():
    print(f"{key}: {len(value)} - {value}")

print("")

for key, value in dict_div["L0"].items():
    print(f"{key}: {value}")

print("")

for key, value in dict_div['L0']['General Topics'].items():
    print(f"{key}: {value}")

print("")

for key, value in dict_div['L0']['General Topics']['Music'].items():
    print(f"{key}: {value}")