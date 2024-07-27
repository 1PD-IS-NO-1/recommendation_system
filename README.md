when you will run the recommendation_system.ipynb then you will get one extra file which name is similarity.pkl it is the most important file which will be use during the recommendation. so if you want to make recommendation system then first colne the repository after of that run the python code file and by using docker desktop make a docker image and then easily you can deploy it on cloud.  
first create style.css file inside a static name foler then run your code 
now if you done these two step now you can build docker image using this below command
docker build -t recommendation-system .
# here your docker image name is reommendation-system when your docker image is build (it will take time )

<h2>now you can give command docker login</h2>
docker push image_name:image_tag          note:- image_tag you can find by giving this command docker images 
after pushing the image into dockerhub then you easily can deploy your application on any cloud but the problem is that your image size is 1.38 so you have to pay for this much space on cloud
ok good by
# <h3>if you wnat to use docker hub image for deployment then you can use this command by this docker image will come in your system     docker pull priyanshudhaked/recommendation-system:latest </h3>
