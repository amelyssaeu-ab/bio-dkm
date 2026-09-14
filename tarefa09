import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Blog de Probabilidade em Biologia",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------------------------------------------------------
# BARRA LATERAL - NAVEGAÇÃO
# -----------------------------------------------------------------------------
st.sidebar.title("📌 Navegação")
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
    ]
)

# -----------------------------------------------------------------------------
# SEÇÃO: INÍCIO & AUTORES
# -----------------------------------------------------------------------------
if secao == "Início & Autores":
    st.title("🧬 Probabilidade Aplicada à Biologia")
    st.caption("Conceitos, conjuntos e aplicações")
    st.markdown("---")
    
    st.header("👥 Autores")
    st.write("Conheça as integrantes do grupo responsáveis pela elaboração deste site.")
    
    # Exemplo de colunas para autores em ordem alfabética por sobrenome
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Substitua por uma imagem real ou caminho de arquivo local (ex: 'imagens/autor1.jpg')
        st.image("https://via.placeholder.com/150", width=150)
        st.markdown("**Nome:** Drielly Mathias")
        st.markdown("**Curso:** Ciências Biologicas")
        st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
        st.markdown("""
        **Contribuições:**
        - Elaboração da introdução do blog;
        - Construção do exemplo biológico, relacionando os conceitos de Probabilidade à Biologia;
        - Elaboração dos exemplos de eventos e das operações entre conjuntos;
        - Produção de diagramas de Venn e outros recursos visuais;
        - Pesquisa, seleção e formatação das referências bibliográficas utilizadas no blog.""")
       
    
    with col2:
        st.image("https://via.placeholder.com/150", width=150)
        st.markdown("**Nome:** Kawana Ganeo")
        st.markdown("**Curso:** Ciências Biologicas")
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
        st.image("https://via.placeholder.com/150", width=150)
        st.markdown("**Nome:** Melyssa Ponce")
        st.markdown("**Curso:** Ciências Biologicas")
        st.markdown("**Instituição:** Escola Superior de Agricultura Luiz de Queiroz - USP")
        st.markdown("""
        **Contribuições:** 
        - Construção e programação do site/blog;
        - Elaboração da conclusão do blog;
        - Seleção de vídeos relacionados ao tema;
        - Elaboração de comentários e contextualização dos vídeos selecionados;
        - Organização e inserção dos conteúdos e recursos multimídia no site, contribuindo para sua apresentação e funcionalidade.
        """)

    # Logo após o bloco 'with col3:'
    st.markdown("---")  # Linha divisória opcional para separar visualmente

    st.info("""
    **Observação:** Todas as integrantes participaram ativamente das discussões e contribuíram para a pesquisa, seleção e compreensão dos conteúdos abordados, especialmente em relação aos conceitos de Probabilidade. As atividades foram desenvolvidas de forma colaborativa, com troca de ideias, revisão conjunta e auxílio mútuo ao longo da elaboração do blog.
    """)

# -----------------------------------------------------------------------------
# SEÇÃO: INTRODUÇÃO
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# SEÇÃO: HISTÓRICO
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# SEÇÃO: CONCEITOS FUNDAMENTAIS
# -----------------------------------------------------------------------------
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
    st.latex(r"S = \{par,ímpar\}")
    st.markdown("""
    Portanto, antes de analisar a probabilidade de um acontecimento, é importante definir claramente qual é o experimento e quais são os resultados que serão considerados possíveis.
    """)
    st.markdown("""
    Considerando o exemplo das aves, Se o objetivo for selecionar aleatoriamente uma visita registrada e identificar **qual espécie de ave foi observada**, os resultados possíveis serão as 14 espécies registradas no estudo.
    """)
    st.markdown("""
    Nesse caso, o espaço amostral pode ser representado por:
    """)
    st.latex(r"S = \{Thraupis sayaca, Thraupis palmarum, Tangara cayana, Pitangus sulphuratus, Mimus saturninus, Turdus leucomelas, Euphonia chlorotica, Turdus amaurochalinus, Passer domesticus, Zonotrichia capensis, Icterus pyrrhopterus, Colaptes melanochloros, Molothrus bonariensis, Saltator similis\}")
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
    st.latex(r"S = \{2,4,6\}")
    st.markdown("""
    Observe que todos os elementos de **A** também pertencem ao espaço amostral **S**. Por isso, dizemos que **A é um subconjunto de S**, o que pode ser representado por:
    """)
    st.latex(r"A \subseteq S")
    st.markdown("""
    Um evento pode ser formado por **apenas um resultado**, por vários resultados ou, em situações específicas, por nenhum resultado. Quando um evento possui apenas um resultado possível, ele é chamado de **evento simples**. Por exemplo:
    """)
    st.latex(r"B = \{4\}")
    st.markdown("""
    O evento B corresponde à ocorrência do resultado 4.
    """)
    st.markdown("""
    Já um evento formado por vários resultados é chamado de **evento composto**. Por exemplo:
    """)
    st.latex(r"C = \{1,3,5\}")
    st.markdown("""
    Nesse caso, o evento corresponde à obtenção de um número ímpar.
    """)
    st.markdown("""
    Também podemos ter um **evento impossível**, que não contém nenhum resultado do espaço amostral. Esse tipo de evento é representado pelo **conjunto vazio (∅).**
    """)
    st.markdown("""
    Os eventos podem assumir diferentes formas. Um evento pode conter apenas um resultado, vários resultados ou até mesmo nenhum resultado. A definição do evento depende da pergunta que o pesquisador deseja investigar.
    """)

# -----------------------------------------------------------------------------
# SEÇÃO: TEORIA DE CONJUNTOS
# -----------------------------------------------------------------------------
elif secao == "4. Teoria de Conjuntos":
    st.header("4. Teoria de Conjuntos Aplicada à Probabilidade")
    
    st.markdown("""
    A **Teoria de Conjuntos** é uma área da Matemática que estuda conjuntos, ou seja, agrupamentos de elementos que possuem alguma característica em comum. Na Probabilidade, essa teoria é importante porque permite **representar e organizar os resultados de um experimento aleatório**, facilitando a análise dos eventos.
    """)
    st.markdown("""
    Como vimos anteriormente, o **espaço amostral (S)** reúne todos os resultados possíveis de um experimento, enquanto um **evento** é um subconjunto desse espaço amostral. Dessa forma, podemos utilizar conceitos e operações da Teoria de Conjuntos para representar diferentes acontecimentos e investigar a relação entre eles.
    """)

    st.divider()
    st.markdown("""
    Alguns conceitos básicos são:
    """)
    st.markdown("##### Conjunto")
    st.markdown("""
    Um conjunto é uma coleção de elementos que possuem alguma característica ou condição em comum. Na Probabilidade, um conjunto pode representar um **evento**.
    """)
    st.markdown("""
    Por exemplo, considerando o lançamento de um dado:
    """)
    st.latex(r"S = \{1,2,3,4,5,6\}")
    st.markdown("""
    Podemos definir:
    """)
    st.latex(r"A = \{2,4,6\}")
    st.markdown("""
    Nesse caso, **A** é o conjunto dos resultados que correspondem à obtenção de um número par. Como todos os elementos de A também pertencem a S, dizemos que **A é um subconjunto de S**:
    """)
    st.latex(r"A \subseteq S")
    st.markdown("##### Elemento")
    st.markdown("""
    Um elemento é cada objeto ou resultado que pertence a um conjunto. O símbolo ∈ significa “pertence a”. Por exemplo:
    """)
    st.latex(r"4 \subseteq A")
    st.markdown("""
    Isso significa que o número 4 pertence ao conjunto A.
    """)
    st.latex(r"\text{Já: } 3 \notin A")
    st.markdown("##### Subconjunto")
    st.markdown("""
    Um conjunto **A** é considerado subconjunto de **S** quando todos os elementos de A também pertencem a S. Essa relação é representada por: **A ⊆ S**
    """)
    st.markdown("""
    Na Probabilidade, essa relação é importante porque **todo evento é um subconjunto do espaço amostral.**
    """)
    st.divider()

    st.markdown("""
    A partir desses conceitos, podemos realizar **operações entre conjuntos**, que também podem ser aplicadas aos eventos de um experimento aleatório. As principais são a **união, a interseção e o complemento.**
    """)
    st.markdown("##### União (A ∪ B):")
    st.markdown("""
    A **união** de dois conjuntos reúne todos os elementos que pertencem a **A, a B ou a ambos.** Na Probabilidade, a união representa a ocorrência de **pelo menos um dos eventos.**
    """)
    st.markdown("##### Interseção (A ∩ B):")
    st.markdown("""
    A **interseção** reúne apenas os elementos que pertencem **simultaneamente aos dois conjuntos.** Na Probabilidade, representa a ocorrência dos **dois eventos ao mesmo tempo.**
    """)
    st.markdown("##### Complemento (Aᶜ)")
    st.markdown("""
    O **complemento de um evento A** é formado por todos os resultados do espaço amostral que **não pertencem a A.** Na Probabilidade, o complemento representa a situação em que o **evento A não ocorre.**
    """)
    st.latex(r"Aᶜ = \{S - A\}")
    
    # Exemplo de Diagrama de Venn
    st.subheader("Representação Visual")
    # Substitua pelo arquivo do seu diagrama autoral (ex: 'imagens/diagrama_venn.png')
    st.image("https://via.placeholder.com/500x300", caption="Figura 1: Diagrama de Venn ilustrando a interseção entre eventos. Fonte: elaboração dos autores.")

# -----------------------------------------------------------------------------
# SEÇÃO: EXEMPLO INTEGRADO
# -----------------------------------------------------------------------------
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
    st.markdown("Espaço amostral (S): Nesse caso, o **espaço amostral** é formado pelas **166 visitas registradas no estudo**, considerando cada visita como um possível resultado do experimento. Cada resultado corresponde a uma visita específica e possui características observadas no estudo, como a **espécie da ave** e o **tempo de permanência no comedouro.**")
    st.latex(r"S = \{\text{todas as 166 visitas registradas}\}")
    st.markdown("")
    st.markdown("**Evento A:** “a visita selecionada foi realizada por uma ave da espécie _Thraupis sayaca_”.")
    st.markdown("Portanto, **A** reúne todas as visitas, dentro das 166 registradas, que foram realizadas por _Thraupis sayaca_. Como a espécie apresentou **56 visitas**, o evento A possui 56 resultados.")
    st.markdown("**Evento B:** “o tempo de permanência da visita selecionada foi superior a 60 segundos”.")
    st.markdown("Nesse caso, B reúne todas as visitas, entre as 166 registradas, nas quais a ave permaneceu no comedouro por mais de 60 segundos.")
    st.markdown("")
    st.markdown("""
    A partir desses dois eventos, podemos aplicar algumas **operações entre conjuntos:**
    - **A ∪ B:** a visita selecionada foi realizada por _Thraupis sayaca_ **ou** teve duração superior a 60 segundos, incluindo também as visitas que apresentam as duas características simultaneamente.
    - **A ∩ B:** a visita selecionada foi realizada por _Thraupis sayaca_ **e** teve duração superior a 60 segundos. Nesse caso, estamos considerando somente as visitas que satisfazem as duas condições ao mesmo tempo.
    - **Aᶜ:** a visita selecionada **não** foi realizada por _Thraupis sayaca_. Considerando as 14 espécies registradas, esse evento corresponde às visitas realizadas pelas outras 13 espécies.
    - **∅ (evento impossível):** Esse evento é impossível porque o pinguim-de-Magalhães não está entre as espécies registradas no estudo. Portanto, não existe nenhuma das 166 visitas que satisfaça essa condição. Esse exemplo corresponde ao **conjunto vazio (∅)**, pois não há nenhum resultado do espaço amostral que pertença a esse evento.
    """)
    st.markdown("")
    st.markdown("")
    st.markdown("")
# -----------------------------------------------------------------------------
# SEÇÃO: VÍDEOS RECOMENDADOS
# -----------------------------------------------------------------------------
elif secao == "6. Vídeos Recomendados":
    st.header("6. Vídeos Recomendados e Comentados")
    st.write("Seleção de materiais complementares para aprofundamento nos conceitos de Probabilidade.")
    
    # Vídeo 1
    st.subheader("1. Introdução à Probabilidade")
    st.video("https://www.youtube.com/watch?v=k3G_n0m6pDA") # Substituir pela URL real do YouTube
    st.markdown("**Canal:** Exemplo Canal Educativo")
    st.markdown("**Conceito explicado:** Espaço amostral e eventos.")
    st.markdown("**Comentário dos autores:** *Este vídeo foi selecionado por apresentar de forma clara a intuição básica por trás da probabilidade...*")
    
    st.markdown("---")

# -----------------------------------------------------------------------------
# SEÇÃO: CONCLUSÃO & REFERÊNCIAS
# -----------------------------------------------------------------------------
elif secao == "7. Conclusão & Referências":
    st.header("7. Conclusão")
    st.write("Síntese das discussões e a importância do pensamento probabilístico na biologia...")
    
    st.header("8. Referências Bibliográficas")
    st.markdown("""
    - BUSSAB, Wilton de Oliveira; MORETTIN, Pedro Alberto. **Estatística Básica**. 9. ed. São Paulo: Saraiva, 2017.
    - MAGALHÃES, Marcos Nascimento; LIMA, Antonio Carlos Pedroso de. **Noções de Probabilidade e Estatística**. 7. ed. São Paulo: EdUSP, 2015.
    """)
