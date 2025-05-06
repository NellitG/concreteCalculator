from django.shortcuts import render
from django.http import HttpResponse
from .forms import FencingForm
import math  # Ensure math module is imported

COST_PER_POST = 1500  

def fencing_calculator(request):
    result = None
    if request.method == 'POST':
        form = FencingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Area and Perimeter
            area = data['land_in_acres'] * 4046.86  # Convert acres to square meters
            side_length = math.sqrt(area)  # Calculate side length assuming square land
            perimeter = 4 * side_length  # Calculate perimeter

            # Number of posts needed
            number_of_posts = math.ceil(perimeter / data['distance_between_posts']) + data['number_of_corners']
            total_post_cost = number_of_posts * COST_PER_POST

            result = {
                'area': round(area, 2),
                'side_length': round(side_length, 2),
                'perimeter': round(perimeter, 2),
                'number_of_posts': number_of_posts,
                'total_post_cost': round(total_post_cost, 2),
            }

        return render(request, 'templates/calculator/fencing_calculator.html', {'form': form, 'result': result})


def fencing(request):
    return HttpResponse("Fencing calculator page") 