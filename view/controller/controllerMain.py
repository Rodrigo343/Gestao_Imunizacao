from .model.pessoaDAO import PessoaDAO

def calculaImunizados():

    pessoaDAO = PessoaDAO()
    pessoas = pessoaDAO.listarPessoas()
    pessoaDAO.close()

    quantidadePessoas = len(pessoas)
    doses = []
    quantidade = []
    for i in pessoas:
        doses.append(i.doses)

    quantidade.append(doses.count(0))
    quantidade.append(doses.count(1))
    quantidade.append(doses.count(2))

    quantidade[0] = round((quantidade[0] / float(quantidadePessoas)) * 100)
    quantidade[1] = round((quantidade[1] / float(quantidadePessoas)) * 100)
    quantidade[2] = round((quantidade[2] / float(quantidadePessoas)) * 100)

    return quantidade

