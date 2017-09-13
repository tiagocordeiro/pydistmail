# pydistmail
Distribui os emails recebidos de forma sequencial entre membros de uma lista 
utilizando Python.

Por exemplo: Imagine que você tem uma equipe de vendas e gostaria que os 
contatos recebidos em um site, seja distribuido igualmente entre os vendedores.


Como usar no cPanel
-------------------

1. Crie uma conta de email que receberá os contatos ```Ex: vendas@domain.com```
2. Crie as contas de emails para onde serão distribuidos os contatos.
3. Faça upload do script no servidor. (atenção: NÃO utilize uma pasta pública)


```python
# lista com vendedores ou emails para distribuição
vendedores = [('Vendedor 01', 'vendas01@dominio.com.br'),
              ('Vendedor 02', 'vendas02@dominio.com.br')]
```

