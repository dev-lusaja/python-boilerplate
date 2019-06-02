from dotenv import load_dotenv, dotenv_values

# Load .env file
load_dotenv(override=True, verbose=True)

if dotenv_values():
    # Import rest interface
    from interface.rest.flask import Api
    # Start app
    app = Api().app
else:
    raise Exception('The env vars were not loaded, check the .env file')

if __name__ == '__main__':
    print('Command line not implemented')
