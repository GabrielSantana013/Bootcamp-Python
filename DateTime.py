from datetime import date, datetime, time

#====================================

#Primeira aula:

# x = date(2023, 7, 19) #data settada
# print(x)

# y = date.today() #data atual
# print(y)

# z = datetime.today() #data e hora atuais
# print(z)

# hora = time(10,10,40) #hora settada
# print(hora)

#======================================

#Segunda aula:

# from datetime import timedelta

# tipo_carro = 'P' #pequeno, medio, grande
# tempo_pequeno = 30
# tempo_medio = 45
# tempo_grande = 60
# data_atual = datetime.now() #pega o fuso horario

# if tipo_carro == 'P':
#     data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
#     print(f"O carro chegou: {data_atual} e ficará pronto as {data_estimada}.")
# elif tipo_carro == 'M':
#     data_estimada = data_atual + timedelta(minutes=tempo_medio)
#     print(f"O carro chegou: {data_atual} e ficará pronto as {data_estimada}.")
# else:
#     data_estimada = data_atual + timedelta(minutes=tempo_grande)
#     print(f"O carro chegou: {data_atual} e ficará pronto as {data_estimada}.")

# print(date.today() - timedelta(days=1))
# resultado = datetime(2024,6,26, 15,32,50) - timedelta(hours=1) #quando usar timedelta, tem que usar datetime
# print(resultado.time()) #pega só a hora 
# print(resultado.date()) #pega só a data

#======================================

#Terceira aula:

# data_hora_atual = datetime.now()
# data_hora_string = "2012-12-12 10:20"
# print(data_hora_atual)

# #Formatando o datetime
# mascara_ptbr = "%d/%m/%Y, %H:%M"
# print(data_hora_atual.strftime(mascara_ptbr))

# #Transformando String em Objeto Datetime
# mascara_en = "%Y-%m-%d %H:%M"
# print(datetime.strptime(data_hora_string, mascara_en))


#======================================

#pip install pytz

#Quarta aula:

#Exemplo com Pytz
# import pytz #fusos-horarios
# from datetime import timezone, timedelta

# data_hora = datetime.now(pytz.timezone("Europe/Oslo"))
# print(data_hora)

# #Exemplo sem Pytz

# data_sp = datetime.now(timezone(timedelta(hours=-3), "SP"))
# print(data_sp)

d = datetime.now().date()
print(d)
