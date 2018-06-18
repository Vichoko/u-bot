# all templates have 1 format argument
import random

FREE_GAME_TITLE_TEMPLATE_PLAT_GAME = [
    "juego gratis: [{}] {}",
    "gratis en {} el {}",
    "en {} free por tiempo limitado {}",
    "[{}] {} gratis por un tiempo",

]
FREE_GAME_TITLE_GAME = [
    "gratis {}",
    "{} gratis",
    "[gratis] {}",
]

FREE_GAME_TITLE_GAME_PLAT = [
    "{} gratis en {}",
    "[GRATIS] {} - {}"

]


def fill_free_game_title_template(dic):
    rand = random.uniform(0, 1)
    if rand < 0.3333:
        return random.choice(FREE_GAME_TITLE_GAME).format(dic["title"])

    elif rand < 0.66666:
        return random.choice(FREE_GAME_TITLE_GAME_PLAT).format(dic["title"], dic["platform"])
    else:
        return random.choice(FREE_GAME_TITLE_TEMPLATE_PLAT_GAME).format(dic["platform"], dic["title"])


FREE_GAME_MSG_TEMPLATE = [
    """
    {} no lo cacho pero esta gratis por un tiempo.\n
    saludos
    """,

    """
    cumpliendo con mi deber civico {}\n
    saludos
    """,

    """
    buenas, \n
    {} está gratis. A alguien le interesara.\n
    """,

    """
    it's free {}
    """,

    """
    {}
    """,

    """
    {}\n
    provecho
    """,

    """
    link {}
    """,

    """
    Ni idea que tal el juego , pero cumplo con el deber :)\n
    {}
    """,

    """
    Sin más preambulo: \n
    {}
    """,

    """
    link: {}\n
    creo que por tiempo limitado 
    """,

    """
    por si alguien le interesa {}
    """,
]
