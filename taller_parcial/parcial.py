# *** ZONA DE CLASES Y LISTAS ***
class Cliente:
    def __init__(self, nombre, id, tel, dir):
        self.nombre, self.id, self.tel, self.dir = nombre, id, tel, dir
        self.bienes = []

class Bien:
    def __init__(self, nombre, cant, disp=True):
        self.nombre, self.cant, self.disp = nombre, cant, disp

clientes = []

# *** FUNCIONES ÚTILES ***
def buscar(id): return next((c for c in clientes if c.id == id), None)
def mostrar_c(c): print(f"{c.nombre} ({c.id}) Tel:{c.tel} Dir:{c.dir}")
def mostrar_b(b): print(f"{b.nombre} - Cant:{b.cant} - Disp:{'Sí' if b.disp else 'No'}")

# *** MENÚS ***
def menu_clientes():
    while True:
        op = input("\n[Clientes] 1.Agregar 2.Ver 3.Editar 4.Borrar 5.Salir: ")
        if op == "1":
            c = Cliente(input("Nombre: "), input("ID: "), input("Tel: "), input("Dir: "))
            print("Ya existe." if buscar(c.id) else (clientes.append(c), print("Agregado.")))
        elif op == "2":
            c = buscar(input("ID: "))
            mostrar_c(c) if c else print("No existe.")
        elif op == "3":
            c = buscar(input("ID: "))
            if c:
                c.nombre = input("Nuevo nombre: ")
                c.tel = input("Nuevo tel: ")
                c.dir = input("Nueva dir: ")
        elif op == "4":
            c = buscar(input("ID: "))
            clientes.remove(c) if c else print("No existe.")
        elif op == "5": break

def menu_bienes():
    while True:
        op = input("\n[Bienes] 1.Agregar 2.Listar 3.Borrar 4.Total 5.Salir: ")
        if op == "1":
            c = buscar(input("ID cliente: "))
            if c:
                b = Bien(input("Nombre: "), int(input("Cant: ")), input("¿Disponible? (s/n): ") == "s")
                c.bienes.append(b)
        elif op == "2":
            c = buscar(input("ID cliente: "))
            [mostrar_b(b) for b in c.bienes] if c else print("No existe.")
        elif op == "3":
            c = buscar(input("ID cliente: "))
            if c:
                nombre = input("Nombre bien: ")
                c.bienes = [b for b in c.bienes if b.nombre != nombre]
        elif op == "4":
            total = sum(b.cant for c in clientes for b in c.bienes)
            print(f"Total bienes: {total}")
        elif op == "5": break

# *** ZONA PRINCIPAL ***
def menu():
    while True:
        op = input("\n[Principal] 1.Clientes 2.Bienes 3.Salir: ")
        if op == "1": menu_clientes()
        elif op == "2": menu_bienes()
        elif op == "3": break

menu()
