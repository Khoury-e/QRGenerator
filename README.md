## QRGenerator
QR generator is a multi-threading client/server networking application consisting of a client which provides a URL and server providing a QR code generated for that URL.


__Note:__ Python 3.x and pip must be installed prior to running this application. For more information on installing python please visit the python documentation: https://docs.python.org/3/ 

## Run Locally

Clone the project

```bash
  git clone https://github.com/Khoury-e/QRGenerator.git
```

Go to the project directory

```bash
  cd QRGenerator
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start server.py

```bash
  python server.py
```

Start the client

```bash
  python client.py
```

__Note:__ It is important to start **Server.py** before **Client.py**

After inputing a URL, check the directory for a picture (QR.png):

__For Windows__

```bash
  dir
```
__For Mac & Linux__
```bash
  ls
```

## Change User Credentials
The application is built with predefined users. Authenticated users can only get access to the application service. Hence, if you want to:\
    - change the users' credentials  
    - add users  
    - delete users

Go to **Users.json**. For example:
```code
  [
    {
        "username":"testUsername",
        "password":"ReallyStrongPassword1234"
    }
  ]  
```

