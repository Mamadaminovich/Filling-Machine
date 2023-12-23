# # T3-> 
# Sotux Mashinani to'ldirish:
# Mashina 4 ta ustundan iborat
# Har bir ustunda ichimlikning turi va hozirda mavjud bo'lgan bankalar soni bor.
# Bitta ichimlik birnechta ustunda bo'lishi mumkin (bitta ustunda bitta turdagi ichimlik bo'lishi mumkin).
# Boshida ustunlar bosh bo'ladi.
# Ustunlar to'ldirilganda har bitta ustunda ichimlik turi va miqdori bo'ladi.
# Shu magsatda refillColumn() metodi yozilgan.
# Ustunlar 1 dan boshlab raqamlangan.
# Ustun ragami
# 1
# 2
# 3
# 4
# Ichimlik nomi Bankalar soni
# Coca Cola
# 1
# Suv
# 10
# 15
# 20
# Pepsi Suv
# availableCans() metodi orqali berilgan ichimlikdan mashinada nechta borligini aniqlash mumkin (soni).

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

fillingMachine = FillingMachine()

fillingMachine.refillColumn(1, "Coca Cola", 1)
fillingMachine.refillColumn(2, "Water", 10)
fillingMachine.refillColumn(3, "Water", 15)
fillingMachine.refillColumn(4, "Water", 20)
fillingMachine.refillColumn(4, "Pepsi", 5)

print(fillingMachine.availableCans())
