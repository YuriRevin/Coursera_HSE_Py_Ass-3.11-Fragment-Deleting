w = input()
si = w.find('h')
ei = w.rfind('h')
print(w[:si] + w[ei+1:])
