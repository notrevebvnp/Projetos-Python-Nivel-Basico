import calendar

calendar.setfirstweekday(calendar.SUNDAY)

print("=== GERADOR DE CALENDÁRIO ===")

while True:
    try:
        mes = int(input("Digite o número do mês [1 a 12]: "))
        if 1 <= mes <= 12:
            break
        print("Mês inválido! O valor deve estar entre 1 e 12.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")

while True:
    try:
        ano = int(input("Digite o ano (ex: 2026): "))
        if ano > 0:
            break
        print("Ano inválido! Digite um ano maior que zero.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")

print(f"\n=== SEU CALENDÁRIO ({mes}/{ano}) ===")
print(calendar.month(ano, mes))