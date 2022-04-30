


sual=[
    {"sual":"Shusa beyannamesi hansi ilde imzalanmisdir",
     "cavablar":[
         "2020",
         "2021",
         "2022",
         "2019"
         ],
        "duzgun cavab":"B"},
    {"sual":"Azerbaycanin daxil oldugu ilk beynelxalq teskilat hansidir",
    "cavablar":[
        "IKT", 
        "BMT",
        "ATET",
        "GUAM" ],
    "duzgun cavab":"A"}
    ]
for i in sual:
    butuntestler=f"""
    1. {sual["sual"]}
        A) {sual["cavablar"][0]}
        B) {sual["cavablar"][1]}
        C) {sual["cavablar"][2]}
        D) {sual["cavablar"][3]}  
    """


print(butuntestler)
cavab=input("cavabinizi daxil edin")
if cavab==sual["duzgun cavab"]:
    print(cavabiniz dogrudur)
else:
    print("cavabiniz sehvdir")

    