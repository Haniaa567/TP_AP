import random
import datetime

# Fonction pour générer une opération aléatoire
def generate_operation():
    operations = ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION"]
    return random.choice(operations)
# Fonction pour générer une expression mathématique aléatoire
def generate_expression(operation):
    num1 = random.randint(0, 1000)
    num2 = random.randint(0, 1000)
    if operation == "DIVISION":
        num2 = random.randint(1, 1000)  #cas de division par 0 
    operator_map = {
        "ADDITION": "+",
        "SUBTRACTION": "-",
        "MULTIPLICATION": "*",
        "DIVISION": "/"
    }
    operator = operator_map.get(operation, )
    return f"{num1}{operator}{num2}"
# Fonction pour générer un grand nombre positif jsp le but de ce champ
def generate_large_number():
    return random.randint(10000, 100000)

# Fonction pour générer un nom d'utilisateur aléatoire
def generate_username():
    length = random.randint(6, 10) #j'ai supposer que le taille de nom entre 6 et 10 caractrer
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choices(characters, k=length))

# Fonction pour générer une date et heure aléatoire entrer 2010 et 2023
def generate_datetime():
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + datetime.timedelta(seconds=random_seconds)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# Génération du fichier avec 250000 lignes
def generate_file(filename, num_lines=250000):
    with open(filename, "w") as file:
        for _ in range(num_lines):
            operation = generate_operation()
            expression = generate_expression(operation)
            line = f"{operation},{expression},1,{generate_large_number()},{generate_username()},\"{generate_datetime()}\""
            file.write(line + "\n")

file = "file.txt"
print(f"Génération du fichier {file} avec 250,000 lignes...")
generate_file(file)
print("Fichier généré avec succès!")