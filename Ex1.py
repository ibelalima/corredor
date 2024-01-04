flash = 300.000
import random
jq = random.randint(flash,500.000)
ba = random.randint(flash,500.000)
ww = random.randint(flash,500.000)
dw = random.randint(flash,500.000)
jg = random.randint(flash,500.000)
mm = random.randint(flash,500.000)

if jq>ba and jq>ww and jq>dw and jq>jg and jq>mm:
    print("O vencedor foi Jesse Quick! sua velocidade foi de",jq,"Km/s")
if ba>jq and ba>ww and ba>dw and ba>jg and ba>mm:
    print("O vencedor foi Barry Allen! sua velocidade foi de",ba,"Km/s")
if ww>jq and ww>ba and ww>dw and ww>jg and ww>mm:
    print("O vencedor foi Wally West! sua velocidade foi de",ww,"Km/s")
if dw>jq and dw>ba and dw>ww and dw>jg and dw>mm:
    print("O vencedor foi Dr. Wells! sua velocidade foi de",dw,"Km/s")
if jg>jq and jg>ba and jg>ww and jg>dw and jg>mm:
    print("O vencedor foi Jay Garrick! sua velocidade foi de",jg,"Km/s")
if mm>jq and mm>ba and mm>ww and mm>dw and mm>jg:
    print("O vencedor foi Max Mercury! sua velocidade foi de",mm,"Km/s")