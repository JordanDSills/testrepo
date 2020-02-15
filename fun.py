names1 = ["Jim", "Hank", "Sue", "Lily", "Tom"]
names2 = ["Hank", "Jim", "Tom", "Sue"]

for name in names1:
    match = False
    for n in names2:
        if name == n:
            match = True
    if match == False:
        print name
