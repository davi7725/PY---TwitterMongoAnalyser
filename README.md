# PY-TwitterMongoAnalyser

## Features

- Read twitter data from a CSV file
- Insert data into MongoDB instance
- Read data from MongoDB and do some sort of analytical work
## Requirements

* Docker ✅
* Python3 ✅
* pymongo for Python3 ✅

## How to run
If you **don't** have **python3** on your system, make sure your docker is running and then execute the following command:
`docker run -it --rm davi7816/pybuntu`.

This will give you a running instance of ubuntu with all the necessary applications installed (python, git, nano, wget and unzip).

If you **do** have **Python3** on your system make sure you have the pymongo installed by executing: `python3 -m pip install pymongo`

After obeying the pre-requirements, let's jump to how to get the project up and running.



On your local machine let's run the following command to get an instance of the MongoDB running (if you don't have currently):

`docker run --rm -v $(pwd):/data/db --publish=27017:27017 --name dbms -d mongo:latest`

This command will spin-up a new instance of mongodb and then create a link from your current folder (**$(pwd)** - which can be changed), to store all the data that will be sent to mongo.
	
  **NB! If you have *Windows*, replace **$(pwd)** with the path to a directory where you want to store the data**

With the local machine running an instance of Mongo, lets now get its local ip address by typing `ifconfing` on Linux/Mac or using `ipconfig` on Windows, all of these should be executed within a terminal.
Let's keep this IP asside since we will be needing it further on on the process.


Now let's clone the repository to the machine where Python is installed (either the docker ubuntu instance or the local machine) by using the following command:
`git clone https://github.com/davi7725/PY---TwitterMongoAnalyser.git`

We also need to download the csv files to a directory of our choice that will have to, once again, remember later on. To do this simply download the zip file with:
`wget http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip` followed by `unzip trainingandtestdata.zip`. **Once again keep notice of the full file path**.


After this we have to go into the repository folder and with nano (or your favourite text editor) edit **"URL_TO_MONGODB"** and **NAME_OF_CSV_FILE** with **"mongodb://[LocalIPAddress]:27017/"** and **"[LocationOfTheCSVFile]"**.
These would for example result in "mongodb://192.168.0.6:27017/" and "/tmp/testdata.csv"

With all of these set up, it is time to run the actual program and for that we need to make sure we are in the folder that contains the python file from this repository (twitterScrape.py) and execute the following command:
`python3 twitterScrape.py`
