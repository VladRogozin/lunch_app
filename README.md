## System startup

### Local startup

1. Install the required libraries using the command:

   ```shell
   pip install -r requirements.txt
   
2. Go to the main project directory.

3. Start the development server with the command:
   (You can also choose any other port to start the server.)

   ```shell
   python manage.py runserver 14321

##Starting in Docker containers
1. Make sure you have Docker installed and running on your computer.

2. Navigate to the directory containing the docker-compose.yml file.

3. Run the system in Docker containers using the command:
   ```shell
   docker compose up --build
If you have the plugin version of DComps, use the
    ```shell
   command docker-compose up-build.
