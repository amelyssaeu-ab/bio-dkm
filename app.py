import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA (Precisa ser OBRIGATORIAMENTE o primeiro comando Streamlit)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Blog de Probabilidade em Biologia",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. BARRA LATERAL - SELETOR DA TAREFA PRINCIPAL
# -----------------------------------------------------------------------------
st.sidebar.title("📌 Menu de Tarefas")
tarefa_selecionada = st.sidebar.selectbox(
    "Escolha a Tarefa:",
    ["Tarefa 9 — Introdução à Probabilidade", "Tarefa 10 — Probabilidade Condicional"]
)

st.sidebar.divider()

# ==============================================================================
# TAREFA 9
# ==============================================================================
if tarefa_selecionada == "Tarefa 9 — Introdução à Probabilidade":
    
    # Navegação exclusiva da Tarefa 9
    st.sidebar.title("📌 Navegação (T9)")
    secao = st.sidebar.radio(
        "Ir para:",
        [
            "Início & Autores",
            "1. Introdução",
            "2. Histórico da Probabilidade",
            "3. Conceitos Fundamentais",
            "4. Teoria de Conjuntos",
            "5. Exemplo Integrado em Biologia",
            "6. Vídeos Recomendados",
            "7. Conclusão & Referências"
        ],
        key="nav_t9"
    )

    # --- SEÇÃO: INÍCIO & AUTORES (T9) ---
    if secao == "Início & Autores":
        st.title("🧬 Probabilidade Aplicada à Biologia")
        st.caption("Conceitos, conjuntos e aplicações da bioestátistica em um estudo de aves.")
        st.markdown("---")
        
        st.header("👥 Autoras")
        st.write("Conheça as integrantes do grupo responsáveis pela elaboração deste site.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image("imagens/autoradrica.png", width=250)
            st.markdown("**Nome:** Drielly Mathias")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:**
            - Elaboração da introdução do blog;
            - Construção do exemplo biológico, relacionando os conceitos de Probabilidade à Biologia;
            - Elaboração dos exemplos de eventos e das operações entre conjuntos;
            - Produção de diagramas de Venn e outros recursos visuais;
            - Pesquisa, seleção e formatação das referências bibliográficas utilizadas no blog.""")
            
        with col2:
            st.image("imagens/autoraka.png", width=250)
            st.markdown("**Nome:** Kawana Ganeo")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:** 
            - Pesquisa e síntese do histórico da Probabilidade; 
            - Elaboração da seção sobre experimento aleatório;
            - Pesquisa e organização dos conceitos fundamentais de Probabilidade apresentados no blog;
            - Organização e estruturação das diferentes seções e conteúdos do blog;
            - Revisão e adequação dos conteúdos teóricos, contribuindo para a organização e clareza das explicações.
            """)

        with col3:
            st.image("imagens/autoramel.png", width=250)
            st.markdown("**Nome:** Melyssa Ponce")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:** 
            - Construção e programação do site/blog;
            - Elaboração da conclusão do blog;
            - Seleção de vídeos relacionados ao tema;
            - Elaboração de comentários e contextualização dos vídeos selecionados;
            - Organização e inserção dos conteúdos e recursos multimídia no site, contribuindo para sua apresentação e funcionalidade.
            """)

        st.markdown("---")

        st.info("""
        **Observação:** Todas as integrantes participaram ativamente das discussões e contribuíram para a pesquisa, seleção e compreensão dos conteúdos abordados, especialmente em relação aos conceitos de Probabilidade. As atividades foram desenvolvidas de forma colaborativa, com troca de ideias, revisão conjunta e auxílio mútuo ao longo da elaboração do blog.
        """)

    # --- SEÇÃO: INTRODUÇÃO (T9) ---
    elif secao == "1. Introdução":
        st.header("1. Introdução: Probabilidade e Investigação Biológica")
        st.markdown("""
        A Biologia convive com a incerteza o tempo todo: imagine um pesquisador observando um comedouro de aves no meio do campus. Ele não tem como prever qual espécie vai aparecer no próximo instante, nem quanto tempo ela vai ficar ali, mas, com o tempo, começa a notar padrões. É exatamente esse tipo de incerteza, comum a quase toda observação biológica, que a Probabilidade nos ajuda a entender e medir. 
        """)
        st.markdown("""
        A probabilidade pode ser aplicada em diversos estudos como: Estudo de populações, genética, ecologia, epidemiologia, monitoramento de espécies e análise de dados experimentais. Dessa forma, compreender conceitos básicos como **experimento aleatório, espaço amostral e evento** é importante para interpretar situações biológicas de maneira quantitativa.
        """)
        st.markdown("""
        Neste blog, esses conceitos serão apresentados a partir de um contexto relacionado à observação de aves em comedouros. O exemplo foi inspirado no trabalho de Teixeira (2023), realizado no campus da UNESP de Rio Claro, no qual foram observadas aves nativas frugívoras em quatro pontos com comedouros. Durante o estudo, foram registradas 166 visitas pertencentes a 14 espécies de aves.
        """)

    # --- SEÇÃO: HISTÓRICO (T9) ---
    elif secao == "2. Histórico da Probabilidade":
        st.header("2. Breve Histórico da Probabilidade")
        st.markdown("""
        O desenvolvimento da probabilidade ocorreu gradualmente, partindo de diferentes problemas relacionados a jogos de azar e, posteriormente, a fenômenos naturais. 
        """)
        st.markdown("""
        Nosso blog se baseou no artigo de Silva e Grando (2024) que apresentam a história da Teoria da Probabilidade dividida em quatro períodos: **Pré-história da Probabilidade, surgimento do conceito, desenvolvimento da Probabilidade clássica e período moderno.**
        """)
        st.markdown("""
        Uma das primeiras vezes que a probabilidade apareceu na história foi através de objetos utilizados em jogos de azar, como os **astrágalos** (Eram ossos do tornozelo usados da mesma forma que um dado, para lançar e obter diferentes resultados). Essas práticas levaram à percepção de que determinados resultados poderiam ocorrer com frequências diferentes.
        """)

        st.image("imagens/imagemdente.jpeg", width=600)

        st.markdown("""
        Por conta disso, alguns estudiosos começaram a analisar matematicamente problemas relacionados aos jogos. Entre eles estavam **Luca Pacioli, Niccolò Tartaglia e Girolamo Cardano**. Posteriormente, **Galileu Galilei** também realizou estudos relacionados ao lançamento de dados. Seus trabalhos contribuíram para mostrar que diferentes resultados nem sempre deveriam ser considerados como igualmente prováveis, dependendo da situação analisada.
        """)
        st.markdown("""
        Um momento fundamental ocorreu no século XVII, com os estudos de **Blaise Pascal** e **Pierre de Fermat**. A partir da correspondência desses dois matemáticos sobre problemas relacionados aos jogos de azar, foram desenvolvidas ideias que contribuíram para a formalização matemática da **Probabilidade** e para o estudo do valor esperado.
        """)
        st.markdown("""
        Em 1657, **Christiaan Huygens** publicou uma obra dedicada à Probabilidade, contribuindo para a sistematização das regras desenvolvidas naquele período e para o conceito de esperança matemática. Posteriormente, **Jacob Bernoulli** desenvolveu resultados relacionados à **Lei dos Grandes Números.** 
        """)
        st.markdown("""
        Com o passar do tempo, a Probabilidade deixou de estar associada aos jogos de azar e passou a ser utilizada em diferentes áreas da ciência. No período moderno, a Teoria da Probabilidade passou por uma formalização matemática rigorosa. Essa evolução culminou em uma abordagem axiomática associada, entre outros acontecimentos, aos trabalhos de **Andrey Kolmogorov**. Assim, a Probabilidade tornou-se uma importante ferramenta para a Matemática, a Estatística e diversas áreas científicas.
        """)

    # --- SEÇÃO: CONCEITOS FUNDAMENTAIS (T9) ---
    elif secao == "3. Conceitos Fundamentais":
        st.header("3. Conceitos Fundamentais")
        
        st.subheader("3.1 Experimento Aleatório")
        st.markdown("""
        Um experimento aleatório é uma situação ou procedimento que pode ser realizado sob determinadas condições, mas cujo resultado exato não pode ser conhecido com certeza antes de sua realização. 
        """)
        st.markdown("""
        Isso não significa que não saibamos o que pode acontecer. Pelo contrário: em um experimento aleatório, geralmente conseguimos identificar e listar os resultados possíveis, mas não podemos determinar antecipadamente qual deles será obtido em uma realização específica.
        """)
        st.markdown("""
        Por exemplo, ao lançar uma moeda, sabemos que os resultados possíveis são cara ou coroa. Entretanto, antes de realizar o lançamento, não podemos afirmar com certeza qual dos dois resultados será obtido.
        """)
        st.markdown("""
        No estudo de Teixeira (2023), podemos considerar a escolha aleatória de uma visita de ave registrada durante um estudo. Sabemos quais espécies foram observadas, mas, antes de selecionar uma visita ao acaso, não sabemos qual espécie estará associada à observação escolhida.
        """)
        st.markdown("""
        É importante perceber que o experimento aleatório não significa que não existam informações sobre o fenômeno. Pelo contrário, conhecemos as possibilidades de resultado, mas não sabemos qual delas será obtida antes da realização do experimento.
        """)
        
        st.subheader("3.2 Espaço Amostral")
        st.markdown("""
        O **espaço amostral** é o **conjunto formado por todos os resultados possíveis de um experimento aleatório.** Ele é geralmente representado pela letra **S** ou pela letra grega **Ω (ômega).** 
        """)
        st.markdown("""
        Cada elemento pertencente ao espaço amostral representa um possível resultado do experimento.
        """)
        st.markdown("""
        Por exemplo, no lançamento de um dado comum, os resultados possíveis são 1, 2, 3, 4, 5 e 6. Assim, o espaço amostral pode ser representado por:
        """)
        st.latex(r"S = \{1, 2, 3, 4, 5, 6\}")
        st.markdown("""
        É importante observar que o espaço amostral depende de como o experimento foi definido. O mesmo fenômeno pode apresentar espaços amostrais diferentes dependendo da pergunta que se deseja investigar.
        """)
        st.markdown("""
        Por exemplo, se o interesse for saber qual número apareceu no dado, o espaço amostral será:
        """)
        st.latex(r"S = \{1, 2, 3, 4, 5, 6\}")
        st.markdown("""
        Por outro lado, se quisermos saber apenas se o resultado foi par ou ímpar, podemos definir:
        """)
        st.latex(r"S = \{par, ímpar\}")
        st.markdown("""
        Portanto, antes de analisar a probabilidade de um acontecimento, é importante definir claramente qual é o experimento e quais são os resultados que serão considerados possíveis.
        """)
        st.markdown("""
        Considerando o exemplo das aves, Se o objetivo for selecionar aleatoriamente uma visita registrada e identificar **qual espécie de ave foi observada**, os resultados possíveis serão as 14 espécies registradas no estudo.
        """)
        st.markdown("""
        Nesse caso, o espaço amostral pode ser representado por:
        """)
        st.latex(r"S = \{Thraupis\ sayaca, Thraupis\ palmarum, Tangara\ cayana, Pitangus\ sulphuratus, Mimus\ saturninus, Turdus\ leucomelas, Euphonia\ chlorotica, Turdus\ amaurochalinus, Passer\ domesticus, Zonotrichia\ capensis, Icterus\ pyrrhopterus, Colaptes\ melanochloros, Molothrus\ bonariensis, Saltator\ similis\}")
        st.markdown("""
        Embora o espaço amostral seja formado pelas 14 espécies possíveis, essas espécies não aparecem necessariamente com a mesma frequência nos dados. Por exemplo, _Thraupis sayaca_ apresentou 56 visitas, enquanto _Thraupis palmarum_ apresentou 29 e _Tangara cayana_, 20. 
        """)
        st.markdown("""
        Essa diferença é importante porque o espaço amostral apresenta as possibilidades de resultado, enquanto a frequência com que cada resultado aparece nos dados pode ser utilizada para compreender sua ocorrência dentro do conjunto observado.
        """)
        
        st.subheader("3.3 Eventos")
        st.markdown("""
        Um **evento** é um **subconjunto do espaço amostral**, ou seja, um conjunto formado por um ou mais resultados possíveis de um experimento. Enquanto o espaço amostral reúne **todos os resultados possíveis**, o evento representa apenas os resultados que possuem alguma característica de interesse para a investigação.
        """)
        st.markdown("""
        Considerando novamente o lançamento de um dado:
        """)
        st.latex(r"S = \{1,2,3,4,5,6\}")
        st.markdown("""
        Podemos definir o evento *A* como:
        """)
        st.latex(r"A = \{\text{obter um número par}\}")
        st.markdown("""
        Nesse caso:
        """)
        st.latex(r"A = \{2,4,6\}")
        st.markdown("""
        Observe que todos os elementos de **A** também pertencem ao espaço amostral **S**. Por isso, dizemos que **A é um subconjunto de S**, o que pode ser representado por:
        """)
        st.latex(r"A \subseteq S")
        
        st.subheader("3.4 Probabilidade de um evento")
        st.markdown("""
        Depois de definir o experimento aleatório, o espaço amostral e os eventos, podemos determinar quão provável é a ocorrência de determinado evento. A probabilidade é uma medida que indica a possibilidade de um evento acontecer e pode assumir valores entre **0 e 1**, ou entre **0% e 100%**.

        Em situações nas quais os resultados possíveis são igualmente prováveis, a probabilidade de um evento **A** pode ser calculada pela relação:
        """)
        st.latex(r"P(A) = \frac{n(A)}{n(S)}")
        st.markdown("""
        em que:
        * **P(A)** é a probabilidade de ocorrência do evento A;
        * **n(A)** é o número de resultados favoráveis ao evento A;
        * **n(S)** é o número total de resultados possíveis do espaço amostral.
        """)
        st.markdown("Por exemplo, no lançamento de um dado comum, o espaço amostral é:")
        st.latex(r"S = \{1, 2, 3, 4, 5, 6\}")

        st.markdown("Se o evento **A** corresponde à obtenção de um número par:")
        st.latex(r"A = \{2, 4, 6\}")

        st.markdown("Existem 3 resultados favoráveis entre 6 resultados possíveis. Portanto:")
        st.latex(r"P(A) = \frac{3}{6} = \frac{1}{2} = 0{,}5")

        st.markdown("Assim, a probabilidade de obter um número par é de **0,5**, ou **50%**.")

        st.divider()

        st.markdown("### Propriedades Importantes")
        st.markdown("A probabilidade possui algumas propriedades fundamentais. Como representa uma medida de possibilidade, seu valor sempre está entre 0 e 1:")
        st.latex(r"0 \leq P(A) \leq 1")

        st.markdown("A probabilidade do espaço amostral é igual a **1**, pois ele reúne todos os resultados possíveis:")
        st.latex(r"P(S) = 1")

        st.markdown("Já a probabilidade de um evento impossível é igual a **0**:")
        st.latex(r"P(\varnothing) = 0")

        st.markdown("Também podemos calcular a probabilidade do complemento de um evento. Como o complemento (\(A^c\)) representa todos os resultados em que **A** não ocorre:")
        st.latex(r"P(A^c) = 1 - P(A)")

        st.divider()

        st.markdown("### 🌿 Aplicando ao estudo das aves")
        st.markdown("""
        Podemos aplicar essa ideia ao estudo de **Teixeira (2023)**. Imagine que uma das 166 visitas registradas seja selecionada aleatoriamente. Nesse caso, podemos calcular a probabilidade de a visita selecionada ter sido realizada por *Thraupis sayaca*.

        O evento **A** corresponde às visitas realizadas por *Thraupis sayaca*. Como foram registradas 56 visitas dessa espécie, temos:
        """)
        st.latex(r"P(A) = \frac{56}{166} \approx 0{,}337")

        st.markdown("""
        Portanto, a probabilidade de selecionar aleatoriamente uma das 166 visitas e ela ter sido realizada por *Thraupis sayaca* é de aproximadamente **0,337**, ou **33,7%**.

        Esse exemplo mostra como a Probabilidade pode ser utilizada para transformar os registros de um estudo biológico em uma medida quantitativa da ocorrência de determinado resultado.
        """)

    # --- SEÇÃO: TEORIA DE CONJUNTOS (T9) ---
    elif secao == "4. Teoria de Conjuntos":
        st.header("4. Teoria de Conjuntos Aplicada à Probabilidade")
        st.markdown("""
        A **Teoria de Conjuntos** é uma área da Matemática que estuda conjuntos, ou seja, agrupamentos de elementos que possuem alguma característica em comum. Na Probabilidade, essa teoria é importante porque permite **representar e organizar os resultados de um experimento aleatório**, facilitando a análise dos eventos.
        """)
        st.markdown("""
        Como vimos anteriormente, o **espaço amostral (S)** reúne todos os resultados possíveis de um experimento, enquanto um **evento** é um subconjunto desse espaço amostral. Dessa forma, podemos utilizar conceitos e operações da Teoria de Conjuntos para representar diferentes acontecimentos e investigar a relação entre eles.
        """)
        st.image("imagens/imagem 4.png", width=500, caption="Fonte: elaboração dos autores.")

        st.divider()
        st.markdown("##### Conjunto")
        st.markdown("""
        Um conjunto é uma coleção de elementos que possuem alguma característica ou condição em comum. Na Probabilidade, um conjunto pode representar um **evento**.
        """)
        st.latex(r"S = \{1,2,3,4,5,6\}")
        st.latex(r"A = \{2,4,6\}")
        st.markdown("Dizemos que **A é um subconjunto de S**:")
        st.latex(r"A \subseteq S")

        st.markdown("##### Elemento")
        st.markdown("""
        Um elemento é cada objeto ou resultado que pertence a um conjunto. O símbolo ∈ significa “pertence a”. Por exemplo:
        """)
        st.latex(r"4 \in A")
        st.latex(r"\text{Já: } 3 \notin A")
        st.image("imagens/imagem 5.png", width=700, caption="Fonte: Elaborado pelo autor.")

        st.markdown("##### Subconjunto")
        st.markdown("""
        Um conjunto **A** é considerado subconjunto de **S** quando todos os elementos de A também pertencem a S. Essa relação é representada por: **A ⊆ S**
        """)
        st.divider()

        st.markdown("##### Operações entre conjuntos:")
        st.markdown("##### União (A ∪ B):")
        st.markdown("A **união** de dois conjuntos reúne todos os elementos que pertencem a **A, a B ou a ambos.**")
        st.markdown("##### Interseção (A ∩ B):")
        st.markdown("A **interseção** reúne apenas os elementos que pertencem **simultaneamente aos dois conjuntos.**")
        st.markdown("##### Complemento (Aᶜ)")
        st.markdown("O **complemento de um evento A** é formado por todos os resultados do espaço amostral que **não pertencem a A.**")
        st.latex(r"A^c = S - A")

    # --- SEÇÃO: EXEMPLO INTEGRADO (T9) ---
    elif secao == "5. Exemplo Integrado em Biologia":
        st.header("5. Exemplo Integrado em Biologia")
        st.markdown("""
        ### Aplicando os conceitos de probabilidade ao estudo das aves
        Vamos consolidar os conceitos apresentados utilizando como referência o estudo _“Frequência de visitação e tempo de permanência de aves nativas frugívoras em comedouros”_, de Teixeira (2023), realizado no campus da UNESP de Rio Claro.
        """)
        st.markdown("Durante o estudo, foram registradas **166 visitas realizadas por 14 espécies de aves nativas frugívoras**, em quatro pontos do campus. _Thraupis sayaca_ foi a espécie que apresentou a maior frequência de visitas, enquanto _Mimus saturninus_ apresentou as visitas mais longas. O tempo de permanência das aves nos comedouros variou de 1 a 620 segundos.")
        st.markdown("Para relacionar esses dados aos conceitos básicos de probabilidade, podemos imaginar que uma das 166 visitas registradas seja escolhida aleatoriamente.")

        st.divider()
        st.markdown("**Experimento aleatório:** selecionar aleatoriamente uma das visitas registradas no estudo e observar qual **espécie de ave** realizou a visita e **quanto tempo** ela permaneceu no comedouro.")
        st.markdown("Espaço amostral (S): Nesse caso, o **espaço amostral** é formado pelas **166 visitas registradas no estudo**, considerando cada visita como um possível resultado do experimento.")
        st.latex(r"S = \{\text{todas as 166 visitas registradas}\}")
        
        st.markdown("**Evento A:** “a visita selecionada foi realizada por uma ave da espécie _Thraupis sayaca_”. Como a espécie apresentou 56 visitas, o evento A possui 56 resultados.")
        st.markdown("**Evento B:** “o tempo de permanência da visita selecionada foi superior a 60 segundos”.")
        
        st.markdown("""
        - **A ∪ B:** a visita selecionada foi realizada por _Thraupis sayaca_ **ou** teve duração superior a 60 segundos.
        """)
        st.image("imagens/imagem1.png", width=700, caption="Fonte: elaboração dos autores.")

        st.markdown("""
        - **A ∩ B:** a visita selecionada foi realizada por _Thraupis sayaca_ **e** teve duração superior a 60 segundos.
        """)
        st.image("imagens/imagem 2.png", width=700, caption="Fonte: elaboração dos autores.")

        st.markdown("""
        - **Aᶜ:** a visita selecionada **não** foi realizada por _Thraupis sayaca_.
        """)
        st.image("imagens/imagem 3.png", width=700, caption="Fonte: elaboração dos autores.")

        st.markdown("""
        - **∅ (evento impossível):** O evento é impossível porque o pinguim-de-Magalhães não está entre as espécies registradas. Corresponde ao **conjunto vazio (∅)**.
        """)

    # --- SEÇÃO: VÍDEOS RECOMENDADOS (T9) ---
    elif secao == "6. Vídeos Recomendados":
        st.header("6. Vídeos Recomendados e Comentados")
        st.write("Seleção de materiais complementares para aprofundamento nos conceitos de Probabilidade.")
        
        st.subheader("1. Análises de Eventos Aleatórios")
        st.video("https://www.youtube.com/watch?v=ytw63q7SgZk")
        st.markdown("**Canal:** Khan Academy Brasil")
        st.markdown("**Conceito explicado:** Eventos aleatórios")
        st.markdown("**Comentário dos autores:** Este vídeo foi selecionado por apresentar de forma clara a intuição básica por trás dos eventos aleatórios...")
        st.markdown("---")

        st.subheader("2. Probabilidade na Genética")
        st.video("https://www.youtube.com/watch?v=asDzvBZ-Q2o")
        st.markdown("**Canal:** Curso Enem Gratuito")
        st.markdown("**Conceito explicado:** Probabilidade e Eventos no geral")
        st.markdown("**Comentário dos autores:** Este vídeo apresenta conceitos da probabilidade de maneira aplicada, dentro de estudos de expressão gênica...")
        st.markdown("---")

        st.subheader("3. História da Matematica e Probabilidade")
        st.video("https://www.youtube.com/watch?v=h_bXJcQgkPM")
        st.markdown("**Canal:** Frequência Cortes")
        st.markdown("**Conceito explicado:** Histórico da probabilidade e Combinações")
        st.markdown("**Comentário dos autores:** O vídeo acima foi selecionado como forma de reforçar o conteúdo apresentado na seção 2...")
        st.markdown("---")

        st.subheader("4. Operações com conjuntos")
        st.video("https://www.youtube.com/watch?v=zMtWXhNl324")
        st.markdown("**Canal:** Gis com Giz")
        st.markdown("**Conceito explicado:** Conjuntos")
        st.markdown("**Comentário dos autores:** Como forma de reforçar os conceitos de operações entre conjuntos...")
        st.markdown("---")

        st.subheader("5. Operações com conjuntos - união e intersecção")
        st.video("https://www.youtube.com/watch?v=k5XdHE6jr8I")
        st.markdown("**Canal:** Gis com Giz")
        st.markdown("**Conceito explicado:** Conjuntos, união e intersecção")
        st.markdown("**Comentário dos autores:** A professora Gis mostra o passo-a-passo de como realizar operações com conjuntos...")

    # --- SEÇÃO: CONCLUSÃO & REFERÊNCIAS (T9) ---
    elif secao == "7. Conclusão & Referências":
        st.header("7. Conclusão")
        st.markdown("""
        A modelagem probabilística e a teoria dos conjuntos não são apenas abstrações matemáticas; elas se consolidam como **ferramentas analíticas indispensáveis para as ciências biológicas**. 
        """)
        st.divider()

        st.markdown("### 📌 Principais Aprendizados")
        st.markdown("""
        * **Estruturação do Espaço Amostral:** Definir corretamente o universo de resultados possíveis é o primeiro passo para qualquer análise quantitativa.
        * **Lógica dos Conjuntos na Biologia:** Operações nos permitem categorizar visitas de espécies específicas.
        * **Métrica da Incerteza:** A probabilidade transforma dados amostrais brutos em taxas mensuráveis.
        """)
        st.divider()

        st.markdown("### 🌿 Reflexão Final")
        st.markdown("""
        Compreender a probabilidade permite ao biólogo e ao pesquisador transitar do mero registro observacional para a quantificação rigorosa dos padrões naturais.
        """)
        
        st.header("8. Referências Bibliográficas")
        st.markdown("""
        - BUSSAB, Wilton de Oliveira; MORETTIN, Pedro Alberto. **Estatística Básica**. 9. ed. São Paulo: Saraiva, 2017.
        - MAGALHÃES, Marcos Nascimento; LIMA, Antonio Carlos Pedroso de. **Noções de Probabilidade e Estatística**. 7. ed. São Paulo: EdUSP, 2015.
        - ROSS, Sheldon. A first course in probability. 10. ed. New York: Pearson, 2019.
        - SILVA, Gerlan da; GRANDO, Regina Célia. A brief historical overview of Probability Theory and the connections with its teaching. Revista Internacional de Pesquisa em Educação Matemática, Brasília, v. 14, n. 3, p. 1–15, 2024.
        - TEIXEIRA, Fábio Fernandes. Frequência de visitação e tempo de permanência de aves nativas frugívoras em comedouros. 2023. Trabalho de Conclusão de Curso (Ciências Biológicas) – Unesp, Rio Claro, 2023.
        """)


# ==============================================================================
# TAREFA 10 — PROBABILIDADE CONDICIONAL
# ==============================================================================
elif tarefa_selecionada == "Tarefa 10 — Probabilidade Condicional":
    
    # Navegação exclusiva da Tarefa 10
    st.sidebar.title("📌 Navegação (T10)")
    secao_t10 = st.sidebar.radio(
        "Ir para:",
        [
            "Início & Autores",
            "1. Introdução",
            "2. Probabilidade Condicional",
            "3. Exemplo em Situação Biológica",
            "4. Independência e Dependência",
            "5. Regra do Produto",
            "6. Relação entre os Conceitos",
            "7. Exemplo Integrado Aplicado",
            "8. Vídeos Recomendados",
            "9. Conclusão & Referências"
        ],
        key="nav_t10"
    )

    # --- T10: INÍCIO & AUTORES ---
    if secao_t10 == "Início & Autores":
        st.image("imagens/capa2.png", width=1200)
        st.markdown("---")
        
        st.header("👥 Autoras")
        st.write("Conheça as integrantes do grupo responsáveis pela elaboração deste site.")
        
        col1, col2, col3 = st.columns(3)
            
        with col1:
            st.image("imagens/autoradrica.png", width=250)
            st.markdown("**Nome:** Drielly Mathias")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:**
            - Elaboração da introdução do blog;
            - Construção do exemplo biológico, relacionando os conceitos de Probabilidade;
            - Elaboração dos exemplos de eventos e das relações entre os conceitos;
            - Produção dos recursos visuais;
            - Seleção dos vídeos relacionado ao tema;
            - Pesquisa, seleção e formatação das referências bibliográficas utilizadas no blog.""")

        with col2:
            st.image("imagens/autoraka.png", width=250)
            st.markdown("**Nome:** Kawana Ganeo")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:** 
            - Pesquisa e síntese do histórico da Probabilidade; 
            - Elaboração da seção sobre Independência e Dependência
            - Pesquisa e organização dos conceitos fundamentais de Regra do Produto apresentados no blog;
            - Organização e estruturação das diferentes seções e conteúdos do blog;
            - Revisão e adequação dos conteúdos teóricos, contribuindo para a organização e clareza das explicações.
            """)
        
        with col3:
            st.image("imagens/autoramel.png", width=250)
            st.markdown("**Nome:** Melyssa Ponce")
            st.markdown("**Curso:** Ciências Biológicas")
            st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
            st.markdown("""
            **Contribuições:** 
            - Construção e programação do site/blog;
            - Elaboração da conclusão do blog;
            - Seleção de vídeos relacionados ao tema;
            - Elaboração de comentários e contextualização dos vídeos selecionados;
            - Organização e inserção dos conteúdos e recursos multimídia no site, contribuindo para sua apresentação e funcionalidade.
            """)
        
        st.markdown("---")
        
        st.info("""
        **Observação:** Todas as integrantes participaram ativamente das discussões e contribuíram para a pesquisa, seleção e compreensão dos conteúdos abordados, especialmente em relação aos conceitos de Probabilidade. As atividades foram desenvolvidas de forma colaborativa, com troca de ideias, revisão conjunta e auxílio mútuo ao longo da elaboração do blog.
        """)

    # --- T10: 1. INTRODUÇÃO ---
    elif secao_t10 == "1. Introdução":
        st.header("1. Por que a probabilidade condicional é relevante em Biologia?")
        
        st.markdown("""
        Na natureza, os fenômenos biológicos raramente acontecem de maneira totalmente previsível. A presença de um organismo, a ocorrência de uma interação ecológica ou a reprodução de uma espécie podem depender de diferentes condições ambientais e biológicas. Por isso, a probabilidade é uma ferramenta importante para descrever e interpretar situações em que existe variabilidade e incerteza.

        Um exemplo interessante pode ser encontrado nas interações entre beija-flores e plantas. Os beija-flores utilizam o néctar das flores como importante fonte de energia e, ao visitar as flores, podem atuar como polinizadores, estabelecendo relações ecológicas fundamentais para a reprodução de diversas espécies vegetais. A disponibilidade desses recursos, entretanto, pode variar no espaço e no tempo, influenciando as interações entre plantas e beija-flores.

        Estudos realizados no Brasil mostram essa relação. Em uma área de Cerrado na Bahia, **Lima-Passos et al. (2026)** registraram 2.233 visitas de quatro espécies de beija-flores a 15 espécies de plantas durante 13 meses. Os autores observaram que a frequência de visitas dos beija-flores esteve positivamente relacionada à disponibilidade de flores, indicando que a quantidade de recursos florais pode estar associada à frequência dessas interações.

        Outro estudo, realizado na Restinga de Jurubatiba, no Rio de Janeiro, também evidenciou a importância da disponibilidade de recursos florais. Os pesquisadores registraram diferentes espécies de plantas visitadas por beija-flores e observaram variações na disponibilidade de flores e néctar ao longo do período estudado. Segundo os autores, essa variação nos recursos pode influenciar os deslocamentos dos beija-flores, sua área de forrageamento e, consequentemente, a polinização das plantas.
        """)

        st.divider()
        st.subheader("Como introduzimos a probabilidade nesses estudos?")
        st.markdown("""
        Imagine que, durante um estudo de campo, sejam registrados diversos momentos de observação de uma determinada área. Em cada momento, podemos verificar duas informações: se havia alta disponibilidade de flores e se ocorreu uma visita de beija-flor. A partir desses dados, podemos perguntar:

        > *"Qual é a probabilidade de ocorrer uma visita de beija-flor quando sabemos que há alta disponibilidade de flores?"*

        Essa pergunta é diferente de simplesmente perguntar qual é a probabilidade de um beija-flor visitar a área. Já que agora, temos uma informação adicional, a disponibilidade de flores, que pode alterar a probabilidade do evento que queremos investigar.

        É nesse tipo de situação que a **probabilidade condicional** se torna especialmente útil. Ela permite calcular a probabilidade de um evento ocorrer considerando que sabemos que outro evento já aconteceu. 

        No contexto deste blog, utilizaremos as interações entre beija-flores e flores para compreender como a informação sobre uma condição ecológica pode modificar a interpretação de uma probabilidade. Ao longo do conteúdo, também veremos como determinar se dois eventos podem ser considerados independentes ou dependentes e como utilizar a regra do produto para calcular a probabilidade de ocorrência simultânea de eventos biológicos.
        """)

    # --- T10: 2. PROBABILIDADE CONDICIONAL ---
    elif secao_t10 == "2. Probabilidade Condicional":
        st.header("2. Probabilidade Condicional")
        st.markdown("""
        A probabilidade condicional representa a probabilidade de um evento ocorrer considerando que sabemos que outro evento já aconteceu. Dessa forma, uma informação previamente conhecida passa a fazer parte da análise e modifica o conjunto de possibilidades que está sendo considerado.

        Segundo **Figueiredo (2002)**, para dois eventos quaisquer \(A\) e \(B\), sendo \(P(B) > 0\), a probabilidade de \(A\) ocorrer sabendo que \(B\) ocorreu é representada por:
        """)
        
        st.latex(r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}")

        st.markdown("""
        O termo \(P(A \mid B)\) representa a probabilidade de ocorrer o evento \(A\) sabendo que o evento \(B\) ocorreu. Já \(P(A \cap B)\) representa a probabilidade de \(A\) e \(B\) ocorrerem simultaneamente, enquanto \(P(B)\) representa a probabilidade de ocorrência do evento que está sendo considerado como condição.

        Como exemplo dentro do contexto das interações entre beija-flores e plantas, podemos considerar:
        * **Evento A:** ocorreu uma visita de beija-flor;
        * **Evento B:** havia alta disponibilidade de flores;
        * **Evento \(A \cap B\):** ocorreu uma visita de beija-flor e havia alta disponibilidade de flores.

        Nesse caso, \(P(A \mid B)\) representa a probabilidade de ocorrer uma visita de beija-flor sabendo que havia alta disponibilidade de flores. 

        Enquanto \(P(A)\) representa a probabilidade de ocorrer uma visita de beija-flor considerando todas as situações observadas, \(P(A \mid B)\) considera **somente** as situações em que havia alta disponibilidade de flores.

        A ordem dos eventos também faz diferença. Por exemplo:
        * \(P(A \mid B)\) significa a probabilidade da visita de um beija-flor sabendo que havia alta disponibilidade de flores.
        * \(P(B \mid A)\) representa a probabilidade de haver alta disponibilidade de flores sabendo que ocorreu uma visita de beija-flor.

        Portanto, \(P(A \mid B)\) e \(P(B \mid A)\) não representam necessariamente a mesma situação. A condição considerada muda a pergunta que está sendo feita.
        """)
        st.image("imagens/grafico1.png", width=1000)

    # --- T10: 3. EXEMPLO EM SITUAÇÃO BIOLÓGICA ---
    elif secao_t10 == "3. Exemplo em Situação Biológica":
        st.header("3. Interpretando a probabilidade condicional em uma situação biológica")
        st.markdown("""
        Um exemplo pode ser encontrado no estudo de **Lima-Passos et al. (2026)**, realizado em uma área de Cerrado no estado da Bahia. Durante 13 meses, os pesquisadores registraram 2.233 visitas de quatro espécies de beija-flores a 15 espécies de plantas. O estudo investigou como variações temporais e na disponibilidade de recursos estavam relacionadas às interações entre plantas e beija-flores. Os autores encontraram uma correlação positiva entre a frequência de visitas e a disponibilidade de flores.

        Os resultados também mostraram que a maioria das visitas ocorreu durante a estação chuvosa, correspondendo a **70,9% das visitas**, período em que houve maior abundância de flores. Os autores relacionaram o aumento da abundância de flores durante a estação chuvosa à maior frequência de visitas e de interações agonísticas entre os beija-flores.

        Esses resultados permitem formular uma pergunta probabilística:
        > *"Qual é a probabilidade de observar uma visita de beija-flor quando sabemos que existe alta disponibilidade de flores?"*

        * **Evento A:** Ocorre uma visita de beija-flor.
        * **Evento B:** Há alta disponibilidade de flores.

        Assim, a pergunta pode ser representada matematicamente por \(P(A \mid B)\). Ou seja, é a probabilidade de ocorrer uma visita de beija-flor, dado que há alta disponibilidade de flores.
        
        *Obs: Isso é diferente de simplesmente calcular \(P(A)\), que representaria a probabilidade de uma visita considerando todas as condições observadas.*
        """)

        st.divider()
        st.subheader("3.1 Exemplo com dados simulados")
        st.markdown("""
        Para visualizar essa diferença, podemos imaginar um conjunto hipotético de 100 períodos de observação, inspirado na situação ecológica descrita no estudo.
        """)

        # Tabela simulada
        tabela_dados = {
            "Disponibilidade de flores": ["Alta", "Baixa", "Total"],
            "Visita de beija-flor": [36, 15, 51],
            "Sem visita": [14, 35, 49],
            "Total": [50, 50, 100]
        }
        st.table(tabela_dados)

        st.caption("*Obs: Esses números são simulados e não representam os resultados do estudo de Lima-Passos et al. (2026). Eles servem apenas para demonstrar como os conceitos de probabilidade podem ser applied de forma didática.*")

        st.markdown("""
        Primeiro, podemos calcular a probabilidade geral de ocorrer uma visita:
        """)
        st.latex(r"P(A) = \frac{51}{100} = 0{,}51 \quad (51\%)")

        st.markdown("Agora podemos calcular a probabilidade de uma visita sabendo que a disponibilidade de flores é alta:")
        st.latex(r"P(A \mid B) = \frac{36}{50} = 0{,}72 \quad (72\%)")

        st.markdown("""
        Temos, portanto: **\(P(A) = 51\%\)** e **\(P(A \mid B) = 72\%\)**.
        
        A diferença entre esses valores mostra por que a condição é importante. No exemplo simulado, quando consideramos somente os períodos de alta disponibilidade de flores, a proporção de períodos com visitas de beija-flores é maior do que quando consideramos todas as observações.
        """)

        st.divider()
        st.subheader("3.2 O que esse resultado significa biologicamente?")
        st.markdown("""
        No exemplo simulado, podemos dizer que:
        > *"Quando havia alta disponibilidade de flores, a probabilidade de registrar uma visita de beija-flor era de 72%. Considerando todos os períodos de observação, essa probabilidade era de 51%."*

        Isso demonstra como uma informação sobre o ambiente pode modificar a probabilidade de observar determinado fenômeno biológico.

        O exemplo também ajuda a compreender os resultados de **Lima-Passos et al. (2026)**. O artigo informa que foram registradas 2.233 visitas de quatro espécies de beija-flores a 15 espécies de plantas durante 13 meses. Dentre todas as visitas, 70,9% ocorreram na estação chuvosa e 29,1% na estação seca. No estudo real, os autores observaram que a frequência de visitas dos beija-flores apresentou correlação positiva com a disponibilidade de flores e que o aumento da abundância de flores durante a estação chuvosa esteve associado a uma maior frequência de visitas.

        No artigo podemos definir:
        * **Evento A:** a visita ocorreu durante a estação chuvosa.
        * **Evento B:** foi registrada uma visita de beija-flor.

        E fazer a pergunta: *Qual é a probabilidade de uma visita de beija-flor ter ocorrido durante a estação chuvosa?*

        O estudo informa diretamente que:
        """)
        st.latex(r"P(A \mid B) = 70{,}9\%")
        st.markdown("""
        Ou seja: Dado que uma visita de beija-flor foi registrada, a probabilidade de ela ter ocorrido durante a estação chuvosa foi de 70,9%.
        """)

        st.divider()
        st.subheader("3.3 Probabilidade condicional não significa necessariamente causa")
        st.markdown("""
        Uma diferença importante entre uma associação observada e uma relação de causa e efeito deve ser considerada.

        O fato de a frequência de visitas estar positivamente correlacionada com a disponibilidade de flores não significa, isoladamente, que a disponibilidade de flores seja a única responsável pelo comportamento observado.

        Outros fatores ambientais e biológicos também podem estar envolvidos. O próprio estudo de Lima-Passos et al. (2026) investigou variações sazonais e ao longo do dia, além das interações entre diferentes espécies de beija-flores e plantas.

        Assim, a probabilidade condicional pode ser utilizada para descrever e investigar relações entre eventos, mas sua interpretação deve considerar o contexto biológico e a forma como os dados foram coletados.
        """)

    # --- T10: 4. INDEPENDÊNCIA E DEPENDÊNCIA ---
    elif secao_t10 == "4. Independência e Dependência":
        st.header("4. Independência e dependência entre eventos")
        st.markdown("""
        Quando a ocorrência de um evento não altera a probabilidade de ocorrência do outro, dizemos que os eventos são **independentes**. Por outro lado, quando a ocorrência de um evento modifica a probabilidade do outro, os eventos são considerados **dependentes**.

        A ideia de dependência está relacionada à existência de uma relação entre eventos. **Leão e Laurenti (2009)**, ao discutirem a relação de dependência entre eventos, abordam a existência de interdependências probabilísticas, mostrando que a ocorrência de determinados eventos pode estar relacionada à ocorrência de outros. 

        Considerando novamente os eventos utilizados no exemplo dos beija-flores:
        * **Evento A:** ocorreu uma visita de beija-flor;
        * **Evento B:** havia alta disponibilidade de flores.

        Se saber que havia alta disponibilidade de flores não alterasse a probabilidade de ocorrer uma visita de beija-flor, poderíamos considerar os eventos independentes. Nesse caso:
        """)
        st.latex(r"P(A \mid B) = P(A)")

        st.markdown("""
        Por outro lado, se a probabilidade de ocorrência da visita de um beija-flor for diferente quando sabemos que havia alta disponibilidade de flores, os eventos serão considerados dependentes:
        """)
        st.latex(r"P(A \mid B) \neq P(A)")

        st.markdown("""
        No estudo de Lima-Passos et al. (2026), foi observada uma relação positiva entre a disponibilidade de flores e a frequência de visitas de beija-flores. Essa relação pode ser considerada no contexto do estudo para investigar como esses eventos estão associados, mas não significa, por si só, que exista uma relação de causa e efeito.

        A independência entre dois eventos também pode ser expressa por meio da seguinte relação:
        """)
        st.latex(r"P(A \cap B) = P(A) \times P(B)")

        st.markdown("""
        Assim, quando dois eventos são independentes, a probabilidade de eles ocorrerem simultaneamente pode ser calculada multiplicando suas probabilidades.
        """)

    # --- T10: 5. REGRA DO PRODUTO ---
    elif secao_t10 == "5. Regra do Produto":
        st.header("5. Regra do Produto")
        st.markdown("""
        A **regra do produto** permite calcular a probabilidade de dois eventos ocorrerem simultaneamente. Ela está diretamente relacionada à probabilidade condicional, pois considera a probabilidade de um evento ocorrer sabendo que outro evento já aconteceu.

        A partir da definição de probabilidade condicional, podemos escrever a regra do produto da seguinte forma:
        """)
        st.latex(r"P(A \cap B) = P(B) \times P(A \mid B)")

        st.markdown("""
        Nessa expressão, \(P(A \cap B)\) representa a probabilidade de os eventos \(A\) e \(B\) ocorrerem ao mesmo tempo. \(P(B)\) representa a probabilidade de ocorrência do evento \(B\), enquanto \(P(A \mid B)\) representa a probabilidade de \(A\) ocorrer sabendo que \(B\) ocorreu. 

        No contexto das interações entre beija-flores e plantas, podemos utilizar novamente os eventos:
        * **Evento A:** ocorreu uma visita de beija-flor;
        * **Evento B:** havia alta disponibilidade de flores.

        Nesse caso:
        """)
        st.latex(r"P(A \cap B) = P(B) \times P(A \mid B)")

        st.markdown("""
        Essa expressão representa a probabilidade de ocorrer uma visita de beija-flor e, ao mesmo tempo, haver alta disponibilidade de flores.

        A regra do produto também permite compreender a diferença entre eventos dependentes e independentes. Quando os eventos são dependentes, a probabilidade condicional é utilizada porque a ocorrência de um evento altera a probabilidade do outro. Já quando os eventos são independentes, temos \(P(A \mid B) = P(A)\).

        Nesse caso, a regra do produto pode ser simplificada:
        """)
        st.latex(r"P(A \cap B) = P(B) \times P(A) \quad \text{ou} \quad P(A \cap B) = P(A) \times P(B)")

    # --- T10: 6. RELAÇÃO ENTRE CONCEITOS ---
    elif secao_t10 == "6. Relação entre os Conceitos":
        st.header("6. Relação entre probabilidade condicional e regra do produto")
        st.markdown("""
        A probabilidade condicional e a regra do produto estão diretamente relacionadas. A regra do produto pode ser obtida a partir da própria fórmula da probabilidade condicional, mostrando que os dois conceitos não são independentes entre si.

        A probabilidade de um evento \(A\) ocorrer sabendo que \(B\) ocorreu é dada por:
        """)
        st.latex(r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}")

        st.markdown("""
        Para obter a regra do produto, podemos reorganizar essa expressão. Multiplicando os dois lados da equação por \(P(B)\), temos:
        """)
        st.latex(r"P(A \mid B) \times P(B) = P(A \cap B)")

        st.markdown("Assim, podemos escrever:")
        st.latex(r"P(A \cap B) = P(B) \times P(A \mid B)")

        st.markdown("""
        Podemos interpretar essa relação pensando novamente no exemplo dos beija-flores:
        * **Evento A:** ocorreu uma visita de beija-flor;
        * **Evento B:** havia alta disponibilidade de flores.

        A probabilidade condicional \(P(A \mid B)\) indica a probabilidade de ocorrer uma visita de beija-flor quando sabemos que havia alta disponibilidade de flores. Já \(P(B)\) indica a probabilidade de haver alta disponibilidade de flores.

        Ao multiplicarmos essas duas probabilidades, obtemos \(P(A \cap B)\), que representa a probabilidade de ocorrer uma visita de beija-flor e, simultaneamente, haver alta disponibilidade de flores.
        """)

    # --- T10: 7. EXEMPLO INTEGRADO APLICADO ---
    elif secao_t10 == "7. Exemplo Integrado Aplicado":
        st.header("7. Exemplo integrado aplicado à Biologia")
        st.markdown("""
        Nos tópicos anteriores, calculamos separadamente a probabilidade condicional (tópico 3), discutimos independência e dependência entre eventos (tópico 4) e apresentamos a regra do produto (tópico 5). Para mostrar como esses conceitos se conectam, vamos retomar a mesma tabela de dados simulados usada anteriormente e completá-la com essas duas análises que ainda faltavam.
        """)

        tabela_dados = {
            "Disponibilidade de flores": ["Alta", "Baixa", "Total"],
            "Visita de beija-flor": [36, 15, 51],
            "Sem visita": [14, 35, 49],
            "Total": [50, 50, 100]
        }
        st.table(tabela_dados)

        st.markdown("""
        Retomando os eventos definidos no tópico 2 (**Evento A:** ocorreu uma visita de beija-flor; **Evento B:** havia alta disponibilidade de flores), já sabemos, do tópico 3, que \(P(B) = 0{,}50\) e \(P(A \mid B) = 0{,}72\).

        #### 1. Verificando independência
        Se A e B fossem independentes, esperaríamos \(P(A \mid B) = P(A)\). 
        
        Mas \(P(A) = \frac{51}{100} = 0{,}51\), enquanto \(P(A \mid B) = 0{,}72\). 
        
        Como os valores são diferentes, **os eventos são dependentes** (saber que a disponibilidade de flores era alta muda a probabilidade de observarmos uma visita).

        Podemos confirmar isso pela outra forma de checar independência: 
        """)
        st.latex(r"P(A) \times P(B) = 0{,}51 \times 0{,}50 = 0{,}255")
        st.markdown("""
        enquanto a probabilidade conjunta observada na tabela é \(P(A \cap B) = \frac{36}{100} = 0{,}36\). Como \(0{,}255 \neq 0{,}36\), a conclusão se confirma.

        #### 2. Aplicando a regra do produto
        Como os eventos são dependentes, usamos a forma geral da regra do produto, e não a versão simplificada de eventos independentes:
        """)
        st.latex(r"P(A \cap B) = P(B) \times P(A \mid B) = 0{,}50 \times 0{,}72 = 0{,}36")
        st.markdown("""
        O resultado bate exatamente com o valor observado diretamente na tabela (\(\frac{36}{100} = 0{,}36\)), o que confirma que a fórmula está sendo aplicada corretamente. Da mesma forma, para a disponibilidade baixa:
        """)
        st.latex(r"P(A \cap B') = P(B') \times P(A \mid B') = 0{,}50 \times 0{,}30 = 0{,}15")
        st.markdown("""
        que também corresponde ao valor da tabela (\(\frac{15}{100}\)).

        #### 3. Interpretação biológica integrada
        O exemplo mostra como os três conceitos se conectam:
        * **A probabilidade condicional** nos diz o quanto a chance de visita muda quando há alta disponibilidade de flores;
        * **O teste de independência** nos diz que essa diferença é real, e não um evento independente; 
        * **E a regra do produto** nos permitiu calcular, a partir dessas informações, a chance de as duas condições ocorrerem juntas. 

        Esse tipo de raciocínio é útil, por exemplo, para estimar com que frequência se espera observar simultaneamente alta disponibilidade de recursos florais e visitas de beija-flores em um levantamento de campo, o que é visto com os resultados de Lima-Passos et al. (2026) sobre a associação entre disponibilidade de flores e frequência de interações.
        """)

    # --- T10: 8. VÍDEOS RECOMENDADOS ---
    elif secao_t10 == "8. Vídeos Recomendados":
        st.header("8. Vídeos recomendados e comentados")
        st.write("Seleção de vídeos para aprofundamento e consolidação dos conceitos de probabilidade condicional, independência e regra do produto.")

        st.subheader("1. Probabilidade Condicional")
        st.video("https://youtu.be/WlUgwydaLcw?si=MUOtXtpbZ_AfClP0")
        st.markdown("**Canal:** Dicasdemat Sandro Curió")
        st.markdown("**Conceito explicado:** Probabilidade Condicional")
        st.markdown("**Comentário dos autores:** O vídeo acima foi selecionado como forma de reforçar o conteúdo de uma forma didática e simples.")
        st.markdown("---")

        st.subheader("2. Dependência e Independência de Eventos")
        st.video("https://youtu.be/Q6CGLHP-818?si=5HeorRCe1Y7ZDFXG")
        st.markdown("**Canal:** Professora Gisele Ramos")
        st.markdown("**Conceito explicado:** Eventos dependentes e independentes")
        st.markdown("**Comentário dos autores:** O vídeo foi selecionado por detalhar a diferença entre os eventos dependentes e independentes de forma visual.")
        st.markdown("---")

        st.subheader("3. Regra do Produto")
        st.video("https://youtu.be/MERwJ8hEQgA?si=HQhEJeycfy5QXadA")
        st.markdown("**Canal:** Pró Universidade Online")
        st.markdown("**Conceito explicado:** Regra do produto")
        st.markdown("**Comentário dos autores:** Para abordar a regra do produto em cáculos de probabilidade simultâneos, foi escolhido o vídeo do Prof. Felipe pela sua boa didática e clara explicação.")
        st.markdown("---")

        st.subheader("4. Regra do Produto")
        st.video("https://youtu.be/tz6_xy6Xvbg?si=LNzMMNcNCH7s2yHz")
        st.markdown("**Canal:** Universo Narrado Militares")
        st.markdown("**Conceito explicado:** Regra do produto")
        st.markdown("**Comentário dos autores:** Para reforçar o conteúdo de regra do produto foi escolhido o seguinte vídeo por apresentar exemplos e exercícios práticos do conteúdo.")

    # --- T10: 9. CONCLUSÃO & REFERÊNCIAS ---
    elif secao_t10 == "9. Conclusão & Referências":
        st.header("9. Conclusão")
        st.markdown("""
        A probabilidade condicional e suas ferramentas derivadas, a avaliação de independência e a regra do produto, constituem pilares fundamentais para a interpretação quantitativa de sistemas ecológicos complexos.

        Em ecologia, onde múltiplos fatores ambientais e comportamentais se entrelaçam, avaliar a ocorrência de um evento sob a influência de outro permite que o pesquisador vá além da simples descrição observacional. Essa abordagem torna possível modelar a dinâmica de interações, como o forrageamento e a polinização, fornecendo uma base rigorosa para prever e compreender os padrões da biodiversidade.
        """)

        st.divider()
        st.header("📚 Referências Bibliográficas")
        st.markdown("""
        - FIGUEIREDO, A. C. **Probabilidade condicional: um enfoque de seu ensino-aprendizagem**. 2000. 158 f. Dissertação (Mestrado em Educação) - Pontifícia Universidade Católica de São Paulo, São Paulo, 2000. Disponível em: https://repositorio.pucsp.br/jspui/handle/handle/11214
        - LEÃO, M. F. F. C.; LAURENTI, C. Uma análise do modelo de explicação no behaviorismo radical: o estatuto do comportamento e a relação de dependência entre eventos. **Interação em Psicologia**, Curitiba, Paraná, Brasil, v. 13, n. 1, 2009. DOI: 10.5380/psi.v13i1.12462. Disponível em: https://revistas.ufpr.br/psicologia/article/view/12462.
        """)