from smartphone import Smartphone
catalog = []

phone_1 = Smartphone("Nokia", "3310", "+79123456789")
phone_2 = Smartphone("Redmi", "Note 10", "+79234567890")
phone_3 = Smartphone("Samsung", "Galaxy S24", "+79345678901")
phone_4 = Smartphone("Apple", "iPhone 15", "+79456789012")
phone_5 = Smartphone("Poco", "X6 Pro", "+79567890123")

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)


for smartphone in catalog:
    print(smartphone.brand, "-", smartphone.model,
          "-", smartphone.number)