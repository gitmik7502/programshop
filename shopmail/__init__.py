def mailnames():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\emails\\mail1.txt', 'r')
  mail = [mail1.read()]
  return mail
def passw():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\emails\\passmail1.txt', 'r')
  mail = [f'mail1 = {mail1.read()}']
  return mail
def card():
  mail1 = open('C:\\OS\\temp\\programshop\\shopmail\\mail_cards\\mail1.card.txt', 'r')
  mail = [f'mail1 = {mail1.read()}']
  return mail
