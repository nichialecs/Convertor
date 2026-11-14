class Convert:
    #clasa mama din care o sa urmeze cele derivate pentru fiecare categorie
    def __init__(self):
        self.unitati_valide=[]

    def valid(self,val,din_val,in_val):
        try:
            val_float= float(val)
        except:
            raise ValueError("Valoarea introdusa nu este un numar.")

        if din_val not in self.unitati_valide or in_val not in self.unitati_valide:
            raise ValueError(f"Unitati gresite.\nFoloseste ceva din: {self.unitati_valide}")

        return val_float

    def converteste(self,val,din_val,in_val):
        #suprascriem ulterior pentru feicare clasa derivata
        pass


class LungimeConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide = ["mm", "cm", "dm", "m", "dam", "hm", "km", "in", "ft", "mi"]

        #luam metrul ca reper
        self.coef = {
            "mm": 0.001, "cm": 0.01, "dm": 0.1, "m": 1.0,
            "dam": 10.0, "hm": 100.0, "km": 1000.0,
            "in": 0.0254, "ft": 0.3048, "mi": 1609.344
        }

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        if val_float <0:
            raise ValueError("Lungimea nu poate fi negativa.")

        in_metri=val_float*self.coef[din_val]
        rez=in_metri/self.coef[in_val]

        return round(rez,3)

class MasaConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide = ["mg", "cg", "dg", "g", "dag", "hg", "kg", "t", "lb", "oz"]

        #reper kg
        self.coef = {
            "mg": 0.000001, "cg": 0.00001, "dg": 0.0001, "g": 0.001,
            "dag": 0.01, "hg": 0.1, "kg": 1.0, "t": 1000.0,
            "lb": 0.45359237, "oz": 0.02834952
        }

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        if val_float <0:
            raise ValueError("Masa nu poate fi negativa.")

        in_kg=val_float*self.coef[din_val]
        rez=in_kg/self.coef[in_val]

        return round(rez,3)

class TemperaturaConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide= ["C","F","K"]

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        #reper celsisus
        celsius=0
        if din_val == "C":
            celsius=val_float
        elif din_val == "K":
            celsius=val_float -273.15
        elif din_val == "F":
            celsius=(val_float -32.0) *5.0 / 9.0

        #acum dam rezultatul cerut
        if(in_val == "C"):
            return round(celsius,2)
        elif(in_val == "K"):
            return round(celsius+273.15,2)
        elif(in_val == "F"):
            return round((celsius*9.0/5.0)+32,2)

class VolumConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide = ["ml", "cl", "dl","l","dal","hl","kl","cm3","m3"]

        #reper litru
        self.coef = {
            "ml": 0.001, "cl": 0.01, "dl": 0.1, "l": 1.0,
            "dal": 10.0, "hl": 100.0, "kl": 1000.0,
            "cm3": 0.001, "m3": 1000.0
        }

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        if val_float <0:
            raise ValueError("Volumul nu poate fi negativ.")

        in_litri=val_float*self.coef[din_val]
        rez=in_litri/self.coef[in_val]

        return round(rez,3)

class TimpConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide = ["ms","s","min","h","zi"]

        #reper secunda
        self.coef = {
            "ms": 0.001, "s": 1.0, "min": 60.0, "h": 3600.0, "zi": 86400.0
        }

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        if val_float <0:
            raise ValueError("Timpul nu poate fi negativ.")

        in_secunde=val_float*self.coef[din_val]
        rez=in_secunde/self.coef[in_val]

        return round(rez,3)


class VitezaConvert(Convert):
    def __init__(self):
        super().__init__()
        self.unitati_valide = ["m/s", "km/h", "mph"]
        #reper m/s
        self.coef = {
            "m/s": 1.0, "km/h": 0.277778, "mph": 0.44704
        }

    def converteste(self,val,din_val,in_val):
        val_float= self.valid(val,din_val,in_val)

        if val_float <0:
            raise ValueError("Viteza nu poate fi negativa.")

        in_ms=val_float*self.coef[din_val]
        rez=in_ms/self.coef[in_val]

        return round(rez,3)



if __name__ == "__main__":
    convertorL=LungimeConvert()
    convertorM=MasaConvert()
    convertorT=TemperaturaConvert()
    convertorV = VolumConvert()
    convertorTimp = TimpConvert()
    convertorVit = VitezaConvert()

    print("Teste ce ar trebui sa dea bine:")
    print("Test lungime: 100 cm in m = ", convertorL.converteste(100, "cm", "m"))  # trb sa dea 1.0
    print("Test masa: 2.5 kg in g = ", convertorM.converteste(2.5, "kg", "g"))  # trb sa dea 2500.0
    print("Test temp: 0 C in F = ", convertorT.converteste(0, "C", "F"))  # trb sa dea 32.0
    print("Test temp: 0 C in K = ", convertorT.converteste(0, "C", "K"))  # 273.15
    # Teste pentru categoriile noi
    print("Test volum: 1 m3 in l = ", convertorV.converteste(1, "m3", "l"))  # trb sa dea 1000.0
    print("Test timp: 2 h in min = ", convertorTimp.converteste(2, "h", "min"))  # trb sa dea 120.0
    print("Test viteza: 100 km/h in m/s = ", convertorVit.converteste(100, "km/h", "m/s"))  # trb sa dea 27.778
    # print("Teste ce n ar trebui sa dea bine:")
    # convertorL.converteste(-5, "m", "cm")
    # convertorT.converteste(-300, "C", "K")
