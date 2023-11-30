print("Hello world")
print("Tesztkerdesek : ")

with open('tesztkerdesek.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        print(sor)