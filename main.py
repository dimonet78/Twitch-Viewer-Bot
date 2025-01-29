import requests  # Importa la biblioteca requests para hacer solicitudes HTTP
import warnings  # Importa la biblioteca warnings para manejar advertencias
from selenium import webdriver  # Importa el módulo webdriver de Selenium para automatización del navegador
from selenium.webdriver.common.keys import Keys  # Importa Keys de Selenium para simular pulsaciones de teclas
from selenium.webdriver.common.by import By  # Importa By de Selenium para localizar elementos en el DOM
from colorama import Fore  # Importa Fore de la biblioteca colorama para colorear la salida en la terminal
from pystyle import Center, Colors, Colorate  # Importa módulos de pystyle para estilos de texto
import os  # Importa el módulo os para interactuar con el sistema operativo
import time  # Importa el módulo time para manejar tiempos y pausas

# Ignora las advertencias de deprecación
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Función para verificar actualizaciones del bot
def verificar_actualizaciones():
    try:
        # Realiza una solicitud GET para obtener la versión remota del bot
        r = requests.get("https://raw.githubusercontent.com/fluidmain/Twitch-Viewer-Bot/main/uptodate")
        remote_version = r.content.decode('utf-8').strip()  # Decodifica y limpia la versión remota
        local_version = open('uptodate.txt', 'r').read().strip()  # Lee y limpia la versión local
        if remote_version != local_version:  # Compara versiones
            print("Hay una versión actualizada del bot disponible. Puedes descargar la actualización aquí: https://github.com/fluidmain/Twitch-Viewer-Bot")
            time.sleep(3)  # Pausa de 3 segundos
            return False  # Retorna False si hay una actualización disponible
        return True  # Retorna True si no hay actualizaciones
    except:
        return True  # Retorna True en caso de cualquier excepción

# Función principal que verifica actualizaciones y muestra anuncios
def main():
    if not verificar_actualizaciones():  # Verifica actualizaciones
        return  # Si hay una actualización, sale de la función

# Función para imprimir anuncios
def imprimir_anuncio():
    try:
        # Solicita el contenido del anuncio desde Pastebin
        r = requests.get("https://pastebin.com/raw/1EwXmhbY", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()  # Decodifica y limpia el anuncio
        return announcement  # Retorna el anuncio
    except:
        print("Falló la verificación de la versión del bot. Inicia manualmente, pero puede que no funcione sin la última versión.\n")

# Función principal que verifica actualizaciones y muestra anuncios
def main():
    if not verificar_actualizaciones():  # Verifica actualizaciones
        return  # Si hay una actualización, sale de la función
    imprimir_anuncio()  # Imprime el anuncio

    # Configura el título de la ventana del sistema
    os.system(f"title fLUIDscripts. Twitch View Bot 3.1 ")

    # Imprime el banner del bot
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐ 
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐ 
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    announcement = imprimir_anuncio()  # Imprime el anuncio
    print("")
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colors.red, Center.XCenter("Gracias por usar nuestro bot."))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print("")

    # URLS de Proxy
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxy.network",
        3: "https://www.croxy.org",
        4: "https://www.youtubeunblocked.live",
        5: "https://www.croxyproxy.net",
    }

    # Seleccionando servidor proxy
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════[...]"))
    print(Colors.red, Center.XCenter("Si un servidor no es accesible, por favor avísame. Lo actualizaré."))
    print(Colors.red, Center.XCenter("Selecciona un servidor. Introduce el número del servidor y presiona Enter."))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    for i in range(1, 5):
        print(Colors.cyan, Center.XCenter(f"Servidor (online) {i}"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════[...]"))
    proxy_choice = int(input(Colorate.Vertical(Colors.cyan_to_blue, ">>")))
    proxy_url = proxy_servers.get(proxy_choice)  # Obtiene la URL del proxy seleccionado
    
    # Selecciona cuenta de Twitch
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════[...]"))
    print(Colors.cyan, Center.XCenter("¿Cuenta de Twitch objetivo? ¡Proporcione solo el nombre de usuario!"))
    print(Colors.cyan, Center.XCenter("Ejemplo: fluidscripts"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════[...]"))
    twitch_username = input(Colorate.Vertical(Colors.cyan_to_blue, ">>"))  # Obtiene el nombre de usuario de Twitch
    
    # Selecciona cantidad de proxys
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════[...]"))
    print(Colors.cyan, Center.XCenter("¿Cuántos espectadores deben ser enviados?"))
    print(Colors.cyan, Center.XCenter("(¡Números altos pueden causar errores!)"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════[...]"))
    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, ">>")))  # Obtiene la cantidad de proxies
    
    # Siguiente paso
    os.system("cls")  # Limpia la pantalla
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐ 
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐ 
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print('')
    print('')
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════[...]"))
    print(Colors.cyan, Center.XCenter("El bot empieza y envía espectadores."))
    print(Colors.cyan, Center.XCenter("Si no llegan todos los espectadores o no funciona,"))
    print(Colors.cyan, Center.XCenter("reinicia el bot o cambia el servidor proxy."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════[...]"))

    # Configura el navegador Chrome
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Ubicación del navegador Chrome
    driver_path = 'chromedriver.exe'  # Ubicación del ChromeDriver

    # Opciones para el navegador Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)  # Inicia el navegador con las opciones configuradas

    driver.get(proxy_url)  # Navega a la URL del proxy

    for i in range(proxy_count):  # Abre nuevas pestañas en el navegador para cada proxy
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        # Encuentra el cuadro de texto para la URL y escribe la URL de Twitch
        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    # Fin
    os.system("cls")  # Limpia la pantalla
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐ 
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐ 
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════[...]"))
    print(Colors.cyan, Center.XCenter("Los espectadores han llegado."))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter("Si el conteo de espectadores disminuye o el bot deja de funcionar,"))
    print(Colors.cyan, Center.XCenter("considera reiniciar el script o intentar con un servidor proxy diferente."))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter("Mantén la ventana abierta mientras desees usar el bot."))
    print(Colors.cyan, Center.XCenter("Cuando quieras salir del bot, presiona la tecla ENTER o cierra la ventana."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════[...]"))
    input(Colorate.Vertical(Colors.cyan_to_blue, ">>"))  # Espera a que el usuario presione ENTER para salir
    driver.quit()  # Cierra el navegador


if __name__ == '__main__':
    main()  # Ejecuta la función principal

# ==========================================
# Copyright 2023 - fLUIDscripts.
# ==========================================
