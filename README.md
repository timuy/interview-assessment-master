# How to Run Assessment

## Prerequiste

1. Install Docker

This is the version on my laptop:

![docker version](https://user-images.githubusercontent.com/77807039/136693628-7f84b1a4-d169-4574-bca8-7207997c3aac.png)


### Steps to Run Assessment

1. Clone public repo

github clone https://github.com/timuy/interview-assessment-master

2. Run docker

docker-compose up

NOTE:  If a build is needed, run the following:

docker-compose up --build 

3. In a separate DOS prompt access the running container

docker exec -it interview-assessment bash

4. Run the python script

python app.py

The program should be running like so:

![running assessment](https://user-images.githubusercontent.com/77807039/136693803-78202e60-c7dc-493e-a029-5ed3c61a2d0d.png)

#### Program Details

1. I extended the requirements to save the order details and I also created a very simple user table like so:

![eerd](https://user-images.githubusercontent.com/77807039/136693958-439988a2-2920-45b6-9f30-f466dea4e81a.png)

It made sense to save the order and assign to a user so it can be used for multiple users in the future.

I created the script to calculate the profit/loss based on each transaction rather than for the whole portfolio.  When I created the program, it would not buy any coins so I had to play around the script so it would trigger a buy.  

When I ran it the day later, I get this output:

![local](https://user-images.githubusercontent.com/77807039/136694132-e17f3d6d-51a7-46f7-83c8-6bbbe8bdcf16.png)

2. The script currently sleeps every hour.  I put the sleep interval in the .env file so it is configurable.  This is not the ideal way to run the script, but I did not have any scheduling app installed on my laptop (like crontab or autosys).
3. We can discuss more if there are any questions.
