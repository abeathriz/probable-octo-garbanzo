df = pandas.read_csv('../bases_tratadas/dadostratadosfarfetch.csv', sep=';')

streamlit.dataframe(df)

streamlit.subheader('Análise de nulos')
aux = df.isnull().sum().reset_index()
aux.columns = ['preco', 'desconto']
streamlit.dataframe(aux)


streamlit.subheader('Análises univariadas')
streamlit.write('Medidas resumo')
streamlit.dataframe(df.describe())

#SELECIONAR COLUNA
lista_de_colunas = df.columns

colunas_numericas = df.select_dtypes(include='number').columns.tolist()


# VERIFICA COLUNAS NUMÉRICAS
if colunas_numericas:

    # SELECIONA
    coluna_escolhida = streamlit.selectbox('Escolha a coluna', colunas_numericas)

    media = round(df[coluna_escolhida].mean(),2)
    desvio = round(df[coluna_escolhida].std(),2)
    mediana = round(df[coluna_escolhida].quantile(0.5),2)
    maximo = round(df[coluna_escolhida].max(),2)
    minimo = round(df[coluna_escolhida].max(),2)

    streamlit.write(f"**Média**: {media}")
    streamlit.write(f"**Desvio padrão**: {desvio}")
    streamlit.write(f"**Mediana**: {mediana}")
    streamlit.write(f"**Máximo**: {maximo}")
else:
    streamlit.warning("Não contém coluna numérica.")

print('Média de valores descontados:', media)
print('Desvio padrão de valores descontados:', desvio)
print('Mediana dos valores descontados:', mediana)
print('Máximo dos valores descontados:' , maximo)
print('Menor valor dos descontados:', minimo)

streamlit.write(f'A coluna escolhida foi {coluna_escolhida}. A sua média é {media}. Seu desvio padrão indica que, quando há desvio, desvia em média {desvio}. E 50% dos dados vão até o valor {mediana}. E seu máximo é de {maximo}.')
streamlit.write(f'O produto com o maior valor, custa {minimo} reais')
streamlit.write('Histograma')
fig = plotly.express.histogram(df,x=[coluna_escolhida])
streamlit.plotly_chart(fig)
streamlit.write('Boxplot')
fig2 = plotly.express.box(df, x=[coluna_escolhida])
streamlit.plotly_chart(fig2)

streamlit.subheader('Análises multivariadas')
lista_de_escolhas = streamlit.multiselect('Escolha mais de uma coluna para avaliar', lista_de_colunas)
streamlit.markdown('Gráfico de dispersão')
if len(lista_de_escolhas)>2 or len(lista_de_escolhas)<2:
    streamlit.error('Escolha somente 2 colunas')
else:
    fig3 = plotly.express.scatter(df, x=lista_de_escolhas[0], y=lista_de_escolhas[1])
    streamlit.plotly_chart(fig3)
    streamlit.markdown('Gráfico de caixa')
    fig4 = plotly.express.box(df, x=lista_de_escolhas[0], y=lista_de_escolhas[1])
    streamlit.plotly_chart(fig4)
    fig5 = plotly.express.pie(df, lista_de_escolhas[0], lista_de_escolhas[1])
    streamlit.plotly_chart(fig5)
