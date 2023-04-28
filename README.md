An example service using fastapi and chatgpt

## build and run

 - build the image

  $ sudo docker build -t chattybird .


 - run the container

  $ sudo docker run -p 8000:8000 chattybird


 - send a message 

$ curl --header "Content-Type: application/json"  --request POST   --data '{"message":"hi!"}'  http://localhost:8000/api/messages/

{"message":"hi!","id":2,"response":"Hello there! How are you doing today?"}
 
 - receive all conversation messages
  $ TODO
