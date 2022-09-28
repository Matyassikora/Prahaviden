import requests

#r = requests.get("https://api.telegram.org/bot5725334288:AAF-Kd7nadnASAuMZWLY2ExVGWV1TiNzLvY/sendMessage?chat_id=-808605900&text={x}")
#x = input()


#enter message
msg = input()
#send message
r = requests.post("https://api.telegram.org/bot5725334288:AAF-Kd7nadnASAuMZWLY2ExVGWV1TiNzLvY/sendMessage?chat_id=-704631232&text="+msg)
