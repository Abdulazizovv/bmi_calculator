from django.shortcuts import render, redirect

def calculate_bmi(height, weight):
    height_meters = height / 100
    weight_kg = weight
    bmi = weight_kg / (height_meters * height_meters)
    return round(bmi, 2)


def index(request):
    bmi = request.session.get('bmi')

    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        calculated_bmi = calculate_bmi(height=height, weight=weight)
        
        request.session['bmi'] = calculated_bmi
        bmi = calculated_bmi
        return redirect('index')

    return render(request, 'index.html', {'bmi': bmi})