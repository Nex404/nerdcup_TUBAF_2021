mensa_names = [
    "Auflaeufe und Pizzen",
    "mensaVital",
    "Selbstwahltheken Gemuese Pasta Salat",
    "tabula-CT und Wok",
    "Vegetarisch"
]

mensa_files = [f"./data/Mensa/{mensa}.csv" for mensa in mensa_names]

mensa_data = [
    {"name":mensa_names[index], 
    "filename": mensa_files[index]}
    for index in range(len(mensa_names))
]
