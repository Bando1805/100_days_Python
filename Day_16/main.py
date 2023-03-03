from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Pokemon Name','Type']
table.add_row(['Pikachu','electric'])
table.add_row(['Squirtle','water'])
table.add_row(['Charmender','fire'])
table.align = 'l'
print(table)