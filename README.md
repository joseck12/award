# [AWARDS SITE]
###### By **[Joseck Ogachi]**
## Description
An application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

## Setup/Installation

- Install python version3.6
- On your terminal run `pip install django==1.11.5`to nstall Django
- Install and activate virtual env
- On GitHub, navigate to the main page of the repository.
- Click Clone or download to copy the link.
- On your terminal type git clone, and then paste the URL you copied in the above step.
- git clone` https://github.com/joseck12/award`
`Press Enter`.

## Creating a database
- `psql`
- `CREATE DATABASE reward`
- Connect to the database `\c reward`
- Check if tables have been created `\dt`

## Run migrations
- `python3.6 manage.py migrate`
- `python3.6 manage.py makemigrations reward`

## Running the app
- `python3.6 manage.py runserver`
- `password to admin(qwerty1234)`

## Testing
- `python3.6 manage.py test reward`
