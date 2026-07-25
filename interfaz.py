import flet as ft
from flet import alignment, controls
from logica import generar_numero_secreto,evaluar_intento

def principal(pagina:ft.Page):
    pagina.title = "juego: numero secreto"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    numero_secreto = generar_numero_secreto()
    intentos = 3
    texto_pista = ft.Text(value="divina el número secreto entre 1 y 10! 🎲",size=20)
    texto_intentos = ft.Text(value=f"¡Numero de intentos!:{intentos}",size=19)
    cuadro_intento = ft.TextField(value="")
    def comprobar_numero(e):
        nonlocal intentos
        intento = int(cuadro_intento.value)
        intentos = intentos -1
        texto_intentos.value = f"¡Numero de intentos!:{intentos}"
        if intentos == 0:
            texto_pista.value = f"¡Perdiste! El número secreto era {numero_secreto}"
            boton_probar.disabled =True
            return
        resultado = evaluar_intento(intento,numero_secreto)

        if resultado == "Acierto":
            texto_pista.value = f"¡Felicidades, Matías! ¡Adivinaste! 🎉🏆"
            texto_pista.color = "green"
        elif resultado == "Bajo":
            texto_pista.value = f"¡Muy bajo! Intenta con un número más grande!"
            texto_pista.color = "blue"
        else:
            texto_pista.value = f"¡Muy alto! Intenta con un número más chico. 👇"
            texto_pista.color = "amber"
        pagina.update()
    
    boton_probar = ft.Button(
        content=ft.Text("Probar suerte",color="white"),
        on_click=comprobar_numero ,
        bgcolor= "blue"
    )
    fila_entrada = ft.Row(
        controls=[cuadro_intento,boton_probar],
        alignment=ft.MainAxisAlignment.CENTER
    )
    pagina.add(texto_pista, fila_entrada, texto_intentos)
