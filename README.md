## How to Create Python Virtual Environment and install all dependencies in it
#### Linux
 1.  Having installed in Python *virtualenv:*
	 - Open command prompt and use: *pip install virtualenv*
2. Change directory to your local repository folder in the command prompt.
3. Create virtual environment: *virtualenv venv*
4. Activate virtual environment: *source venv/bin/activate*
5. Install dependencies:
	- Flask: *pip install flask*
	- Pyrebase4: *pip install pyrebase4*
	- Dotenv: *pip install -U python-dotenv*
	- Flask CORS: *pip install -U flask-cors*
### Windows
1.  Install Python in Windows
2.  Install Python *virtualenv:*
    - Open CMD and use *pip install virtualenv*
3.  Create virtual environment: *python -m venv c:\path\to\myenv*
4. Activate virtual environment: c:\path\to\myenv\activate.bat
5. Install dependencies:
    - Flask: *pip install flask*
	- Pyrebase4: *pip install pyrebase4*
	- Dotenv: *pip install -U python-dotenv*
	- Flask CORS: *pip install -U flask-cors*
   

## How to configure .env file with the Firebase config

1. Create new file called *env*
2. Edit file and write:
config = {"apiKey": "value","authDomain": "value","databaseURL": "value","projectId": "value","storageBucket": "value","messagingSenderId": "value","appId": "value","measurementId": "value"}
3. Change the *value* (not deleting " ") with the real configuration in Firebase page -> Configuration -> Firebase SDK snipett CDN.
4. DO NOT ENTER NEW LINES BETWEEN EACH PAIR (KEY: VALUE) JUST KEEP IT IN ONE LINE
4. Change file name from env to .env
5. .gitignore file would ignore this file to upload it, but do not try to add it to the commit...

## How to "Code" in the project
* Commits messages and code in English
* Code in snake_case NOT camelCase
* Use PEP-8 style guide for Python https://www.python.org/dev/peps/pep-0008/
    * Adding two empty lines before a function
    * Adding two empty lines before 'main'
    * Adding whitespace between # and text in comments
    * Removing redundant parentheses
    * Etc.

## Flask HTTP methods
https://pythonbasics.org/flask-http-methods/

## Flask RESTful API tutorial
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

## How to run Servers files
1. Navigate to *~/PruebaServiciosWeb2020Servidor* in terminal
2. Use *python src/app/[filename]* where *[filename]* can be *server.py*.
	```
	python src/app/server.py
	```
3. Open your browser an type *127.0.0.1/30006/<your-query>* without '>' and '<'
4. You can also use *curl* to test it (in terminal):
    - GET REQUEST:
        - $ curl -i http://127.0.0.1:30006/<your-query>
    - POST REQUEST:
        - $ curl -i -H "Content-Type: application/json" -X POST -d '{"key":"value of the json"}' http://127.0.0.1:30006/<your-query>
    - PUT REQUEST:
        - $ curl -i -H "Content-Type: application/json" -X PUT -d '{"key":"value of the json"}' http://127.0.0.1:30006/<your-query>
    - DELETE REQUEST:
        - $ curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:30006/<your-query>
