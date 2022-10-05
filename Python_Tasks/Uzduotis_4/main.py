# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Film:
    '''
    tai yra filmu klase kurioje kursime filmam orientuotus objektus ir metodus.
    '''
    def __init__(self, title, director, budget):
        '''
            trumpai konstruktorius
            :param title:
            :param director:
            :param budget:
            :return:
            grazina objekta
        '''
        self.title = title
        self. director = director
        self.budget = budget

    def was_expensive(self):
        '''
            jeigu budget > 100000000 , grazins true jeigu ne False
            :param budget: pasiima is konstruktoriaus buget value
            :return:
            grazina true / false
        '''
        if self.budget > 100000000:
            print("True")
            return True
        else:
            print("False")
            False



film1 = Film("Riteriai", "Jodvyga", 100000000000000)
film2 = Film("Trys Drugeliai", "Kestas", 100000)
film1.was_expensive()
film2.was_expensive()