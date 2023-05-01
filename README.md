# Master_Thesis

## Reposetory Structure

´´´bash
.

├── _MCOSC

├── __pycache__

├── dataset

│ ├── data

│ ├── .DS_Sotre

│ └── labeled_ids.txt

├── insert_data

│ ├── __pycache

│ ├── Activity.py

│ └── DatabaseSetup.py

├── DbConnector.py

├── Queries.py

├── READMED.md

├── main.py

└── requirements.txt

´´´

## Run the queries

1. Clone the project

```bash
git clone 'HTTPS' or 'SSH'
```

2. Open the cloned folder in terminal

3. Create virtual environment
```bash
python3 -m venv venv
```

4. Activate virtual environment
```bash
source venv/bin/activate
```

5. Install packages with pip
```bash
pip install -r requirements.txt
```

6. Run the code
```bash
python3 main.py
```

## Here is all the information that are necessary in order to set up the databse in combination with docker for the private and public clouds.

1. Install docker

```bash
curl -sSL https://get.docker.com/ | sudo sh
```

2. Create a docker container with a MySql database. Change "mysql" with the container name and "root" with the root password.

```bash
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.26
```

If access denied to Docker daemon socket run the following codde:

```bash
sudo chmod 666 /var/run/docker.sock
```

3. Go the the docker bash. Write "docker ps" in the terminal to display the name.

```bash
docker exec -it [container_name] bash
```

4. Go into mysql

```bash
mysql -uroot -p
```

5. An password input is prompted. Write the password used in step 6.
6. Create an admin user with all right (Remember to use: ‘):

```bash
CREATE USER ‘YOUR_USERNAME_HERE’@’%’ IDENTIFIED BY ‘YOUR_PASSWORD_IN_PLAIN_TEXT_HERE’;
```

7. Give that user all rights:

```bash
GRANT ALL PRIVILEGES ON *.* TO ‘YOUR_USERNAME_HERE’@’%’ WITH GRANT OPTION;
```

8. Flush the privileges

```bash
FLUSH PRIVILEGES;
```

9. Check if the user is created:

```bash
SELECT User FROM mysql.user;
```

10.Create a database:

```bash
CREATE DATABASE Master_Thesis_DB;
```

11. Check if it is created:

```bash
SHOW DATABASES;
```

12. Write "exit" twice or open another terminal.
13. Restart the docker container:

```bash
docker restart [container id]
```
