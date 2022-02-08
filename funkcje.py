def spytne_potegowanie(podstawa, wykladnik):
    if  wykladnik == 0:
        return 1

    if wykladnik == 1:
        return podstawa

    polowa = spytne_potegowanie(podstawa, wykladnik//2)

    if wykladnik % 2 == 0:
        return polowa*polowa
    else:
        return polowa*polowa*podstawa

print(spytne_potegowanie(2,7))

