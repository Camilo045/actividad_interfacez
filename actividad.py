import flet as ft
import random

class JuegoAdivinaNumero:
    def __init__(self, page: ft.Page):
        #Configuración de la ventana
        self.page = page
        self.page.title = "Adivina el Número"

        self.page.bgcolor = "#1e1e2f"

        #Estado del juego (datos internos)
        self.numero_secreto = random.randint(1, 20)
        self.intentos = 0

         #Elementos visuales
        self.titulo = ft.Text("Adivina el número entre 1 y 20", size=20)
        self.entrada = ft.TextField(hint_text="Escribe tu numero", width=200)
        self.pista = ft.Text(value="Espera tu intento...")

        self.boton = ft.FilledButton(
            content=ft.Text("Probar número"), 
            on_click=self.comprobar_numero
        )

        # Colocamos los elementos en la ventana
        self.page.add(self.titulo, self.entrada, self.boton, self.pista)

    def comprobar_numero(self, e):
        if not self.entrada.value.strip():
            self.pista.value = "Por favor escribe un número primero."
            self.pista.color = "red"
            self.page.update()
            return

        numero_usuario = int(self.entrada.value)
        self.intentos += 1

        if numero_usuario < self.numero_secreto:
            self.pista.value = f"El número secreto es MAYOR. (Intento {self.intentos})"
            self.pista.color = "blue"
        elif numero_usuario > self.numero_secreto:
            self.pista.value = f"El número secreto es MENOR. (Intento {self.intentos})"
            self.pista.color = "orange"
        else:
            self.pista.value = f"¡Correcto! Acertaste en {self.intentos} intentos."
            self.pista.color = "green"
            self.entrada.disabled = True
            self.boton.content = ft.Text("Jugar de nuevo")
            self.boton.on_click = self.reiniciar_juego

        self.page.update()

    def reiniciar_juego(self, e):
        self.numero_secreto = random.randint(1, 20)
        self.intentos = 0

        self.entrada.value = ""
        self.entrada.disabled = False

        self.boton.content = ft.Text("Probar número")
        self.boton.on_click = self.comprobar_numero

        self.pista.value = "¡Nueva partida iniciada! Elige otro número."
        self.pista.color = "black"

        self.page.update()

def main(page: ft.Page):
    JuegoAdivinaNumero(page)

ft.run(main)