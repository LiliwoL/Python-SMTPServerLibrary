# SMTPServerLibrary

Source:
https://github.com/mattwalshdev/emailee/tree/main

## FrontEnd

### Inclusion du script dans votre page HTML

```html
<script src="http://172.16.3.253/SMTPServerLibrar/js/smtp.js"></script>
```
### Utilisation du script

```javascript
Email.send({
    Host : "smtp.elasticemail.com",
    Username : "username",
    Password : "password",
    To : 'them@website.com',
    From : "you@isp.com",
    Subject : "This is the subject",
    Body : "And this is the body"
}).then(
    message => alert(message)
);
```