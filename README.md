## Instagram Downloader Bot Script Documentation

This Python script utilizes the Instagrapi library to download Instagram content (photos and videos) within the Switch Chats and Communities platform. By leveraging an Instagram account's credentials, the script simplifies saving desired content directly from the app.

## Features

Downloads Instagram content including:
- Photo
- Igtv
- Reel
- Story

# How to deploy?

## Prerequisites

### 1. Installing requirements

- clone this repo:

```
git clone https://github.com/staneswilson/Instagram-Downloader-Bot/ && cd Instagram-Downloader-Bot
```

- For Debian based distros

```
sudo apt install python3 python3-pip
```

Install Docker by following the [official Docker docs](https://docs.docker.com/engine/install/debian/)

- For Arch and its derivatives:

```
sudo pacman -S docker python
```

- Install dependencies for running setup scripts:

```
pip install -r requirements.txt
```

------

### 2. Setting up the config file

_Rename the provided sample_config.env file to config.env._

```
cp config_sample.env config.env
```

Fill up the rest of the fields. The meaning of each field is discussed below.

- `INSTAGRAM_SESSION_ID`: Provide the session from Instagram login (optional)
- `INSTAGRAM_USERNAME`:  Instagram login username
- `INSTAGRAM_PASSWORD`: Instagram login password
- `BOT_TOKEN`: Access Token from Switch
- `COMMUNITY_ID`: Community id
- `COMMUNITY_URL`: URL to the community
- `OWNER_ID`: User id of the owner
- `FOLDER`: Download location

------

### 3. Build And Run the Docker Image

Ensure you still mount the app folder and install the docker from official documentation.

- There are two methods to build and run the docker:
    1. Using official docker commands.
    2. Using docker-compose. (Recommended)

------

#### Build And Run The Docker Image Using docker-compose

**NOTE**: If you want to use ports other than 80 and 8080 for deploying in Switch servers serve respectively,
change it in [docker-compose.yml](https://github.com/staneswilson/Instagram-Downloader-Bot/blob/main/docker-compose.yml)
also.

- Install docker compose plugin

```
sudo apt install docker-compose-plugin
```

- Build and run Docker image or to view current running image:

```
sudo docker compose up
```

- After editing files with nano for example (nano start.sh) or git pull:

```
sudo docker compose up --build
```

- To stop the running image:

```
sudo docker compose stop
```

- To run the image:

```
sudo docker compose start
```

- To get log from already running image (after mounting the folder):

```
sudo docker compose logs --follow
```

------

## Note: 
- You must log in even if you want to download public posts. After your first attempt, you must confirm that you logged in from a different IP address (you can confirm this using the phone app).
- Private posts, stories, reels, igtv cannot be downloaded unless the logged account is followed and accepted by the user.
