class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + tipPercent/100 + taxPercent/100)

purchase = Purchase(100)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print('Tax: ', tax)
print('Tip: ', tip)
print('Total: ', purchase.calculateTotal(taxPercent, tipPercent))