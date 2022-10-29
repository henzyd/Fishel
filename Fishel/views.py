import csv
import sys
import csv
from django.shortcuts import render

# def data(reqe)




# Create your views here.
def generating_questions(request):
    file_folder = 'physics'
    file_subfolder = 'higher'
    file_name = 'physics_highers'
    user_data_num = 30

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
    
    with open(f'Fishel/{file_folder}/{file_subfolder}/{file_name}.csv') as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        print(type(reader_obj))
        for row in reader_obj:
            # row[-1]
            # print(row)
            # def recursion(data)
            # while len(x) < user_data_num :
            #     x.append(row[-1])
            if len(x) > user_data_num:
                break
            else:
                x.append(row[-1])
    # return redirect('home_page') 
    # print(x)
    context = {
        'data_s': x
    }
    return render(request, 'Fishel/generate.html', context)


def home(request):
    return render(request, 'Fishel/home.html')

def generate_question_view(request):
    return render(request, 'Fishel/generate.html')
