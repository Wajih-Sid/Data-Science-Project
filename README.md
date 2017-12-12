# Data-Science-Project
Data Science Project 

- https://www.kaggle.com/ludobenistant/hr-analytics-1/data

- https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/data



## API

The APIs for this project are located in the folder apiserver/HRProject.py

- Goto directory apiserver
- Run ```python manage.py runserver```
  - Should give the below response:
      <pre><code>Django version 1.11.8, using settings 'apiserver.settings'
       Starting development server at http://127.0.0.1:8000/
       Quit the server with CONTROL-C.</code></pre>

- All Set!


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
