from scipy.stats import (
    levene, 
    mannwhitneyu,
    ttest_ind
)

# Função para realizar o teste de Levene, que verifica a igualdade de variâncias
def analise_levene(dataframe, alfa=0.05, centro="mean"):
    print("Teste de Levene")
    
    # Calcula a estatística e o valor p do teste de Levene
    estatistica_levene, valor_p_levene = levene(*[dataframe[coluna] for coluna in dataframe.columns], center=centro, nan_policy="omit")

    print(f"{estatistica_levene=:.3f}")
    # Verifica se o valor p é maior que alfa para determinar se as variâncias são iguais
    if valor_p_levene > alfa:
        print(f"Variâncias iguais (valor p: {valor_p_levene:.3f})")
    else:
        print(f"Ao menos uma variância é diferente (valor p: {valor_p_levene:.3f})")

# Função para realizar o teste t de Student, que compara as médias de dois grupos
def analise_ttest_ind(
    dataframe,
    alfa=0.05,
    variancias_iguais=True,
    alternativa="two-sided"
):
    
    print("Teste t de Student")
    # Calcula a estatística e o valor p do teste t de Student
    estatistica_ttest, valor_p_ttest = ttest_ind(
        *[dataframe[coluna] for coluna in dataframe.columns], 
        equal_var=variancias_iguais, 
        alternative=alternativa,
        nan_policy="omit"
    )

    print(f"{estatistica_ttest=:.3f}")
    # Verifica se o valor p é maior que alfa para determinar se rejeita a hipótese nula
    if valor_p_ttest > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")

# Função para realizar o teste de Mann-Whitney, que compara distribuições de dois grupos independentes
def analise_mannwhitneyu(
    dataframe,
    alfa=0.05,
    alternativa="two-sided",
):

    print("Teste de Mann-Whitney")
    # Calcula a estatística e o valor p do teste de Mann-Whitney
    estatistica_mw, valor_p_mw = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativa,
    )

    print(f"{estatistica_mw=:.3f}")
    # Verifica se o valor p é maior que alfa para determinar se rejeita a hipótese nula
    if valor_p_mw > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_mw:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_mw:.3f})")

# Função para remover outliers dos dados com base no intervalo interquartil (IQR)
def remove_outliers(dados, largura_bigodes=1.5):
    q1 = dados.quantile(0.25)  # Primeiro quartil
    q3 = dados.quantile(0.75)  # Terceiro quartil
    iqr = q3 - q1  # Intervalo interquartil
    # Retorna os dados sem os outliers
    return dados[(dados >= q1 - largura_bigodes * iqr) & (dados <= q3 + largura_bigodes * iqr)]