from django.shortcuts import render
from django.http import HttpResponse

from predict_pipeline import CustomData,PredictPipline

# Create your views here.

def home(request):
    if request.method=='GET':
        return render(request,'home.html')
    
    else:
        data=CustomData(
        gender=request.POST['gender'],
        age=request.POST['age'],
        hypertension=request.POST['hypertension'],
        heart_disease=request.POST['heart_disease'],
        smoking_history=request.POST['smoking_history'],
        bmi=request.POST['bmi'],
        HbA1c_level=request.POST['HbA1c_level'],
        blood_glucose_level=request.POST['blood_glucose_level'],
        
        )
        
        pred_df=data.get_data_as_data_frame()
        

        predict_pipline=PredictPipline()
    
        result=predict_pipline.predict(pred_df)

        return render(request,'home.html',{'result':int(result[0])})
