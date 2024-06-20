Pokédex Django Project
Este é um projeto simples de uma Pokédex utilizando Django, integrado com a PokéAPI para buscar informações sobre Pokémon. A PokéAPI é uma API pública que fornece dados detalhados sobre Pokémon, incluindo sprites, tipos, habilidades e muito mais.

Funcionalidades
Visualização de detalhes de Pokémon, incluindo nome, número, sprite e tipos.
Navegação entre Pokémon usando os botões "Prev" e "Next".
Pesquisa de Pokémon pelo nome ou número.

Pré-requisitos
Python 3.x
Django 3.x
Pip (gerenciador de pacotes Python)

Clone o repositório:
git clone https://github.com/wellingtonflores/A3Pokedex

Navegue até a pasta raiz
cd pokedex

Crie e ative um ambiente virtual:
python -m venv venv

Para ativação:
source venv/bin/activate  # no Windows use `venv\Scripts\activate`

Instale as dependências do projeto:
pip install -r requirements.txt

Execute as migrações do Django:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

Acesse a aplicação em seu navegador:
Abra seu navegador e acesse http://localhost:8000/pokemon/1.

Uso
Ao acessar a página inicial, você verá detalhes do primeiro Pokémon na Pokédex.
Use os botões "Prev" e "Next" para navegar entre os Pokémon.
Utilize a barra de pesquisa para buscar um Pokémon específico por nome ou número.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades. Para mudanças significativas, por favor, abra um problema para discutirmos antes.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Você pode personalizar este README conforme as especificidades do seu projeto, incluindo mais detalhes sobre a estrutura de diretórios, como rodar testes, ou qualquer outra informação relevante para os colaboradores ou usuários do seu projeto. Certifique-se também de incluir um arquivo LICENSE caso ainda não tenha um, e escolha uma licença adequada para o seu projeto.
