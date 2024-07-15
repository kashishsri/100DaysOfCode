# Installing outside package and using it

from prettytable import PrettyTable
table = PrettyTable()
table.align = "c"
table.add_column("PokemonName", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)






