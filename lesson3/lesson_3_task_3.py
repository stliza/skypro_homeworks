from adresses import Address
from mailing import Mailing

address1 = Address("199206", "St.P", "Morskaya", "5", "10")
address2 = Address("202206", "Moscow", "Rechnaya", "10", "5")

mailing = Mailing(address1, address2, "3800", "AF-11-123-456" )

print(f"Отправление {mailing.track} из {mailing.to_adress.index},"
      f" {mailing.to_adress.city}, {mailing.to_adress.building},"
      f" {mailing.to_adress.flat} - в {mailing.from_adress.index},"
      f" {mailing.from_adress.city}, {mailing.from_adress.building},"
      f" {mailing.from_adress.flat}. Cтоимость {mailing.cost} рублей.")