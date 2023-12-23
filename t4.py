# T4-> 
# Sotish:
# sell() metodi ichimlikning nomi va karta IDsi orqali sotadi.
# Metod ichimlik sotilgan ustun raqamini qaytaradi.
# Agar kredit ID yokiy ichimlik nomi hato bo'lsa -1.0 return giling.
# Agar ichimlik qolmagan bo'lsa -1.0 return giling.
# Agar kartada yetarli pul miqdori bo'lmasa -1.0 return giling.
# Odatiy holda (barcha shartlardan o'tsa):
# kartadan pul miqdorini kamaytiring,
# tanlangan ustundagi ichimlik sonini kirga kamaytiring.
# Eslatma: Mashina ichimlik mavjut boʻlgan birinchi ustunni tanlaydi.

class FillingMachine:
    def __init__(self):
        self.columns = {}
    
    def refillColumn(self, column, drink_name, quantity):
        if column in self.columns:
            self.columns[column][drink_name] = quantity
        else:
            self.columns[column] = {drink_name: quantity}
    
    def availableCans(self):
        total_cans = 0
        for column in self.columns.values():
            for quantity in column.values():
                total_cans += quantity
        return total_cans
    
    def sell(self, drink_name, card_id):
        for column, drinks in self.columns.items():
            if drink_name in drinks:
                if card_id in self.cards:
                    if self.cards[card_id] >= self.columns[column][drink_name] and self.columns[column][drink_name] > 0:
                        self.cards[card_id] -= self.columns[column][drink_name]
                        self.columns[column][drink_name] = 0
                        return column
                    else:
                        return -1.0
                else:
                    return -1.0
        return -1.0
    
class VendingMachine:
    def __init__(self):
        self.cards = {}
        self.fillingMachine = FillingMachine()
    
    def rechargeCard(self, card_id, credit):
        self.cards[card_id] = credit
    
    def getPrice(self, drink_name):
        return self.fillingMachine.getPrice(drink_name)
    
    def sell(self, drink_name, card_id):
        return self.fillingMachine.sell(drink_name, card_id)
    
vendingMachine = VendingMachine()

vendingMachine.rechargeCard(12, 12000)
vendingMachine.rechargeCard(21, 5600)
vendingMachine.rechargeCard(99, 15800)

vendingMachine.fillingMachine.refillColumn(1, "Coca Cola", 1)
vendingMachine.fillingMachine.refillColumn(2, "Water", 10)
vendingMachine.fillingMachine.refillColumn(3, "Water", 15)
vendingMachine.fillingMachine.refillColumn(4, "Water", 20)

print(vendingMachine.sell("Coca Cola", 12))
print(vendingMachine.sell("Water", 21)) 
print(vendingMachine.sell("Pepsi", 99))
print(vendingMachine.sell("Water", 12))
print(vendingMachine.sell("Water", 21))