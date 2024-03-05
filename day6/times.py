times_brasileirao = (
    "Flamengo",
    "Palmeiras",
    "Atlético Mineiro",
    "Fortaleza",
    "Athletico Paranaense",
    "Ceará",
    "Santos",
    "Internacional",
    "Atlético Goianiense",
    "Bahia",
    "Corinthians",
    "Fluminense",
    "Juventude",
    "Sport",
    "São Paulo",
    "América Mineiro",
    "Cuiabá",
    "Grêmio",
    "Chapecoense",
    "Bragantino"
)

#for i in times_brasileirao[:5]:
#    print(i)

#for i in times_brasileirao[-5:]:
 #   print(i)
    
# time_ordem_alfabetica = sorted(times_brasileirao)
# print(time_ordem_alfabetica)

for pos, i in enumerate(times_brasileirao):
    if i == "Chapecoense":
        print(f"{i} está na {pos}ª posição")
    