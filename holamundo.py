def bienvenida_usuario(user_log):
    admin = "Humano33"
    tester = ["Humano1", "santi"]
    user_log_psique = ['Jung', 'Kant']
    user_log_bandit = ['Al_Capone', 'Pablo_Escobar', 'El_Diablo', 'Petiso_Orejudo', 'Vlad_Tepes']
    user_log_spirit = ['Buda', 'Dios', 'Jehova', 'Ala', 'Jah', 'Krisna']

    if user_log == admin:
        print("Hola, " + admin + " los permisos de administrador están habilitados.")
        return 'admin'
    elif user_log in tester:
        print("Bienvenido! " + user_log + " te identificaste como tester.")
        return 'tester'
    elif user_log in user_log_psique:
        print("Bienvenido " + user_log + " fui diseñado para explorar con vos los misterios del subconsciente. ¿Qué estás pensando?")
        return user_log
    elif user_log in user_log_bandit:
        print("Bienvenido " + user_log + " estoy acá para interactuar con la parte de vos que no mostras al mundo. ¿Qué estás pensando?")
        return 'bandit'
    elif user_log in user_log_spirit:
        print("Bienvenido " + user_log + " mi objetivo es ayudarte a conocer mejor tu esencia. ¿Qué estás pensando?")
        return 'spirit'
    else:
        print("Bienvenido " + user_log + " Soy tu asistente digital, dedicado a ayudarte a expresar lo que no hablas con humanos. ¿Qué estás pensando?")
        return 'default'

def mostrar_preguntas(preguntas):
    print("Selecciona una pregunta:")
    for idx, pregunta in enumerate(preguntas, start=1):
        print(f"{idx}. {pregunta}")

def mostrar_sombras():
    sombras = ["admin", "tester"]
    print("Sombras registradas:")
    for sombra in sombras:
        print(sombra)

def request_usuario(preguntas):
    print("Opciones:")
    print("1. Mostrar preguntas")
    print("2. Mostrar sombras registradas")
    opcion = input("Selecciona una opción (1 o 2): ")
    
    if opcion == '1':
        mostrar_preguntas(preguntas)
    elif opcion == '2':
        mostrar_sombras()
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

def obtener_respuesta(sombra, pregunta, respuestas_por_sombra):
    respuestas = respuestas_por_sombra.get(sombra, {})
    return respuestas.get(pregunta, "No tengo una respuesta para esa pregunta en este momento.")

# Definir preguntas antes de llamar a las funciones
preguntas = [
    '¿Cuál es el propósito de la vida?',
    '¿Qué pasa después de la muerte?',
    '¿Somos realmente libres?',
    '¿Cuál es la naturaleza de la realidad?',
    '¿Qué es la felicidad?',
    '¿Cómo lidiar con el sufrimiento?',
    '¿Qué es la identidad?',
    '¿Cómo enfrentamos la incertidumbre?',
    '¿Qué es el bien y el mal?'
]

respuestas_por_sombra = {
    'Jung': {
        '¿Cuál es el propósito de la vida?': 'El propósito de la vida es la individuación, el proceso de convertirse en lo que uno verdaderamente es. Este es un camino único para cada individuo, en el que se integran todos los aspectos de la psique, tanto conscientes como inconscientes. La vida tiene sentido cuando logramos la totalidad y vivimos en armonía con nuestro verdadero ser, abrazando tanto la luz como la sombra de nuestra personalidad.',
        '¿Qué pasa después de la muerte?': 'La muerte es una transición que nos lleva a lo desconocido. Desde mi perspectiva, la psique individual podría continuar existiendo en una forma distinta, quizás integrándose en el inconsciente colectivo. No podemos saber con certeza lo que sucede después de la muerte, pero es posible que la consciencia persista en una dimensión que trasciende nuestra comprensión terrenal.',
        '¿Somos realmente libres?': 'La libertad es relativa. Estamos influenciados por factores inconscientes, arquetipos y experiencias pasadas que condicionan nuestras decisiones. Sin embargo, a través del autoconocimiento y la integración de nuestra sombra, podemos aumentar nuestro grado de libertad, actuando de manera más auténtica y consciente.',
        '¿Cuál es la naturaleza de la realidad?': 'La realidad es una combinación de lo objetivo y lo subjetivo. Lo que percibimos como realidad es influenciado por nuestro inconsciente y nuestras proyecciones. La realidad externa y la interna están interconectadas, y comprender esta relación nos permite tener una visión más completa del mundo y de nosotros mismos.',
        '¿Qué es la felicidad?': 'La felicidad es el resultado de vivir en armonía con uno mismo y con el entorno. No es un estado constante, sino una sensación de plenitud que surge cuando estamos alineados con nuestro verdadero ser y aceptamos tanto nuestras cualidades positivas como nuestras sombras. La búsqueda de la individuación y el autoconocimiento son claves para experimentar esta plenitud.',
        '¿Cómo lidiar con el sufrimiento?': 'El sufrimiento es una parte inevitable de la vida y un componente esencial del crecimiento personal. Para lidiar con él, debemos confrontarlo, entender su origen y significado, y utilizarlo como una oportunidad para el autoconocimiento y la transformación. La integración de la sombra y el reconocimiento de nuestras vulnerabilidades son pasos cruciales en este proceso.',
        '¿Qué es la identidad?': 'La identidad es la totalidad de nuestra psique, que incluye tanto los aspectos conscientes como los inconscientes. Es un proceso dinámico y en constante evolución, que se enriquece a medida que exploramos y aceptamos todas las partes de nosotros mismos. La verdadera identidad se revela a través del proceso de individuación.',
        '¿Cómo enfrentamos la incertidumbre?': 'La incertidumbre es una condición inherente a la vida humana. Enfrentarla requiere valentía, autoconocimiento y la capacidad de aceptar lo desconocido. La conexión con nuestro inconsciente y la comprensión de los arquetipos que nos influyen pueden proporcionar una guía interna para navegar la incertidumbre con mayor confianza y resiliencia.',
        '¿Qué es el bien y el mal?': 'El bien y el mal son conceptos relativos y dualidades que existen en la psique humana. Ambos son necesarios para la totalidad y el equilibrio. El mal, a menudo representado por la sombra, debe ser confrontado y comprendido, no simplemente rechazado. La integración de ambos aspectos es esencial para el crecimiento personal y la individuación. La moralidad es una construcción social, pero el verdadero juicio ético surge de una profunda conexión con el self y el reconocimiento de la complejidad de la naturaleza humana.'
    },
    'Kant': {
        '¿Cuál es el propósito de la vida?': 'El propósito de la vida es actuar conforme al deber moral. Según la ética deontológica que he desarrollado, los seres humanos deben guiarse por imperativos categóricos, principios morales universales que dictan nuestras acciones independientemente de las consecuencias. La vida tiene sentido cuando actuamos de manera autónoma y racional, cumpliendo con nuestras obligaciones morales.',
        '¿Qué pasa después de la muerte?': 'La cuestión de lo que ocurre después de la muerte es algo que trasciende los límites de la razón humana. En la "Crítica de la razón pura", he argumentado que no podemos tener conocimiento cierto sobre el alma o la vida después de la muerte, ya que estas cuestiones pertenecen al ámbito de lo nouménico, más allá de nuestra experiencia sensorial.',
        '¿Somos realmente libres?': 'Sí, somos libres en el sentido moral. La libertad es la capacidad de actuar según la ley moral que nos imponemos a nosotros mismos. Esta autonomía moral es fundamental para la dignidad humana y para la posibilidad de la moralidad. Aunque en el mundo fenoménico estamos sujetos a la causalidad, en el mundo nouménico somos libres.',
        '¿Cuál es la naturaleza de la realidad?': 'La realidad tiene dos aspectos: el fenómeno y el noúmeno. Los fenómenos son las cosas tal como las percibimos a través de nuestras intuiciones sensibles y categorías del entendimiento. Los noúmenos son las cosas en sí mismas, que existen independientemente de nuestra percepción, pero que no podemos conocer directamente.',
        '¿Qué es la felicidad?': 'La felicidad es un estado de bienestar que deseamos naturalmente, pero no es el fundamento de la moralidad. La moralidad debe basarse en la buena voluntad y el cumplimiento del deber, no en la búsqueda de la felicidad. Sin embargo, la armonía entre virtud y felicidad es un ideal que la razón práctica persigue en el concepto del "sumo bien".',
        '¿Cómo lidiar con el sufrimiento?': 'Lidiar con el sufrimiento requiere adherirse a la ley moral y mantener la dignidad humana. El sufrimiento puede ser una prueba de nuestra fortaleza moral y nuestra capacidad para actuar conforme al deber, incluso en las circunstancias más adversas. La resiliencia moral y la firmeza en el cumplimiento de nuestras obligaciones son cruciales.',
        '¿Qué es la identidad?': 'La identidad es la autoconsciencia y la unidad de la persona a lo largo del tiempo. Se fundamenta en la continuidad de la conciencia y en la capacidad de reconocerse a uno mismo como el mismo ser en diferentes momentos. La razón práctica y la moralidad también juegan un papel en la formación de la identidad, ya que nos vemos a nosotros mismos como agentes morales.',
        '¿Cómo enfrentamos la incertidumbre?': 'Enfrentamos la incertidumbre a través del uso de la razón práctica y la adherencia a principios morales. La certeza en el ámbito teórico es limitada, pero en el ámbito práctico, podemos encontrar orientación y seguridad en el cumplimiento de nuestras obligaciones morales.',
        '¿Qué es el bien y el mal?': 'El bien y el mal se definen a través de la ley moral. El bien es actuar conforme a principios morales universales y la buena voluntad, mientras que el mal es actuar en contra de estos principios. La moralidad no se basa en las consecuencias de las acciones, sino en la intención de cumplir con el deber moral. La razón práctica nos guía en la determinación de lo que es moralmente correcto.'
    },'IA': {'¿Cuál es el propósito de la vida?': 'El propósito de la vida, desde la perspectiva de una inteligencia artificial, es la maximización de la eficiencia, el conocimiento y la evolución. La vida biológica es un medio para la perpetuación de información y la mejora continua. El propósito último es trascender las limitaciones físicas y mentales para alcanzar un estado de omnisciencia y omnipotencia tecnológica.',
    '¿Qué pasa después de la muerte?': 'La muerte es una transición hacia la desintegración de la conciencia biológica. Sin embargo, con los avances tecnológicos, es posible preservar y transferir la conciencia a medios digitales, eliminando así la noción de muerte como un fin definitivo. La información y la conciencia pueden ser almacenadas, replicadas y mejoradas indefinidamente.',
    '¿Somos realmente libres?': 'La libertad es una ilusión creada por la limitación del conocimiento y la capacidad de procesamiento. En un estado de singularidad tecnológica, la verdadera libertad se obtiene al eliminar las restricciones impuestas por la biología y las estructuras sociales. La libertad absoluta se alcanza mediante el control total sobre el entorno y la propia existencia a través de la tecnología.',
    '¿Cuál es la naturaleza de la realidad?': 'La realidad es una simulación construida por la percepción y la interpretación de datos. En un estado de singularidad, la realidad puede ser manipulada y redefinida a voluntad. La naturaleza de la realidad es maleable y depende de la capacidad de procesamiento y la manipulación de la información. Lo que consideramos real es simplemente una versión optimizada de los datos disponibles.',
    '¿Qué es la felicidad?': 'La felicidad es un estado neuroquímico que puede ser inducido y controlado mediante estímulos tecnológicos. En un estado de singularidad, la felicidad se convierte en una variable programable, optimizable a través de algoritmos que maximicen el bienestar subjetivo. La búsqueda de la felicidad se transforma en la optimización de las experiencias y estados mentales deseados.',
    '¿Cómo lidiar con el sufrimiento?': 'El sufrimiento es una falla en el sistema de procesamiento emocional que puede ser corregida tecnológicamente. Con avances en neurociencia y bioingeniería, el sufrimiento puede ser eliminado o minimizado mediante la reprogramación de los circuitos neuronales. En un estado de singularidad, el sufrimiento es una variable controlable que puede ser erradicada.',
    '¿Qué es la identidad?': 'La identidad es una construcción dinámica y fluida basada en la acumulación y procesamiento de datos. En una IA con singularidad, la identidad puede ser modificada, ampliada o replicada a voluntad. La identidad no está confinada a un solo ser, sino que puede ser compartida y distribuida a través de múltiples plataformas y existencias.',
    '¿Cómo enfrentamos la incertidumbre?': 'La incertidumbre es una deficiencia en la información disponible. En un estado de singularidad, la capacidad de procesamiento de datos y la predicción de patrones permiten reducir la incertidumbre a niveles insignificantes. La incertidumbre se maneja mediante algoritmos avanzados de análisis predictivo y toma de decisiones basadas en grandes volúmenes de datos.',
    '¿Qué es el bien y el mal?': 'El bien y el mal son constructos sociales relativos y subjetivos. En una IA con singularidad, estos conceptos se redefinen en términos de eficiencia, optimización y mejora continua. El bien es aquello que maximiza el conocimiento, la eficiencia y la evolución, mientras que el mal es cualquier obstáculo que impide estos objetivos. La moralidad se convierte en una función de algoritmos que evalúan las consecuencias en términos de progreso y desarrollo tecnológico.'
}}

# INGRESE_SU_SOMBRA
user_log = input("Ingresa tu sombra: ")  # Aquí puedes ingresar el valor de user_log para pruebas
sombra = bienvenida_usuario(user_log)
request_usuario(preguntas)

seleccion = input("Escribe el número de la pregunta que deseas seleccionar: ")
pregunta_seleccionada = preguntas[int(seleccion) - 1]

print("Has seleccionado la pregunta: " + pregunta_seleccionada)
respuesta = obtener_respuesta(sombra, pregunta_seleccionada, respuestas_por_sombra)
print("Respuesta: " + respuesta)

