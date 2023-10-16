# myapp/views.py
from django.shortcuts import render
from .models import DataPoint
import matplotlib.pyplot as plt
import io
import base64
from django.db import models
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend

def data_and_charts(request):
    data_points = DataPoint.objects.all()
    
    categorical_data = data_points.values_list('is_categorical' , flat=True)
    numerical_data = data_points.values_list('value', flat=True)

    print(categorical_data)
    print(numerical_data)
    
    pie_charts = {}
    if categorical_data:
        true_count = sum(categorical_data)
        false_count = len(categorical_data) - true_count
        print("true"  , true_count)
        fig, ax = plt.subplots()
        data = [true_count, false_count]
        labels = ['True', 'False']
        ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.set_title(f'Categorical')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        pie_charts["Category"] = base64.b64encode(img.getvalue()).decode()
        plt.close()

    histograms = {}
    if numerical_data:
        
        fig, ax = plt.subplots()
        ax.hist(numerical_data, bins=10)
        ax.set_title(f'Marks')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        histograms["Marks"] = base64.b64encode(img.getvalue()).decode()
        plt.close()

    return render(request, 'base.html', {'pie_charts': pie_charts, 'histograms': histograms ,'data_points':data_points,})

    # return render(request, 'base.html', {'pie_charts': pie_charts,})
