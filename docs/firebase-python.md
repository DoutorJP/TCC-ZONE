# Documentação da integração Python-Firebase

## Preparação de dados
```
dados = {'campo1': valor1, 'campo2': valor2, 'campo3': valor3}
```
## Enviando os dados para o firebase
```
requisicao = requests.post(f'{link}/Tabela/.json', data=json.dumps(dados))
```
## Leitura 
A leitura extrai os dados do arquivo json e adiciona a um [dicionário](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries), assim, podemos melhor tratar e modelar os dados.
```
requisicao = requests.get(f'{link}/.json')
dic_requisicao = requisicao.json()
print(dic_requisicao['Tabela'])
```
No dicionário, podemos substituir "Tabela" por qualquer tabela que quisermos obter dados.

