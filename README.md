
## Table of Contents

* [Demo](#demo)
* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Browser Support](#browser-support)
* [Resources](#resources)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing](#licensing)
* [Useful Links](#useful-links)

<br />

## Demo

> To authenticate use the default credentials ***test / ApS12_ZZs8*** or create a new user on the **registration page**.

- **Argon Dashboard Django** [Login Page](https://www.creative-tim.com/live/argon-dashboard-django)
- **[Django Argon Charts](https://github.com/app-generator/django-argon-charts)** - sample projects that showcase real information in charts 

<br />

## Quick start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/argon-dashboard-django.git
$ cd argon-dashboard-django
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />



## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br /> 

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/creativetimofficial/argon-dashboard-django.git
$ cd argon-dashboard-django
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />



## Resources

- Demo: <https://www.creative-tim.com/live/argon-dashboard-django>
- Download Page: <https://www.creative-tim.com/product/argon-dashboard-django>
- Documentation: <https://demos.creative-tim.com/argon-dashboard-django/docs/1.0/getting-started/getting-started-django.html>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/argon-dashboard-django/issues)

<br />