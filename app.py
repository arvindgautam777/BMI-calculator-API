from flask import Flask, jsonify, request
import requests
from bmi import calculatingBMI
app = Flask(__name__)

class get:
    #This class will accept the input from the user and return the desired output
    @app.route('/', methods = ['GET', 'POST'])
    def js_data():
    	#accepts the json request
        data = request.get_json(force=True)

        #Creating the object and calling the class
        bmi_obj = calculatingBMI(data)
        res, overweight = bmi_obj.bmi_calculator()

        #Return the newly added columns and no of overweight
        return jsonify({"No of overweight":overweight, "Calculated_BMI":res})
  
if __name__=='__main__':
    app.run(debug = True)
