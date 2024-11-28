# creo classe contoCorrente
class ContoCorrente:
    # inizializzatore/costruttore
    def __init__(self, nome, conto, importo):
        # attributi di istanza
        self.nome = nome
        self.conto = conto
        self.saldo = importo
    # metodo preleva
    def preleva(self, importo):
        self.saldo -= importo

    # metodo deposita
    def deposita(self, importo):
        self.saldo += importo

    # metodo descrizione
    def descrizione(self):
        print(self.nome, self.conto, self.saldo)

# creo istanze

c1 = ContoCorrente("Stefano", "fgbth23", 3000)
c1 = ContoCorrente("Fabrizio", "4tghty5", 2000)

c1.descrizione()
c2.descrizione()