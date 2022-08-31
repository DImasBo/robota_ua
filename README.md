# robota ua project

# Getting Started
1) need to run kafka, zookeeper and elasticsearch. `docker-compose up --build kafka zookeeper elasticsearch -d`
2) when the services will work then need to run other service: apiinser, apishow, consumer `docker-compose up --build apiinsert apishow consumer -d`

# Preview A general workflow 
Services:

### API Insert
success

![image](https://user-images.githubusercontent.com/52758126/187552948-84f0741f-a3b3-4c32-bf53-4a03a2dccbbe.png)

exception

![image](https://user-images.githubusercontent.com/52758126/187553093-08d8d07d-ac46-4d85-af96-436a535d4681.png)

### Kafka
![image](https://user-images.githubusercontent.com/52758126/187554656-b10b3e0b-941b-4c10-be2f-3d66b60ddeb2.png)

### Consumer
![image](https://user-images.githubusercontent.com/52758126/187553227-311df134-bdef-4887-a050-2673b777183f.png)

### elasticsearch
![image](https://user-images.githubusercontent.com/52758126/187554557-51725acf-d31b-4889-8f3e-d188d6014ee2.png)

### API Show
![image](https://user-images.githubusercontent.com/52758126/187554450-95aab58a-64f7-4cbd-b158-0e43ede029c8.png)



