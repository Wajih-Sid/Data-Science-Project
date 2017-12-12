# Data-Science-Project
Data Science Project 

- https://www.kaggle.com/ludobenistant/hr-analytics-1/data

- https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/data



## API

The APIs for this project are located in the folder apiserver/HRProject.py

The API server runs on Flask with the url:
<pre><code>"http://mohsinaslam.pythonanywhere.com/predict"</code></pre>

- Run a POST request from any REST client to test.


## Angular Website

The website is built on Angular 1.5 and requires node, npm dependancies

- Goto directory website
- Run `npm start`
- Should give the following response:
    <pre><code>
        > angular-seed@0.0.0 start /home/wajih/PycharmProjects/Data-Science-Project/apiserver/website
        > http-server -a localhost -p 8080 -c-1 ./app
         Starting up http-server, serving ./app
         Available on: http://localhost:8080
         Hit CTRL-C to stop the server
    </code></pre>
    
 ## Testing the App
 
 - Goto URL `http://localhost:8080/?#!/employee_churn`
 - Fill Form Data and hit Submit
 - On submit the endpoint `get_churn` is hit.
