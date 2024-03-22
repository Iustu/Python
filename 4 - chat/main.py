#titulo
 #Botão
  #Pop up
   #TItulo
   #Campo
   #Botao
#Chat
 #Mensagem
 #Enviar

import flet as ft

def main(pagina):
   titulo = ft.Text("Hashzap")

   #chat - lista mostrada em pé
   chat = ft.Column()

   #enviar para todo mundo num túnel
   def enviar_mensagem_tunel(mensagem):
      texto_mensagem = ft.Text(mensagem)
      chat.controls.append(texto_mensagem)
      pagina.update()

   pagina.pubsub.subscribe(enviar_mensagem_tunel)

   #manipula mensagens no chat com o botão
   def enviar_mensagem(evento):
      pagina.pubsub.send_all(f"{nome_usuario.value}:{campo_mensagem.value}")
      #texto_mensagem = ft.Text(f"{campo_mensagem.value}")
      #chat.controls.append(texto_mensagem)
      campo_mensagem.value = ""
      pagina.update()

   campo_mensagem = ft.TextField("Digite sua mensagem")
   botao_enviar = ft.ElevatedButton("Enviar mensagem",on_click=enviar_mensagem)
   linha_enviar = ft.Row([campo_mensagem,botao_enviar])
   #entrar no chat
   def entrar_chat(evento):
      popup.open=False
      pagina.remove(botao_iniciar)
      pagina.remove(titulo)
      pagina.add(chat)
      pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
      #texto_entrada = ft.Text(f"{nome_usuario.value} entrou no chat")
      #chat.controls.append(texto_entrada)
      pagina.add(linha_enviar)

      pagina.update()
   
   #inicio
   titulo_popup = ft.Text("Bem vindo ao BemsomZap")
   nome_usuario = ft.TextField(label="Escreve o seu nome de chat")
   botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

   #colocar nome
   popup  = ft.AlertDialog(
      open=False,
      modal=True,
      title=titulo_popup,
      content=nome_usuario,
      actions=[botao_entrar],
   )

   #inicio mesmo
   def abrir_popup(evento):
      pagina.dialog = popup
      popup.open = True
      pagina.update()
   
   botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

   pagina.add(titulo)
   pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)