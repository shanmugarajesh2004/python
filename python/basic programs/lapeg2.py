class laptop():
    chargertype = "C TYPE"
    @classmethod
    def charger(cls):
        cls.chargertype = "B TYPE"
        print(cls.chargertype)
    @staticmethod
    def info():
        print("DELL is a good laptop")    
a = laptop()

laptop.charger()

a.info()
        