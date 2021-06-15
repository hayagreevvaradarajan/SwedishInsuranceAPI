# Swedish Insurance API

I have built a simple linear regression model as an API. The model takes the number of claims (independent variable) and predicts the total payment for all the claims in thousands of Swedish Kronor (dependant variable).
 
How to recreate the virtual environment?

The swedishInsuranceRegressor_venv.yaml contains the details of the virtual environment I used and the packages I had used. To recreate this environment on your machine, You'd need Anaconda installed.
After installing Anaconda and cloning this repository on your machine, type the following command: 
conda env create -f swedishInsuranceRegressor_venv.yaml

Dataset:

Swedish Insurance.csv is the dataset that I used to train the model after modifying the european decimal system (decimals places denoted after a comma) to the indian decimal system (decimal places denoted after a period).

Model:

swedish_insurance_Model.py contains the ML model that I had built based on the dataset that you can download from here:
https://www.math.muni.cz/~kolacek/docs/frvs/M7222/data/AutoInsurSweden.txt 
The model is saved as a pickle file which will then be imported into the Django Application for running the model as an API.

Running the API:

Recreate the virtual environment, activate the virtual environment using 'conda activate swedishInsuranceRegressor_venv' and then navigate into the api folder. The tree structure of the api folder will be as follows:
  |--api
  |--regressor
  |--manage.py

Run the manage.py file using the command 'python manage.py runserver'. This will activate your local web server at the URL http://127.0.0.1:8000/. 

If you don't want to recreate the exact virtual environment, then install the required packages from the requirements.txt file either using 'pip install -r requirements.txt' or using 'conda install --file requirements.txt'.

Testing the API:

Open your browser and type the URL 'http://127.0.0.1:8000/regressor?numberofclaims=xx' (replace xx in the URL with a number of your choice) or type the command curl -X GET http://127.0.0.1:8000/regressor?numberofclaims=xx ((replace xx in the URL with a number of your choice) in the command line.
This will return a JSON object. 

For example:
http://127.0.0.1:8000/regressor?numberofclaims=250 will return {"total_money": "873.5179465744159"}. Here, 873.5179465744159 is the predicted value for number of claims = 250.

Feel free to use this code in your projects as long as you give me credit , because let's face it. Leeching sucks. 

If you face any issues, feel free to open an issue and report it to me. 

If you have any queries, reach me at hayagreev.chintu1@gmail.com. 