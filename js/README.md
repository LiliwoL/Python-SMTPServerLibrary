# Librairie SMTP javascript

## Inclusion du script dans votre page HTML

À insérer juste avant la balise `</head>`.

> Pensez à adapter avec votre arborescence!

```html
<script src="http:://172.16.3.253:666/v1/"></script>
```

> Ce script est hébergé sur un serveur local. Pensez à adapter l'URL avec votre propre serveur.
> Vous pouvez également télécharger le fichier et l'inclure dans votre projet.

---

## Utilisation du script

Ajoutez le code suivant dans votre fichier javascript.
Ce code va utiliser les données issues de votre formulaire.

> Ce code ne fonctionnera que si le script précédent à été inséré!

```javascript
Email.send(
    {    
        "to" : "",        
        "reply-to" : "",
        "subject" : "",
        "body" : ""
    }
).then(
    message => console.log(message)
);
```

---

# Exemple d'utilisation

Le HTML pourrait ressembler à ceci:

```html
<form id="formulaireEnvoiMail">
    <input type="email" id="to" name="to" placeholder="Destinataire" required>
    <input type="email" id="reply-to" name="reply-to" placeholder="Répondre à" required>
    <input type="text" id="subject" name="subject" placeholder="Sujet" required>
    <textarea id="body" name="body" placeholder="Corps du message" required></textarea>
    <button type="submit">Envoyer</button>
</form>
```

Le javascript pourrait ressembler à ceci:

```javascript
document.getElementById('formulaireEnvoiMail').addEventListener('submit', function(e) {
    e.preventDefault();

    // Ajout d'un écouteur d'événement
    document.getElementById('formulaireEnvoiMail').addEventListener('submit', function(e) {
        // On évite le comportment par défaut d'un formulaire
        e.preventDefault();
        Email.send(
            {
                "to" : document.getElementById('to').value,
                "reply-to" : document.getElementById('reply-to').value,
                "subject" : document.getElementById('subject').value,
                "body" : document.getElementById('body').value
            }
        ).then(
            message => console.log(message)
        );
    });
});
```

---

# Sécurité

La librairie embarque une clé API pour l'envoi des mails.
Cette clé API est définie côté serveur.
