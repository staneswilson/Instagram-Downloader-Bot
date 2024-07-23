## Instagram Downloader Bot Script Documentation

### Introduction
This Python script utilizes the Instagrapi library to download Instagram content (photos and videos) within the Switch Chats and Communities platform. By leveraging an Instagram account's credentials, the script simplifies the process of saving desired content directly from the app.

### Prerequisites
* Python (version 3.6 or later)
* pip (Python package installer)
* Instagrapi library

### Installation
clone the github repository:

    git clone https://github.com/staneswilson/Instagram-Downloader-Bot
	cd Instagram-Downloader-Bot
install requirements:

    pip install -r requirements.txt

### Configuration
Rename the provided sample_config.env file to config.env.

Open the config.env file and replace the placeholder values with your actual Instagram and Switch Chats credentials:

**`INSTAGRAM_SESSION_ID`**: Provide the session from instagram login (optional)

**`INSTAGRAM_USERNAME`**:  Instagram login username

**`INSTAGRAM_PASSWORD`**: Instagram login password

**`BOT_TOKEN`**: Access Token from Switch

**`COMMUNITY_ID`**: Community id

**`COMMUNITY_URL`**: URL to the community

**`OWNER_ID`**: User id of the owner

**`FOLDER`**: Download location

### Start the bot
    bash start.sh  
or

    python3 -m bot

