## Alexa Music Bot by Cute.. 

### Install required libs on fresh VPS.

```
apt update && apt install tzdata docker.io -y
```

### Clone repo on server
```
git clone https://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@github.com/Mrcutex1/dark2
```

### Edit .env to make changes in bot vars.

## Localhost deploy 
1. Clone repoo make sure git, ffmpeg, nodejs is installed. 
   ```
   apt install ffmpeg nodejs git zip unzip git -y
   ```
2. Install req and start bot:
```
cd  alexa-aio && pip3 install -r requierments.txt && chmod 777 * &&  bash start
```

## Deploy on Docker 
1. Clone repo and install docker and build image and run docker.
```
cd && git clone https://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@github.com/Mrcutex1/dark2 && cd dark2 && chmod 777 * && bash docker.sh 
```

If docker is already installed you can clone repo and build with a tag and run with below code make sure you are in cloned repo folder.
    
    docker build -t xxx . 
    docker run -d --restart=unless-stopped --name xxxx xxxx

### IF Bot is already deployed on server
To restart or redoply bot thay you have already edited/created.

```
docker container rm alexa -f && docker image rm alexa && cd && rm -R alexa && git clone https://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@github.com/Mrcutex1/dark2 && cd dark2 docker build -t alexa . &&  docker run -d --restart=unless-stopped --name alexa alexa
```

    
