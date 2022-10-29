import csv
import sys
import csv
from django.shortcuts import render


# Create your views here.
def generating_questions(request):
    maxInt = sys.maxsize
    while True:
        # decrease the maxInt value by factor 10 
        # as long as the OverflowError occurs.

        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)   
    x = []
    num = 0
    with open('Fishel/Test/physics_highers.csv') as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        print(type(reader_obj))
        for row in reader_obj:
            # row[-1]
            # print(row)
            # def 
            while num > 0:

                x.append(row[-1])
    # return redirect('home_page') 
    context = {
        'data_s': x
    }
    return render(request, 'Fishel/generate.html', context)


def home(request):
    return render(request, 'Fishel/home.html')