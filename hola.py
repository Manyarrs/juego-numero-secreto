import flet as ft
import random

def principal(pagina:ft.Page):
    pagina.title = "juego:numero secreto - Matias"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    numero_secreto=random.randint(1,10)
    intentos=3
    texto_pistas = ft.Text(value="¡Adivina el número secreto entre 1 y 10! 🎲", size=20)
    texto_intentos = ft.Text(value=f"¡Numero de intentos!:{(intentos)}", size=19)
    cuadro_intento = ft.TextField(label="Introduce tu número aquí", width=250)
    def comprobar_numero(e):
        nonlocal intentos
        intento= int(cuadro_intento.value)
        intentos = intentos -1
        texto_intentos.value = f"¡Numero de intentos!:{(intentos)}"
        if intentos == 0:
            texto_intentos.value = f"¡Perdiste! ❌ El número secreto era {numero_secreto}"
            pagina.update()
            boton_probar.disabled=True
        if intento==numero_secreto:
            texto_pistas.value = "¡Felicidades, Matías! ¡Adivinaste! 🎉🏆"
            texto_intentos.color = "green"
        elif intento < numero_secreto:
            texto_pistas.value = "¡Muy bajo! Intenta con un número más grande!"
            texto_pistas.color="blue"
        else:
            texto_pistas.value = "¡Muy alto! Intenta con un número más chico. 👆"
            texto_pistas.color = "amber"
        pagina.update()
    boton_probar = ft.Button(
        content=ft.Text("Probar suerte"),color="withe", 
        on_click=comprobar_numero,
        bgcolor="blue"
        )
    fila_entrada = ft.Row(
        controls=[cuadro_intento,boton_probar],
        alignment=ft.MainAxisAlignment.CENTER
        )
    pagina.controls.append(texto_pistas)
    pagina.controls.append(fila_entrada)
    pagina.controls.append(texto_intentos)
    pagina.update()
ft.app(target=principal)