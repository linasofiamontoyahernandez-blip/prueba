import streamlit as st

# Título de la app
st.title("Cuestionario: Influencia de las redes sociales en la autoestima (15-25 años)")

# Preguntar nombre y edad
nombre = st.text_input("Ingresa tu nombre")
edad = st.number_input("Ingresa tu edad", min_value=15, max_value=25, step=1)

# Definir preguntas (positivo/negativo)
preguntas = [
    ("Me siento valioso/a aunque no reciba muchos 'me gusta' en redes sociales.", "positivo"),
    ("Si no obtengo atención en redes sociales, pienso que no valgo lo suficiente.", "negativo"),
    ("Las redes sociales me ayudan a sentirme seguro/a de mí mismo/a.", "positivo"),
    ("Me comparo demasiado con lo que publican otros y eso afecta mi autoestima.", "negativo"),
    ("Puedo sentirme orgulloso/a de mí mismo/a incluso si no comparto nada en redes.", "positivo"),
    ("Si recibo pocos comentarios o reacciones, siento que soy menos importante.", "negativo"),
    ("Mi valor como persona no depende de lo que muestro en redes sociales.", "positivo"),
    ("Cuando veo publicaciones de éxito de otros, siento que no estoy a su nivel.", "negativo"),
    ("Las redes sociales refuerzan mi confianza personal.", "positivo"),
    ("Si elimino una publicación por poca interacción, siento que he fracasado.", "negativo"),
    ("Me siento digno/a de aprecio aunque no use redes sociales constantemente.", "positivo"),
    ("Las comparaciones en redes me hacen sentir inferior a los demás.", "negativo"),
    ("Me considero capaz y valioso/a independientemente de mi popularidad en línea.", "positivo"),
    ("Cuando no tengo seguidores nuevos, pienso que no soy interesante.", "negativo"),
    ("En general, me acepto y me valoro aunque no sea muy activo/a en redes.", "positivo")
]

# Diccionario para respuestas
respuestas = {}

st.subheader("Responde cada pregunta (1=Totalmente en desacuerdo, 4=Totalmente de acuerdo)")

for i, (pregunta, tipo) in enumerate(preguntas, 1):
    respuestas[i] = st.radio(pregunta, [1, 2, 3, 4], horizontal=True, key=f"q{i}")

# Botón para calcular resultado
if st.button("Calcular resultados"):
    puntaje = 0
    for i, (pregunta, tipo) in enumerate(preguntas, 1):
        if tipo == "positivo":
            puntaje += respuestas[i]
        else:
            puntaje += (5 - respuestas[i])

    st.success(f"Puntaje total de {nombre} (edad {edad}): {puntaje} / 60")

    # Interpretación psicológica
    if puntaje <= 30:
        st.error("Autoestima baja influenciada por redes sociales.")
        st.write("Estudios psicológicos muestran que una autoestima baja suele estar asociada con mayor vulnerabilidad a la comparación social en plataformas digitales (Vogel et al., 2014). Esto puede generar sentimientos de insuficiencia, ansiedad y síntomas depresivos.")
    elif 31 <= puntaje <= 45:
        st.warning("Autoestima media, cierta influencia de redes sociales.")
        st.write("Investigaciones han demostrado que un nivel intermedio de autoestima indica que, aunque la persona logra mantener una visión relativamente positiva de sí misma, sigue siendo susceptible a la influencia de las redes sociales (Perloff, 2014). Puede experimentar altibajos en su autoimagen.")
    else:
        st.success("Autoestima alta, redes sociales no afectan de manera negativa significativa.")
        st.write("La literatura psicológica indica que los jóvenes con alta autoestima tienden a usar las redes sociales de forma más crítica y saludable, sin depender fuertemente de la aprobación externa (Orth & Robins, 2014). Esto les permite mantener un autoconcepto sólido.")

    st.info("Nota: Este cuestionario es una adaptación de la Escala de Rosenberg y no sustituye una evaluación psicológica profesional.")
