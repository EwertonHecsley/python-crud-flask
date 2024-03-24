produtos = {
    1:{
        "descricao":"Cerveja Heineken 350ml",
        "embalagem":"lata",
        "fornecedor":"Heineken"
    },
    2:{ 
        "descricao":"Cerveja Heineken 600ml",
        "embalagem":"garrafa",
        "fornecedor":"Heineken"
    },
    3:{
        "descricao":"Bohemia 600ml",
        "embalagem":"garrafa",
        "fornecedor":"Ambev"
    }
}

def gerar_id():
    id = len(produtos) + 1
    return id

def cadasdastrar_produto(descricao,embalagem,fornecedor):
    id = gerar_id()
    produtos[id] = {
        "descricao":descricao,
        "embalagem":embalagem,
        "fornecedor":fornecedor
    }
    return produtos[id]

def listar_produtos():
    return produtos

def listar_produto(id:int):
    if id in produtos:
        return produtos[id]
    else:
        return {}
    
def atualizar_produto(id:int,descricao:str,embalagem:str,fornecedor:str):
    if id in produtos:
        produtos[id]["descricao"] = descricao
        produtos[id]["embalagem"] = embalagem
        produtos[id]["fornecedor"] = fornecedor
        return produtos[id]
    else:
        return {}




