def vokon_zählen (x):
    x_lower = x.lower()
    x_lower_list = list(x_lower)
    vokale = "aeiou"
    
    v = []
    k = []
    
    for b in x_lower_list:
        # prüfen ob b ein Buchstabe ist
        if b.isalpha():
            k.append(b)
        #prüfen ob b ein Vokal ist
        if b in vokale:
            v.append(b)
    return f"Es gibt im String {x} {len(v)} Vokale und {len(k)-len(v)} Konsonanten. "

print (vokon_zählen("Berlin I love you!"))
            
    
