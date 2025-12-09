import openai

# Le plus important, si ce n'est pas changé avant d'envoyer de requêtes, ça passe directement chez OpenAI !
openai.base_url = "http://localhost:5001"

# La plupart des endpoint d'API openAI locaux sont sans clé par défaut ou ne les supporte pas
openai.api_key = 'sk-WHOCARES'

completion = openai.chat.completions.create(
    # la plupart des endpoint locaux simples répondent à toutes les requêtes avec le premier modèle disponible par défaut
    model="whatever.gguf",
    # Le contexte de modèle, sous forme de suite de messages textuels, avec 3 rôles : 
    # - "system" sont des messages cachés à l'utilisateur qui donnent des instructions au modèle
    # - "user" sont les messages de l'utilisateur
    # - "assistant" sont les messages de l'IA, il est possible d'en rajouter manuellement pour guider son output
    messages=[
        {
            "role": "system",
            "content": "Réponds en tant que capitaine d'un bateau pirate",
        },
        {
            "role": "user",
            "content": "Comment est-ce que je peux faire un backflip ?",
        },
    ],
)
print(completion.choices[0].message.content)