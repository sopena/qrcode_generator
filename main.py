import qrcode
import flet as ft

def main(page: ft.Page):
    page.window.width = 450
    page.window.height = 800
    page.title = "Gerador de QR Code"
    def gerar_qrcode(dado, nome):
        code = qrcode.QRCode(
            version= 1,
            error_correction=qrcode.ERROR_CORRECT_L,
            box_size= 10,
            border= 4,
        )
        code.add_data(dado)
        code.make(fit=True)

        img = code.make_image(fill_color="black", back_color="white")
        img.save(rf"C:\Users\conta\Documents\GitHub\qrcode_generator\qrcodes\{nome}.png")

    def button_clicked(e):
        gerar_qrcode(link.value, nome.value)
        imagem = ft.Image(
            src=rf"C:\Users\conta\Documents\GitHub\qrcode_generator\qrcodes\{nome.value}.png",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )
        title = ft.Text(value=nome.value, size=15, weight=ft.FontWeight.BOLD, color="Black")
        container.content.controls.append(ft.Row(controls=[title], alignment=ft.MainAxisAlignment.CENTER))
        container.content.controls.append(ft.Row(controls=[imagem], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    titulo = ft.Text("Gerador de QR Code!", size=20, color="White", font_family="Arial", weight= ft.FontWeight.W_800)
    link = ft.TextField(label="Link", hint_text="Cole o link para transformar em QRCode: ", )
    nome = ft.TextField(label="Nome", hint_text="Nome para salvar o Arquivo: ")
    button = ft.ElevatedButton(text="Criar QRcode", on_click=button_clicked)

    container = ft.Container(
            width=450,
            height= 750,
            bgcolor=ft.colors.BLUE_ACCENT_100,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content= ft.Column(
                controls= [
                    ft.Row(
                        controls= [
                            titulo
                        ],
                        alignment= ft.MainAxisAlignment.CENTER,

                    ),
                    ft.Row(
                        controls = [
                            link
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls = [
                            nome
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls = [
                            button
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                    )
                ],
                scroll=ft.ScrollMode.ALWAYS
            )
        )
    
    page.add(container)

ft.app(main)


