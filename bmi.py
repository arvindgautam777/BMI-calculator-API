class calculatingBMI:
    def __init__(self, data):
        self.data = data
        #self.bmi_calculator()
    
    def bmi_calculator(self):
        import pandas as pd
        import json
        df = pd.DataFrame(self.data)
        df['BMI'] = df['WeightKg']/((df['HeightCm']/100)**2)
        df['BMI_Category'] = ''
        df['Health_Risk'] = ''
        df.loc[(df.BMI <= 18.5), ['BMI_Category','Health_Risk']] = ['Underweight', 'Malnutrition risk']
        df.loc[(df.BMI > 18.5) & (df.BMI < 24.9), ['BMI_Category','Health_Risk']] = ['Normal Weight', 'Low risk']
        df.loc[(df.BMI > 25) & (df.BMI < 29.9), ['BMI_Category','Health_Risk']] = ['Over Weight', 'Enhanced risk']
        df.loc[(df.BMI > 30) & (df.BMI < 34.9), ['BMI_Category','Health_Risk']] = ['Moderately obese', 'Medium risk']
        df.loc[(df.BMI > 35) & (df.BMI < 39.9), ['BMI_Category','Health_Risk']] = ['Severely obese', 'High risk']
        df.loc[(df.BMI >= 40 ), ['BMI_Category','Health_Risk']] = ['Very severely obese', 'Very high risk']
        overweight = df[df.BMI_Category == 'Over Weight'].shape[0]
        res = json.loads(df.to_json(orient='records'))
        return res, overweight