# CaronaManager

**Descrição:** Sistema em Python para gerenciar caronas, com cadastro de pessoas, criação de viagens, controle de participantes e status de pagamentos. CLI pronta para uso e expandível para interface gráfica ou web.

---

## 🛠 Tecnologias

* Python 3.11
* SQLite
* (Futuro) Tkinter ou Flask
* Git (controle de versão)

---

## 📂 Estrutura do projeto

```
CaronaManager/
│
├─ core/               # Lógica do programa
│   ├─ db.py
│   ├─ pessoa.py
│   ├─ carona.py
│   ├─ pessoa_carona.py
│   └─ create.py
│
├─ ui/                 # Interface(Desenvolvida futuramente)
│   └─ arquivos
│
├─ requirements.txt    # Dependências do projeto(No momento nenhuma)
├─ README.md           # Este arquivo
├─ main.py
└─ .gitignore          # Arquivos ignorados pelo Git
```

---

## ⚡ Funcionalidades atuais

* Cadastrar pessoas
* Criar caronas
* Atribuir pessoas a caronas
* Consultar caronas e pendências
* Consultar status de pagamento
* Input SQL personalizado para consultas avançadas

---

## 🚀 Funcionalidades futuras

* Interface gráfica com Tkinter ou Flask
* Atualização e exclusão de registros
* Busca inteligente por caronas, pessoas e datas
* Exportação de dados para CSV
* Testes unitários completos
* Validação de entradas e datas
* Sistema de login de usuários (admin/usuário)

---

## 🎯 Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/CaronaManager.git
cd CaronaManager
```

2. Instale dependências (nenhuma no momento):

```bash
pip install -r requirements.txt
```

3. Execute o programa:

```bash
python main.py
```

---

## 🧩 Estrutura do banco de dados

* **pessoas**: id_pessoa, nome, contato, descricao(opcional)
* **carona**: id_carona, origem, destino, data_carona, descricao(opcional)
* **pessoa_carona**: id_rel, id_carona, id_pessoa, status(pago/pendente)

O banco é **SQLite** e é criado automaticamente ao rodar o programa.

---

## 📝 Licença

MIT License — sinta-se livre para usar, estudar e contribuir no projeto.


