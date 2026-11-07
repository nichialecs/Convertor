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
        self.unitati_valide = ["m", "cm", "mm", "km", "in", "ft", "mi"]

        #luam metrul ca reper
        self.coef={
            "m":1.0, "cm": 0.01, "mm": 0.001, "km": 1000.0,
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
        self.unitati_valide = ["kg", "g", "mg", "t", "lb", "oz"]

        #reper kg
        self.coef={
            "kg": 1.0, "g": 0.001, "mg": 0.000001,
            "t": 1000.0, "lb": 0.45359237, "oz": 0.02834952
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


if __name__ == "__main__":
    convertorL=LungimeConvert()
    convertorM=MasaConvert()
    convertorT=TemperaturaConvert()

    print("Teste ce ar trebui sa dea bine:")
    print("Test lungime: 100 cm in m = ", convertorL.converteste(100, "cm", "m"))  # trb sa dea 1.0
    print("Test masa: 2.5 kg in g = ", convertorM.converteste(2.5, "kg", "g"))  # trb sa dea 2500.0
    print("Test temp: 0 C in F = ", convertorT.converteste(0, "C", "F"))  # trb sa dea 32.0
    print("Test temp: 0 C in K = ", convertorT.converteste(0, "C", "K"))  # 273.15

    # print("Teste ce n ar trebui sa dea bine:")
    # convertorL.converteste(-5, "m", "cm")
    # convertorT.converteste(-300, "C", "K")
