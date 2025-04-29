from pyswip import Prolog

prolog = Prolog()

prolog.consult("kb.pl")

print(list(prolog.query("female(marge)")))
print(list(prolog.query("parent(X, bart)")))
print(list(prolog.query("mother(X, bart)")))
print(list(prolog.query("father(X, bart)")))