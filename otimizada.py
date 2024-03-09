import random
import time

def sequencia_otimizada(vetor, chave):

    for i in range(len(vetor)):
        if vetor[i] == chave:
            return i
        elif vetor[i] > chave:
            return None
    return None

def main():
    # Tamanho da sequência
    n = 10

    # Número de buscas a serem realizadas sobre a sequência
      
    q = random.randint(10000, 99999)

    #Criação do vetor e do vetor de chaves
    vetor = []
    vetor_chaves= []

    #Colocando os números no vetor
    for i in range(n) :
        numero = random.randint(0, 10)
        vetor.append(numero)

    #Colocando os numeros no vetor de chaves
    for i in range(q):
      numero = random.randint(0, 10)
      vetor_chaves.append(numero)

    

    # Teste da função sequencia_otimizada
    
    resultados = []
    chaves_encontradas = 0
    start_time = time.time()
    #ordenando o vetor
    vetor.sort()
    for chave in vetor_chaves:
      result = sequencia_otimizada(vetor, chave)
      resultados.append(result)
      if result is not None:
        chaves_encontradas += 1
    execution_time = time.time() - start_time
  
    print(f"Vetor: {vetor}, Chaves encontradas: {chaves_encontradas}, Tempo de execução: {execution_time} segundos")


if __name__ == '__main__':
  main()