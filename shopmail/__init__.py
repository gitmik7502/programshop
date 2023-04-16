def mailnames():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\emails\\mail1.txt', 'r')
  mail = [mail1.read()]
  return mail
def passw():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\emails\\passmail1.txt', 'r')
  passmail = [f'{mail1.read()}']
  return passmail
def card():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\mail_cards\\mail1.card.txt', 'r')
  cardmail = [f'{mail1.read()[11:30]}', f'{mail1.read()[31:34]}', f'{mail1.read()[35:40]}', f'{mail1.read()[41:90]}']
  return cardmail
