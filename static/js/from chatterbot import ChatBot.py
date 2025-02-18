from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Configuración del chatbot
chatbot = ChatBot("Asistente")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

# Función para interactuar con el chatbot
def chat():
    print("Chatbot activo. Escribe 'salir' para terminar.")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("Chatbot: Hasta luego!")
            break
        respuesta = chatbot.get_response(pregunta)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    chat()