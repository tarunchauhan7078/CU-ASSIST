# Email a random XKCD challenge

### Subscribe to XKCD comics and get comic emails every five minutes.

## Made with 
- HTML
- CSS
- PHP
- MySQL

## Platforms
- [Mailjet](https://www.mailjet.com)
- [Heroku](https://www.heroku.com)

## Description of XKCD comic mailer

- This is a PHP application that accepts a visitor’s email address and emails them a random XKCD comics.

- *connection.php*: is used to connect with the database.

- *index.php*: is used for entering the user details like username, email address and also helps to send email verification to the user.

- *sendmail.php*: is used to verify the user's email address.

- *cron.php*: is used to send the random emails from the https://c.xkcd.com/random/comic/ by using the cronjob functionality


- *images*: All the images used will be stored in this folder.

- *styles.css*: is used for giving the styles to the index.php.

## Getting Started
- Enter Email !
- Open mailbox and click on the verification link !
- Enjoy XKCD Comics at every 5 minutes in Inbox !

*LIVE DEMO* :  https://xkcdcomicsbykalyanjit.herokuapp.com
