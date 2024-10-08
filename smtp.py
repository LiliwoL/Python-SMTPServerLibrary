# ############################################
# Description: Serveur SMTP pour envoyer des emails
# ############################################


# ############################################
# Import des modules
from emailee import Emailee
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyfiglet

# ############################################

print(pyfiglet.figlet_format("SMTP Server") + "Version: 2.0.0")

# Chargement des variables d'environnement
envVars = dotenv.dotenv_values("./.env")
HOST = envVars['HOST']
PORT = envVars['PORT']
DEBUG = envVars['DEBUG']

print("Variables d'environnement:")
print(envVars)

__version__ = "2.0.0"

# ############################################
# Création de l'application Flask
app = Flask(__name__)
CORS(app)
app.logger.info('Flask app started')


# ############################################


# ############################################
# Définition des routes
@app.route('/v1/', methods=['POST'])
def send_email():
    # Lecture du JSON envoyé
    data = request.get_json()

    # Vérification des données
    if data['api_key'] != envVars['API_KEY']:
        output = jsonify({'status': 'error', 'message': 'Invalid API key'})
    else:
        # Envoi de l'email
        emailee = Emailee()

        serverOptions = {
            'smtpServer': envVars['SMTP_SERVER'],
            'port': int(envVars['SMTP_PORT']),
            'authUsername': envVars['SMTP_USER'],
            'authPassword': envVars['SMTP_PASSWORD']
        }


        # Only If SSL/TLS is required
        if envVars['SMTP_USE_SSL_OR_TLS'] == 'SSL' or envVars['SMTP_USE_SSL_OR_TLS'] == 'TLS':
            serverOptions['SSLTLS'] = envVars['SMTP_USE_SSL_OR_TLS']

        emailee.server(**serverOptions)

        emailee.sender(sender=envVars['SMTP_USER'], replyTo=data['reply-to'])

        emailee.sendTo(to=[data['to']])

        emailee.subject(subject=data['subject'])

        emailee.msgContent(msgText=data['body'])

        emailee.send()
        output = jsonify({'status': 'success'})

    return output

@app.route('/v1/', methods=['GET'])
def script():
    # Lecture du fichier SMTP.js
    file = open("js/smtp.min.js", "r")

    # Retourner le contenu du fichier
    return file.read()

# ############################################

# Lancement du serveur sur le port 666
app.run(host=HOST, port=PORT, debug=DEBUG)
