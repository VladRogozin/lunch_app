## A brief comment about the project
The project is divided into 3 applications that interact with each other:
1. lunch_api - is the app that contains restaurant information, menus, and menu voting, small tests.

2. lunch_app - is the main application that contains the project settings and configuration.

3. users - is the app, which is responsible for registration, authorization, and employee information. It also includes small tests.

4. vote_api - is the application that displays the results of votes and also contains.
5. 
I also marked large functions with comments in Ukrainian for better understanding

Each application performs a different role and provides interaction between the components of the system. This modular structure makes it easy to develop, maintain, and extend the project.


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

3. If you have the plugin version of DComps, use the command:
   ```shell
   docker compose up --build
4. Else run the system in Docker containers using the command:

    ```shell
   docker-compose up-build.
