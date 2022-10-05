# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def get_dict_values(car):
  '''
      Si funkcija pasiema argumentus is audi dictionary ir paiima tik value argumentus ir atspauzdina tai sarase.
      :param audi:
      :return:
      Grazina
      audi dictionary values
      '''
  print(list(car.values()))


get_dict_values(audi)