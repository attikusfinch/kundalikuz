# Больше примеров есть на странице Wiki - https://github.com/paracosm17/dnevnikru/wiki

from kundalikuz import Kundalik

login = "login"
password = "password"
dairy = Kundalik(login=login,
                password=password)

print(dairy.marks())