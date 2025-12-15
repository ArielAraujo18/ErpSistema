from validate_docbr import CPF

cpf = CPF()

cpf_numero = "01014044504+"

if cpf.validate(cpf_numero):
    print("CPF válido")
else:
    print("CPF inválido")
