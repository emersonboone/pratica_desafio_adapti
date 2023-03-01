def cadastraCandidatos(N, nomesCandidatos=[""], i=1):
    if N >= 1:
        nomesCandidatos += [input()]
        return cadastraCandidatos(N - 1, nomesCandidatos, i + 1)
    return nomesCandidatos


def apuraVotos(V, N, listaVotos=[]):
    if len(listaVotos) > 0:
        if V > 0:
            voto = int(input())
            if voto > N:
                listaVotos[N+1] += 1
            else:
                listaVotos[voto] += 1
            return apuraVotos(V - 1, N, listaVotos)
        return listaVotos
    # Cria uma lista com N (número de candidatos) + 2 posições, para armazenar os votos em cada índice
    return apuraVotos(V, N, listaVotos[:] + ([0] * (N + 2)))


def descobreVencedor(listaVotos, N, i=1, vencedor=0, indiceVencedor=0):
    if N >= i:
        if listaVotos[i] >= vencedor:
            vencedor = listaVotos[i]
            indiceVencedor = i
        return descobreVencedor(listaVotos, N, i + 1, vencedor, indiceVencedor)
    return indiceVencedor


def imprimeRelatorio(nomesCandidatos, listaVotos, vencedor, i=1):
    if len(nomesCandidatos) > i:
        print(f"{nomesCandidatos[i]}: {listaVotos[i]}")
        return imprimeRelatorio(nomesCandidatos, listaVotos, vencedor, i + 1)
    print(f"Brancos: {listaVotos[0]}")
    print(f"Nulos: {listaVotos[len(nomesCandidatos)]}")
    print(f"Vencedor(a): {nomesCandidatos[vencedor]}")


def main():
    n = int(input())
    nomesCandidatos = cadastraCandidatos(n)
    v = int(input())
    votosApurados = apuraVotos(v, n)
    vencedor = descobreVencedor(votosApurados[:], n)
    imprimeRelatorio(nomesCandidatos[:], votosApurados[:], vencedor)


main()
