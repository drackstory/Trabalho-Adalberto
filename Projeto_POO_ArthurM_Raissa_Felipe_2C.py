condicao = True
medicos = [{"Nome": "José", "CPF": "12345678910", "RG": "1", "CRM": "1", "Telefone": "9999999", "Endereço": "Rua do tiquin", "Sexo": "M", "Senha": "aeiou"}]
pacientes = [{"Nome": "Afonso", "Endereço": "Granjeiro", "Telefone": "40028922", "CPF": "111", "RG": "4", "Sexo": "F", "Convênio": "casa do cachaprego"}] 
convenios = [{"Nome": "Plano", "Telefone": "0000010", "Endereço": "Ali", "CNPJ": "101010", "Planos": "Nenhumkkkk"}]
compromissos = [{"Data": "", "Hora Inicial": "", "Hora Final": "", "Descrição": ""}] 
consultas = [{"Médico": "José", "Paciente": "Afonso", "Data": "Amanhã", "Hora": "10h"}]
    
while condicao:
    lang = int(input("1 - Cadastrar Médicos\n"
             "2 - Cadastrar Pacientes\n"
             "3 - Cadastrar Convênios\n"
             "4 - Buscar Médicos\n"
             "5 - Buscar Pacientes\n"
             "6 - Buscar Convênios\n"
             "7 - Alterar Médicos\n"
             "8 - Alterar Pacientes\n"
             "9 - Marcar Compromisso\n"
             "10 - Marcar Consulta\n"
             "11 - Emitir Relatorio\n"
             "12 - Encerrar Programa\n"
             "O que você deseja fazer?\n"))
    
    while lang > 12 or lang < 1:
        print("Escolha uma opção válida")
        lang = int(input("O que você deseja fazer?\n"))
    
    def cadastrarMedicos():
        nomeMedico = input("Digite o nome do médico: ")
        cpfMedico = input("Digite o CPF do médico: ")
        rgMedico = input("Digite o RG do médico: ")
        crm = input("Digite o CRM do médico: ")
        telefoneMedico = input("Digite o telefone do médico: ")
        enderecoMedico = input("Digite o endereço do médico: ")
        sexoMedico = input("Digite o sexo do médico: ")
        senha  = input("Digite a senha de acesso do médico: ")
        medicos.append({"Nome": nomeMedico, "CPF": cpfMedico, "RG": rgMedico, "CRM": crm, "Telefone": telefoneMedico, "Endereço": enderecoMedico, "Sexo": sexoMedico, "Senha": senha})
        print(f"Médico {nomeMedico} cadastrado com sucesso.")
        
    def cadastrarPacientes():
        nomePaciente = input("Digite o nome do paciente: ")
        enderecoPaciente = input("Digite o endereço do paciente: ")
        telefonePaciente = input("Digite o telefone do paciente: ")
        cpfPaciente = input("Digite o CPF do paciente: ")
        rgPaciente = input("Digite o RG do paciente: ")
        sexoPaciente = input("Digite o sexo do paciente: ")
        convenio = input("Digite o convênio ao qual o paciente está associado: ")
        pacientes.append({"Nome": nomePaciente, "Endereço": enderecoPaciente, "Telefone": telefonePaciente, "CPF": cpfPaciente, "RG": rgPaciente, "Sexo": sexoPaciente, "Convênio": convenio})
        print(f"Paciente {nomePaciente} cadastrado com sucesso.")
        
    def cadastrarConvenios():
        nomeConvenio = input("Digite o nome do convênio: ")
        telefoneConvenio = input("Digite o telefone do convênio: ")
        enderecoConvenio = input("Digite o endereço do convênio: ")
        cnpj = input("Digite o CNPJ do convênio: ")
        planos = input("Digite os planos do convênio: ")
        convenios.append({"Nome": nomeConvenio, "Telefone": telefoneConvenio, "Endereço": enderecoConvenio, "CNPJ": cnpj, "Planos": planos})
        print(f"{nomeConvenio} cadastrado com sucesso.")
        
    def buscarMedicos():
        escolha = int(input("Você quer buscar por nome ou CRM?\nDigite 1 para nome e 2 para CRM: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaMedico = input("Digite o nome do médico: ")
            for n in medicos:
                if n["Nome"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
        if escolha == 2:
            buscaMedico = input("Digite o CRM do médico: ")
            for n in medicos:
                if n["CRM"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
        
    def buscarPacientes():
        escolha = int(input("Você quer buscar por nome ou CPF?\nDigite 1 para nome e 2 para CPF: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaPaciente = input("Digite o nome do paciente: ")
            for n in pacientes:
                if n["Nome"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
        if escolha == 2:
            buscaPaciente = input("Digite o CPF do pacientes: ")
            for n in pacientes:
                if n["CPF"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
        
    def buscarConvenios():
        escolha = int(input("Você quer buscar por nome ou CNPJ?\nDigite 1 para nome e 2 para CNPJ: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaConvenio = input("Digite o nome do convênio: ")
            for n in convenios:
                if n["Nome"] == buscaConvenio:
                    print("Convênio encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCNPJ:", n["CNPJ"])
        if escolha == 2:
            buscaConvenio = input("Digite o CNPJ do convênio: ")
            for n in convenios:
                if n["CNPJ"] == buscaConvenio:
                    print("Convênio encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCNPJ:", n["CNPJ"])
        
    def alterarMedicos():
        escolha = int(input("Você quer buscar por nome ou CRM?\nDigite 1 para nome e 2 para CRM: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaMedico = input("Digite o nome do médico: ")
            for n in medicos:
                if n["Nome"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    alterar = int(input("Você deseja alterar os dados deste médico?\nDigite 1 para sim e 2 para não: "))
                    if alterar == 1:
                        n["Nome"] = input("Digite o nome do médico: ")
                        n["CPF"] = input("Digite o CPF do médico: ")
                        n["RG"] = input("Digite o RG do médico: ")
                        n["CRM"] = input("Digite o CRM do médico: ")
                        n["Telefone"] = input("Digite o telefone do médico: ")
                        n["Endereço"] = input("Digite o endereço do médico: ")
                        n["Sexo"] = input("Digite o sexo do médico: ")
                        n["Senha"] = input("Digite o senha do médico: ")
                        print("Médico alterado com sucesso.")
                    if alterar == 2:
                        print()
        if escolha == 2:
            buscaMedico = input("Digite o CRM do médico: ")
            for n in medicos:
                if n["CRM"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    alterar = int(input("Você deseja alterar os dados deste médico?\nDigite 1 para sim e 2 para não: "))
                    if alterar == 1:
                        n["Nome"] = input("Digite o nome do médico: ")
                        n["CPF"] = input("Digite o CPF do médico: ")
                        n["RG"] = input("Digite o RG do médico: ")
                        n["CRM"] = input("Digite o CRM do médico: ")
                        n["Telefone"] = input("Digite o telefone do médico: ")
                        n["Endereço"] = input("Digite o endereço do médico: ")
                        n["Sexo"] = input("Digite o sexo do médico: ")
                        n["Senha"] = input("Digite o senha do médico: ")
                        print("Médico alterado com sucesso.")
                    if alterar == 2:
                        print()
        
    def alterarPacientes():
        escolha = int(input("Você quer buscar por nome ou CPF?\nDigite 1 para nome e 2 para CPF: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaPaciente = input("Digite o nome do paciente: ")
            for n in pacientes:
                if n["Nome"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
                    alterar = int(input("Você deseja alterar os dados deste paciente?\nDigite 1 para sim e 2 para não: "))
                    if alterar == 1:
                        n["Nome"] = input("Digite o nome do paciente: ")
                        n["Endereço"] = input("Digite o endereço do paciente: ")
                        n["Telefone"] = input("Digite o telefone do paciente: ")
                        n["CPF"] = input("Digite o CPF do paciente: ")
                        n["RG"] = input("Digite o RG do paciente: ")
                        n["Sexo"] = input("Digite o sexo do paciente: ")
                        n["Convênio"] = input("Digite o convênio ao qual o paciente está associado: ")
                        print("Paciente alterado com sucesso.")
                    if alterar == 2:
                        print()

        if escolha == 2:
            buscaPaciente = input("Digite o CPF do pacientes: ")
            for n in pacientes:
                if n["CPF"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
                    alterar = int(input("Você deseja alterar os dados deste paciente?\nDigite 1 para sim e 2 para não: "))
                    if alterar == 1:
                        n["Nome"] = input("Digite o nome do paciente: ")
                        n["Endereço"] = input("Digite o endereço do paciente: ")
                        n["Telefone"] = input("Digite o telefone do paciente: ")
                        n["CPF"] = input("Digite o CPF do paciente: ")
                        n["RG"] = input("Digite o RG do paciente: ")
                        n["Sexo"] = input("Digite o sexo do paciente: ")
                        n["Convênio"] = input("Digite o convênio ao qual o paciente está associado: ")
                        print("Paciente alterado com sucesso.")
                    if alterar == 2:
                        print()
        
    def marcarCompromisso():
        escolha = int(input("Você quer buscar por nome ou CRM?\nDigite 1 para nome e 2 para CRM: "))
        while escolha < 1 or escolha > 2:
            escolha = int(input("Escolha inválida. Tente novamente."))
        if escolha == 1:
            buscaMedico = input("Digite o nome do médico: ")
            for n in medicos:
                if n["Nome"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    compromisso = int(input("Você deseja marcar um compromisso com este médico?\nDigite 1 para sim e 2 para não: "))
                    if compromisso == 1:
                        data = input("Digite a data do compromisso: ")
                        horaI = input("Digite a hora inicial do compromisso: ")
                        horaF = input("Digite a hora final do compromisso: ")
                        descricao = input("Descreva o compromisso: ")
                        compromissos.append({"Data": data, "Hora Inicial": horaI, "Hora Final": horaF, "Descrição": descricao})
                        print(f"Compromisso marcado com {n['Nome']} para o dia {data} às {horaI}.")
                    if compromisso == 2:
                        print()
        if escolha == 2:
            buscaMedico = input("Digite o CRM do médico: ")
            for n in medicos:
                if n["CRM"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    compromisso = int(input("Você deseja marcar um compromisso com este médico?\nDigite 1 para sim e 2 para não: "))
                    if compromisso == 1:
                        data = input("Digite a data do compromisso: ")
                        horaI = input("Digite a hora inicial do compromisso: ")
                        horaF = input("Digite a hora final do compromisso: ")
                        descricao = input("Descreva o compromisso: ")
                        compromissos.append({"Data": data, "Hora Inicial": horaI, "Hora Final": horaF, "Descrição": descricao})
                        print(f"Compromisso marcado com {n['Nome']} para o dia {data} às {horaI}.")
                    if compromisso == 2:
                        print()
        
    def marcarConsulta():
        escolhaM = int(input("Você quer buscar médicos por nome ou CRM?\nDigite 1 para nome e 2 para CRM: "))
        while escolhaM < 1 or escolhaM > 2:
            escolhaM = int(input("Escolha inválida. Tente novamente."))
        
        if escolhaM == 1:
            buscaMedico = input("Digite o nome do médico: ")
            for n in medicos:
                if n["Nome"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    consultaM = int(input("Você deseja escolher este médico?\nDigite 1 para sim ou 2 para não: "))
                    if consultaM == 1:
                        medicoC = n["Nome"]
                    if consultaM == 2:
                        print()
        
        if escolhaM == 2:
            buscaMedico = input("Digite o CRM do médico: ")
            for n in medicos:
                if n["CRM"] == buscaMedico:
                    print("Médico encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCRM:", n["CRM"])
                    consultaM = int(input("Você deseja escolher este médico?\nDigite 1 para sim ou 2 para não: "))
                    if consultaM == 1:
                        medicoC = n["Nome"]
                    if consultaM == 2:
                        print()
        
        escolhaP = int(input("Você quer buscar paciente por nome ou CPF?\nDigite 1 para nome e 2 para CPF: "))
        while escolhaP < 1 or escolhaP > 2:
            escolhaP = int(input("Escolha inválida. Tente novamente."))
        if escolhaP == 1:
            buscaPaciente = input("Digite o nome do paciente: ")
            for n in pacientes:
                if n["Nome"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
                    consultaP = int(input("Você deseja escolher este paciente?\nDigite 1 para sim ou 2 para não: "))
                    if consultaP == 1:
                        pacienteC = n["Nome"]
                    if consultaP == 2:
                        print()
        if escolhaP == 2:
            buscaPaciente = input("Digite o CPF do pacientes: ")
            for n in pacientes:
                if n["CPF"] == buscaPaciente:
                    print("Paciente encontrado: ")
                    print("Nome:", n["Nome"], "\nTelefone:", n["Telefone"], "\nCPF:", n["CPF"])
                    consultaP = int(input("Você deseja escolher este paciente?\nDigite 1 para sim ou 2 para não: "))
                    if consultaP == 1:
                        pacienteC = n["Nome"]
                    if consultaP == 2:
                        print()
        dataC = input("Digite o dia da consulta: ")
        horaC = input("Digite a hora completa da consulta: ")
        consultas.append({"Médico": medicoC, "Paciente": pacienteC, "Data": dataC, "Hora": horaC})
        print(f"Consulta marcada para às {horaC} do dia {dataC} com {pacienteC}, para o médico {medicoC}.")
        
    def emitirRelatorio():
        relatorios = int(input("Escolha o tipo de relatório:\nDigite 1 para médicos cadastrados;\n2 para pacientes cadasatrados;\n3 para convênios;\n4 para consultas: "))
        if relatorios == 1:
            print("Médicos cadastrados:")
            for n in medicos:
                print(n["Nome"])
        
        if relatorios == 2:
            print("Pacientes cadastrados:")
            for n in pacientes:
                print(n["Nome"])
        
        if relatorios == 3:
            print("Convênios cadastrados:")
            for n in convenios:
                print(n["Nome"])
        
        if relatorios == 4:
            print("Consultas marcadas:")
            for n in consultas:
                print(f"Dia: {n['Data']} \nHora: {n['Hora']}\n")

    if lang == 1:
        cadastrarMedicos()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 2:
        cadastrarPacientes()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 3:
        cadastrarConvenios()
        lang = input("Pressione ENTER para prosseguir")
    
    if lang == 4:
        buscarMedicos()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 5:
        buscarPacientes()
        lang = input("Pressione ENTER para prosseguir")
        
    if lang == 6:
        buscarConvenios()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 7:
        alterarMedicos()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 8:
        alterarPacientes()
        lang = input("Pressione ENTER para prosseguir")
    
    if lang == 9:
        marcarCompromisso()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 10:
        marcarConsulta()
        lang = input("Pressione ENTER para prosseguir")

    if lang == 11:
        emitirRelatorio()
        lang = input("Pressione ENTER para prosseguir")
    
    if lang == 12:
        condicao = False