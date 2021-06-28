#conversor de medidas
medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a \n{}cm \n{}mm \n{}dm \n{}dam \n{}hm \n{}km '.format(medida,cm,mm,dm,dam,hm,km))

