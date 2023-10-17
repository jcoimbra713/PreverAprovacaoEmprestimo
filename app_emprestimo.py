import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_emprestimo.pkl', 'rb') 
maquina_preditiva_emprestimo = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER APROVAÇÃO DE EMPRÉSTIMO</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA APROVAÇÃO DE EMPRÉSTIMO< - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    Sexo = st.selectbox('Sexo', ("Feminino", "Masculino","Bissexual","Não Declarado"))
    TipoEmpréstimo = st.selectbox('Tipo Empréstimo', ("Empréstimo Consignado", "Empréstimo Pessoal","Empréstimo Com Garantia"))
    CapacidadeCrédito = st.selectbox('Capacidade Crédito', ("Crédito Pessoal", "Financiamento"))
    NegócioOuComercial = st.selectbox('Tipo', ("Comercial", "Negócio"))
    ValorEmpréstimo = st.number_input("Valor Do Empréstimo") 
    CobrançasIniciais = st.number_input("Cobrança Iniciai")
    Renda = st.number_input("Renda")
    TipoCrédito = st.selectbox('Tipo Crédito', ("CIBIL", "CRIF","Equifax","Experian"))
    PontuaçãoCrédito = st.number_input("Pontuação Crédito")
    Região = st.selectbox('Região', ("North", "North East","central","south"))
    AltosJuros = st.selectbox('Juros alto', ("Sim", "Não"))
    IdadeAvançada = st.selectbox('Idade Avançada', ("Sim", "Não"))

    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(Sexo,TipoEmpréstimo,CapacidadeCrédito,NegócioOuComercial,ValorEmpréstimo,CobrançasIniciais,Renda,TipoCrédito,PontuaçãoCrédito,Região,AltosJuros,IdadeAvançada) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(Sexo,TipoEmpréstimo,CapacidadeCrédito,NegócioOuComercial,ValorEmpréstimo,CobrançasIniciais,Renda,TipoCrédito,PontuaçãoCrédito,Região,AltosJuros,IdadeAvançada):   
    # Pre-processando a entrada do Usuário    
    Sexo_dict = {
        "Feminino": 0,
        "Masculino": 1,
        "Bissexual": 2,
        "Não Declarado": 3,
    }
    Sexo = Sexo_dict[Sexo]

    TipoEmpréstimo_dict = {
        "Empréstimo Consignado": 0,
        "Empréstimo Pessoal": 1,
        "Empréstimo Com Garantia": 2,
    }
    TipoEmpréstimo = TipoEmpréstimo_dict[TipoEmpréstimo]


   
    CapacidadeCrédito_dict = {
        "Crédito Pessoal": 0,
        "Financiamento": 1,
    }
    CapacidadeCrédito = CapacidadeCrédito_dict[CapacidadeCrédito]



    NegócioOuComercial_dict = {
        "Comercial": 0,
        "Negócio": 1,
    }
    NegócioOuComercial = NegócioOuComercial_dict[NegócioOuComercial]


    TipoCrédito_dict = {
        "CIBIL": 0,
        "CRIF": 1,
        "Equifax": 2,
        "Experian": 3,
    }
    TipoCrédito = TipoCrédito_dict[TipoCrédito]


    Região_dict = {
        "North": 0,
        "North East": 1,
        "central": 2,
        "south": 3,
    }
    Região = Região_dict[Região]


    AltosJuros_dict = {
        "Sim": 0,
        "Não": 1,
    }
    AltosJuros = AltosJuros_dict[AltosJuros]

    IdadeAvançada_dict = {
        "Sim": 0,
        "Não": 1,
    }
    IdadeAvançada = IdadeAvançada_dict[IdadeAvançada]

    # Fazendo a Predição
    parametro = np.array([[Sexo,TipoEmpréstimo,CapacidadeCrédito,NegócioOuComercial,ValorEmpréstimo,CobrançasIniciais,Renda,TipoCrédito,PontuaçãoCrédito,Região,AltosJuros,IdadeAvançada]])
    fazendo_previsao = maquina_preditiva_emprestimo.predict(parametro)
    probabilidade = maquina_preditiva_emprestimo.predict_proba(parametro)

    if (fazendo_previsao == 0).any():
        pred = 'EMPRÉSTIMO APROVADO!'
    else:
        pred = 'EMPRÉSTIMO REPROVADO!'

    return pred, probabilidade

if __name__ == '__main__':
    main()




