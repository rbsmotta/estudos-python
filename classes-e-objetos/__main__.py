from modules.estados import Estados

estado = Estados("", "", "", 0, 0, "")

if __name__ == "__main__":
    
    estado.set_nome("São Paulo")
    print(estado.get_nome())

