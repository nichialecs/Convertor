from convert import (
    LungimeConvert, MasaConvert, TemperaturaConvert,
    VolumConvert, TimpConvert, VitezaConvert
)

def conversii_in_lot(lista_conversii):
    """
    primeste o lista de genul:
    [ {"categorie": "lungime", "valoare": 10, "din": "m", "in": "cm"}]
    si returnează o listă cu rezultatele gata de afișat
    """
    #ne folosim de clasele din convert.py
    convert = {
        "lungime": LungimeConvert(),
        "masa": MasaConvert(),
        "temperatura": TemperaturaConvert(),
        "volum": VolumConvert(),
        "timp": TimpConvert(),
        "viteza": VitezaConvert(),
    }

    rezultate = []

    for item in lista_conversii:
        categorie = item.get("categorie","").lower()
        val = item.get("valoare",0)
        din = item.get("din","")
        inn = item.get("in","")

        if categorie not in convert:
            rezultate.append(f"Categoria '{categorie}' nu exista.")
            continue

        convertor = convert[categorie]

        try:
            rez = convertor.converteste(val,din,inn)
            rezultate.append(f"{val} {din} = {rez} {inn}")
        except ValueError as eroare:
            rezultate.append(f"[Eroare la {val} {din}]: {eroare}")

    return rezultate

if __name__ == "__main__":
    #test
    date_test = [
        {"categorie": "lungime", "valoare": 5, "din": "km", "in": "m"},
        {"categorie": "viteza", "valoare": 100, "din": "km/h", "in": "mph"}
    ]

    print("Rezultate Batch:")
    for r in conversii_in_lot(date_test):
        print(r)