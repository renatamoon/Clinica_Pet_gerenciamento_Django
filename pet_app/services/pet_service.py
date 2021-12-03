from ..models import Pet


def cadastrar_pet(pet):    
    pet_bd = Pet.objects.create(proprietario=pet.proprietario, nome=pet.nome, idade=pet.idade, categoria=pet.categoria, cor=pet.cor, peso=pet.peso, raca=pet.raca, genero=pet.genero)
    pet_bd.save()



# def editar_pet(pet, pet_novo):
    

# def listar_pet_id(id):