from time import sleep

from splinter import Browser
import private_credentials
from settings import *


def post_message(create_msg_url, category, title, message, send):
    # config
    browser = Browser('chrome')
    # new message syntax is: https://www.u-cursos.cl/<institution>/<year>/<semester>/<community>/<section>/foro/mensaje
    browser.visit(create_msg_url)

    # log in
    browser.fill(USERNAME_FIELD_NAME, private_credentials.username)
    browser.fill(PASSWORD_FIELD_NAME, private_credentials.password)
    browser.find_by_value(LOG_IN_BUTTON_VALUE).click()

    # build up message
    # choose category
    browser.find_by_id(CATEGORY_CHOSER_ID).first.click()
    browser.find_by_css(CATEGORY_CHOSER_TEXT_INPUT_CSS_CLASS).first.fill("{}\n".format(category))

    # write title
    browser.find_by_name(TITLE_FIELD_NAME).fill(title)

    # write message
    browser.find_by_name(MESSAGE_INPUT_NAME).fill(message)

    # send message (CAUTION)
    if send:
        browser.find_by_value(SEND_BUTTON_VALUE).click()


def main():
    mode = input("""Menu:
        [0] Pre-visualizar Prueba. Se visualiza log-in y escritura de mensaje sin enviar el mensaje al final.
        [1] Enviar mensaje a COMGAMER. Se le consultará categoria, titulo y mensaje. Se envía el mensaje al final.
        [2] Activar bot de publicacion de juegos gratis.
        
    Ingrese opcion: """)
    if mode is "0":
        print("Pre-visualizar Prueba")
        DROPDOWN_CATEGORY_OPTION = "Utilidad Pública"
        TITLE = "Titulo de prueba"
        MESSAGE = """ Buenos dias:
        
    
        Saludos cordiales 
        """
        URL = "https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/foro/mensaje"
        post_message(URL, DROPDOWN_CATEGORY_OPTION, TITLE,MESSAGE, False)
    elif mode is "1":
        print("Enviar mensaje a COMGAMER")
        DROPDOWN_CATEGORY_OPTION = input("Ingrese categoria del mensaje: ")
        TITLE = input("Ingrese titulo del mensaje: ")
        MESSAGE = input("Ingrese contenido del mensaje (<br> para saltos de linea): ")
        MESSAGE = MESSAGE.replace("\\n", "\n")
        URL = "https://www.u-cursos.cl/uchile/2010/0/COMGAMER/1/foro/mensaje"
        post_message(URL, DROPDOWN_CATEGORY_OPTION, TITLE, MESSAGE, False)
    elif mode is "2":
        print("not implemented")
    else:
        print("Invalid entry")
        main()
    print("Gracias por usar u-bot")
    sleep(5)


if __name__ == "__main__":
    main()


"""
Ingrese categoria del mensaje: Utilidad Pública
Ingrese titulo del mensaje: Layers of Fear Steam Gratis
Ingrese contenido del mensaje: https://store.steampowered.com/app/391720/Layers_of_Fear/ \n asd \n\n\n asdads
"""