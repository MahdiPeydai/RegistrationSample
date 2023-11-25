# RegistrationSample

You can create users with different email and phone number. Admin panel for managing users.

## Installation

First clone the repository :
```bash
git clone https://github.com/mahdipeydai/RegistrationSample.git
```
then go to project directory

```bash
cd path/to/project/directory/
```

after that create a database for project in MySQL.

Then create a .env file in project directory and set these configs in it:

- SECRET_KEY
- MYSQL_ROOT_PASSWORD
- MYSQL_DATABASE

For installing Webpack dependencies and bundling run :

```bash 
npm install
npm run build
```
After that for creating static files run :

```bash
python3 manage.py collectstatic
```

Then you need to do database migrations :(make sure MySQL is running on your machine)
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

For creating admin user run :
```bash
python3 manage.py creatersuperuser
```
It is ready. Enjoy
