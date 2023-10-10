def climb_stairs(n: int) -> int:
    if n ==1:
        return 1 # Se há apenas um degrau, há apenas uma maneira de subir.
    if n ==2:
        return 2  # Se há dois degraus, há duas maneiras de subir: (1,1) ou (2).
    
    # Cria um array para armazenar o número de maneiras de subir cada degrau.
    """Nesta linha, estamos inicializando uma lista chamada ways de 
    tamanho n + 1 (onde n é o número total de degraus) com todos os 
    elementos inicialmente setados para 0. A razão pela qual a lista 
    tem tamanho n + 1 é para acomodar degraus de 0 a n inclusos, 
    uma vez que listas em Python são indexadas a partir do 0."""
    ways = [0] * (n + 1)
    """Aqui estamos atribuindo o valor 1 ao elemento na posição 1 da lista ways. Isso representa que há exatamente uma maneira de subir se houver apenas um degrau (subindo 1 degrau).

    Portanto, se n for, pelo menos, 1, o array ways agora será algo como: [0, 1, 0, 0] (considerando o exemplo onde n = 3)."""
    ways[1] = 1

    """Similar à linha anterior, estamos atribuindo o valor 2 ao elemento na posição 2 da lista ways. Isso representa que há exatamente duas maneiras de subir se houver dois degraus: ou subimos um degrau de cada vez, ou subimos os dois degraus de uma vez.

    Assim, se n for, pelo menos, 2, o array ways agora será algo como: [0, 1, 2, 0] (considerando o exemplo onde n = 3)."""
    ways[2] = 2

    for i in range (3, n + 1):
        # O número de maneiras de subir ao degrau i é a soma do número de maneiras
        # de subir ao degrau i-1 e i-2, pois podemos subir 1 ou 2 degraus por vez.
        ways[i] = ways[i - 1] + ways[ i -2]

    return ways[n]

