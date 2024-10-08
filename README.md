███████╗███╗   ███╗████████╗██████╗ ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ ██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
██╔════╝████╗ ████║╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
███████╗██╔████╔██║   ██║   ██████╔╝███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
╚════██║██║╚██╔╝██║   ██║   ██╔═══╝ ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
███████║██║ ╚═╝ ██║   ██║   ██║     ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

Un projet d'une librairie en JS pour faciliter l'envoi de mail depuis un formulaire HTML.

Il consiste en une librairie Js à insérer dans le code HTML et un script appelant un serveur SMTP en Python.

[toc]

v0.2

---

# Source

- https://github.com/mattwalshdev/emailee/tree/main

---

# Requis

- Un serveur SMTP fonctionnel et les informations à configurer dans le fichier **.env**
- Une machine avec Python3 installé pour le script serveur et fournir le script JS.

---

# FrontEnd

## Inclusion du script dans votre page HTML

Incluez le script juste avant la balise `</head>`.

> L'URL est celle du serveur hébergeant le script.
> Pensez à adapter avec votre propre serveur.

```html
<script src="http://172.16.0.100:666"></script>
```

---

## Utilisation du script

```javascript
Email.send(
    {
        "to" : "email@destinataire.fr",
        "reply-to" : "sender@seder.com",
        "subject" : "It's awesome!",
        "body" : "Some long text"
    }
).then(
    message => {
        alert("Envoyé avec succès");

        console.log(message)
    }
);
```

---

# Collection PostMan

Vous trouverez une collection PostMan pour tester le serveur SMTP dans le dossier **PostManCollection**.

Il faut modifier les **variables** de la collection et adapter à votre configuration.

---

# Backend

## Installation

```bash
pip install -r requirements.txt
```

---

## Configuration

Créer le fichier **.env** (en vous basant sur le fichier **.env.sample** fourni) avec vos valeurs.

---

```dotenv

## Utilisation

```bash
python3 smtp.py
```

---

# Exemple

Le dossier **sample** contient une application exemple pour tester la librairie et le serveur.