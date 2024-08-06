### Promotional Task 7

The following is the steps I took in detail, to create a simple python app, containerize it and deploy it to a kubernetes cluster.

[Docker Image URL](https://hub.docker.com/repository/docker/actokuyt/kodecamp-devops-bootcamp-app/general)

## Step 1 (create a simple web app)
I created a new python file "app.py", with the following content.

```
# app.py

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('MESSAGE', 'Hello, Welcome to KodeCamp DevOps Bootcamp!')
    password = os.getenv('PASSWORD', 'default_password')
    return f"{message} - Password: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

Running this python file starts a local server as shown in the image below.

![app.py run](./images/Screenshot%202024-08-05%20at%2010.08.21%20PM.png)

## Step 2 (Dockerize the App)
I created a docker file in the project directory with the following content

```
# Dockerfile

FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python3", "app.py"]

```

After this I ran `$docker build -t kodecamp-devops-bootcamp-app .
` to build the docker image, and `$docker run -p 5000:5000 kodecamp-devops-bootcamp-app` to run the image.

![docker build](./images/Screenshot%202024-08-05%20at%2010.39.15%20PM.png)

I also tagged and pushed the image to docker hub using the commands `$docker tag kodecamp-devops-bootcamp-app actokuyt/kodecamp-devops-bookcamp-app:latest` and `$docker push actokuyt/kodecamp-devops-bookcamp-app:latest`

![tag and push](./images/Screenshot%202024-08-06%20at%205.40.09%20AM.png)

## Step 3 (Deploy the App to a Kubernetes Cluster)
 I have created four yaml config files with the following contents.

 ```
# deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: kodecamp-devops-bootcamp-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: kodecamp-devops-bootcamp-app
  template:
    metadata:
      labels:
        app: kodecamp-devops-bootcamp-app
    spec:
      containers:
      - name: kodecamp-devops-bootcamp-app
        image: actokuyt/kodecamp-devops-bootcamp-app:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        env:
        - name: MESSAGE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: MESSAGE
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: PASSWORD
 ```

 ```
# service.yaml

apiVersion: v1
kind: Service
metadata:
  name: kodecamp-devops-bootcamp-service
spec:
  selector:
    app: kodecamp-devops-bootcamp-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: ClusterIP
 ```

 ```
# configmap.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  MESSAGE: "Hello, Kubernetes!"
 ```

 ```
 # secret.yaml

apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  PASSWORD: "eW91ci1wYXNzd29yZA=="
 ```

I also started minikube with the command `$minikube start`.

![minikube start](./images/Screenshot%202024-08-06%20at%206.23.18%20AM.png)

and applied all the config files created earlier

![config files applied](./images/Screenshot%202024-08-06%20at%206.34.54%20AM.png)

## Step 4 (Test the Deployment)

I forwarded the service to a localhost port and accessed it through a browser.

![testing testing](./images/Screenshot%202024-08-06%20at%206.55.10%20AM.png)