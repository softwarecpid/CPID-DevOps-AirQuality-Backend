# Air Quality FastAPI - Sensor Data

This is an API dedicated to serve and receive data from the air quality sensors located all over the State.
The receved data is treated and returned in order to facilitate the interpretation by the user.

## Setting the Enviroment

### GeoJSON

`GeoJSON` is a specific kind of JSON file used for geographic data.

The application uses a `GeoJSON` file to know accurately where the sensor was (city and state) the moment the data was sent.
It bases in the latitude and longitude of the sensor GPS.

Depending where you are, the GeoJSON may change. Here we use the IBGE pattern.

```json
[
    ...
    {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                ...
            ],
        }
        "properties": {
            ...
            "NM_MUN": "<City Name>",
            "SIGLA_UF": "<UF>",
            ...
        }
    },
    ...
]
```

The `"NM_MUN"` and `"SIGLA_UF"` are required for the application to work properly.

### Getting the GeoJSON

1. Access the [IBGE website](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) and select your UF (State) municipality;

   ![A print of the IBGE website in the territorial mesh page with a red rectangle outlining the "municipality" option.](./media_readme/malha-municipal-ibge.png)

2. Once downloaded the zip folder, go to [mapshaper.org](https://mapshaper.org/) and drop, paste or select the zip folder you downloaded from IBGE.

   ![A print of the mapshaper website with a red rectangle outlining the "select" option.](./media_readme/select-files-mapshaper.png)

   ![A print where the user is selecting the zip folder downloaded from the IBGE website. A red rectangle is outlining the folder.](./media_readme/selected-zip.png)

3. Now, you need to export the file in the GeoJSON format.

   ![The mapshaper website with a red rectangle outlining the "Export" button in the right upper corner.](./media_readme/export-mapshaper.png)

   ![The image shows the mapshaper website with the options of exporting the file, a red rectangle is outlining the GeoJSON marked option and another red rectangle is outlining the new "Export" button.](./media_readme/geojson-mapshaper.png)

4. Finally, put the GeoJSON file in the root directory of the application and you are good to go.

### Installing the Dependencies

In the terminal, make sure you are in the root directory.

First, install the dependencies of the project with:

```bash
pip install -r requirements.txt
```

If you prefer, use an virtual environment to install the dependencies:

```bash
python3 -m venv .venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Running the Application

To run the application, use the commands:

```bash
# for development enviroments
fastapi dev path/to/main.py
```

```bash
# for production enviroments
fastapi run path/to/main.py
```

### Enviroment Variables

Enviroment variables (also known as "**env var**") are variables that lives **outside** the Python code, in the **operating system**, and could be read by your Python code (or by other programs as well).

For this application, create a `.env` file similar to the `.envExample`. Or just rename the `.envExample` to `.env`. This is where you are going to put all the environment variables of the application, such as the database name, host, username, port, password and every other environment variables you may like.

### FastAPI Tutorial

If you feel insecure or a bit lost, check the [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) for more information.

## Project Organization

The application is organized through three main directories: db, routers and tests. Also four Python files: main, models, schemas and utils.

The `models` file is mainly for working with the database through `SQLAlchemy` and use the `declarative_base` that comes from the directory `db.database`. Won't need to do anything there, unless the database is under changes, in this case see the [Alembic](#alembic) section.

The `schemas` file is for defining the model that will be outputed to the app.

The `/routes` directory is for all the endpoints of the project (to create more routes, take a look at the [Creating New Routes](#creating-new-routes) section).

The `/db` directory is used to connect to the database, using, at first, environment variables.

The `/tests` directory uses Pytest (a Python testing framework known for its simplicity, scalability and integration capabilities with other tools). For more information, check the [Tests](#tests) section.

## Alembic

Alembic is a lightweight database migration tool for usage with the [SQLAlchemy](https://www.sqlalchemy.org/) Database Toolkit for Python.

To begin, make sure Alembic is installed. The tutorial below assumes the `alembic` command line utility is present in the local path and when invoked, will have access to the same Python module environment as that of the target project.

### The Migration Enviroment

The migration environment is created just once, and is then maintained along with the application's source code itself.

The environment is created using:

```bash
alembic init #name-of-folder
```

and is customizable to suit the specific needs to the application.

The structure of the environment should look like this:

```
yourproject/
    alembic/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py
```

The `alembic` environment is already setup for this application. In case something went missing or you have any doubts, feel free to check the [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Creating New Routes

To create a new route, first you need to create a file in the `/routers` directory. There you have to initialize a function like this one:

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get("/")
async def read_users():
    return [{"username": "Cpid"}, {"username": "Elena"}]
```

Inside the `main.py` file just add this code:

```python
from fastapi import FastAPI

from .routers import your_file

app = FastAPI()

app.include_router(your_file.router)
```

## Tests

For unit testing the application, we use Pytest. We test each endpoint separately and check if the application is running all good.

The test environment is setup by the `conftest.py` file, where we setup a new database and the FastAPI's `TestClient` for making requests locally to our application.

<!-- # Legal Responsability

> Toda a documentação técnica, legal e histórica está disponível na Nota Metodológica Malha
> Municipal Digital e Áreas Territoriais 2022: [Informações Técnicas e Legais para a Utilização dos
> Dados Publicados](https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=2101998)
> Qualquer dúvida não sanada pela documentação deve ser encaminhada via canais oficiais do IBGE
> ou via [Lei de Acesso à Informação (LAI)](https://www.gov.br/acessoainformacao/pt-br)

## CONSIDERAÇÕES SOBRE AS LIMITAÇÕES DE USO E ISENÇÃO DE RESPONSABILIDADE

Embora a Malha Municipal Digital - MMD e as Áreas Territoriais do IBGE sejam utilizadas como
referência para diversas atividades e por diversos órgãos públicos, privados e a sociedade em geral, o
IBGE não é um órgão com atribuição legal para definição e demarcação de limites territoriais.

Os limites territoriais representados na MMD refletem o legado institucional das interpretações das
legislações efetuadas ao longo do projeto Arquivo Gráfico Municipal, da década de 1980, com incrementos
definidos pelos órgãos estaduais a partir da Constituição Federal de 1988. Assim, não devem ser
consideradas como demarcações ou caracterizações oficiais, ou seja, esta malha não pode ser utilizada,
em nenhuma hipótese, como sendo uma malha oficial da divisão político-administrativa.

De forma geral, os limites presentes na MMD devem ser entendidos como limites aproximados e,
consequentemente, as áreas territoriais, calculadas a partir destes, refletirão estas incertezas. A precisão da
linha dependerá de diversos fatores, tais como: clareza da legislação, tipo de feição, qualidade gráfica e
atualização da cartografia de referência utilizada para confecção da linha de limite. Destacam-se os
seguintes casos de limites territoriais, onde é necessária especial atenção em relação ao correto uso da
malha:

1. Limites baseados em hidrografia cujas leis utilizem os termos: “talvegue”, “álveo”, “sobe” ou
   “desce o rio”. Tais situações trazem problemas na materialização da linha, devido ao
   desconhecimento dos locais exatos onde passam o limite sobre a hidrografia.
2. Rios meandrantes ou regiões com alterações hidrográficas frequentes: A atualização
   cartográfica e a definição fundiária de propriedades podem ser comprometidas em função das
   alterações naturais e artificiais no curso do rio e também da escala de produção da malha
   municipal.
3. Divisor de água em regiões planas: A representação da linha divisória é compatível com a melhor
   escala do documento oficial disponível na região, podendo não ser a adequada para definição de
   detalhes no terreno.
4. Linhas secas cujos vértices não sejam definidos por marcos ou cujas coordenadas sejam
   desconhecidas dentro dos parâmetros atuais de precisão. É comum também leis que definem
   limites através de acidentes geográficos ou pontos notáveis de difícil identificação, não
   materializados por marcos e/ou não devidamente caracterizados por coordenadas.
5. Linhas astronômicas de qualquer tipo (ao menos que possuam a exigência solicitada no item 4)
6. Descritivos defasados ou genéricos: Limites cuja legislação ou memorial não contemple feições
   identificáveis em campo ou em produtos cartográficos oficiais e cuja precisão seja compatível com a
   demanda analisada.
7. Áreas urbanizadas: Determinados trechos de limites que atravessam áreas urbanizadas com
   grande adensamento de edificações podem sofrer ajustes em sua representação com objetivo de
   viabilizar as operações de pesquisa em campo.
8. A linha de costa representada na MMD tem finalidade operacional para as atividades de pesquisa
   inerentes ao IBGE; devido a isso, ela não possui expressão física, pois não foi alvo de estudos de
   linhas de marés, abrangência ou extensão das reentrâncias típicas do nosso litoral (baías,
   estuários, lagunas, deltas), ou mesmo, de estudos de erosão fluvial ou marinha. Assim, não deve
   ser utilizada para qualquer finalidade econômica ou ambiental.

Em decorrência direta e indireta dos itens acima, o IBGE não se responsabiliza por definir a posse de
qualquer ilha localizada em rios, lagoas, lagos, baías, estuários ou no oceano cuja subordinação políticoadministrativa não esteja explicitamente definida na lei que descreve o limite, e havendo divergência entre
descritivos serão obedecidos os critérios hierárquicos no nível federal e estadual.

O IBGE não se responsabiliza por definir a posse ou a subordinação político-administrativa de imóvel
urbano/rural, linhas de dutos, usinas, aeroportos, antenas, poços de petróleo/gás, áreas de mineração,
torres de parques eólicos, praças de pedágio, posto fiscal e qualquer outra edificação ou instalação
comercial ou industrial. Para todos os casos citados, qualquer discordância com relação à malha municipal
fornecida pelo IBGE deve ser direcionada:

- Ao Órgão Estadual responsável pela divisão político-administrativa no estado para os casos de
  limite municipal intraestadual. (vide Apêndice C para lista completa de órgãos estaduais
  reconhecidos pelo IBGE)

- Ao Ministério das Relações Exteriores – Comissões Brasileiras Demarcadoras de Limites, para
  os casos que envolverem a Fronteira Internacional do Brasil com Países vizinhos.
- Em casos de limites interestaduais, recomenda-se procurar ambos os órgãos estaduais
  envolvidos na questão.

Em função do cenário estabelecido, o IBGE reconhece o uso da MMD como referência da DPA para
fins diversos da produção de estatísticas, ressaltando as limitações informadas neste documento e em
outros documentos aqui indicados.

Os valores de Áreas Territoriais são publicados como valores oficiais no Diário Oficial da União, em
função das competências da Diretoria de Geociências do IBGE e da metodologia descrita, da melhor
representação cartográfica disponível dos elementos ou feições limítrofes, da projeção cartográfica utilizada
e seus respectivos parâmetros e Datum geodésico. Alertamos aos usuários que os valores calculados pelo
IBGE podem ser diferentes dos valores obtidos por outros órgãos, em virtude dos parâmetros, insumos
utilizados e softwares disponíveis.

Por fim, o IBGE não se responsabiliza pelo uso dos dados quando utilizados para finalidade diferente
relacionada a compilação de dados estatísticos, estando o IBGE isento de qualquer responsabilidade. -->
