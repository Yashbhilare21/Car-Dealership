from django.shortcuts import render
from .models import Car
def home(request):
    cars = Car.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})


from django.shortcuts import render
from django.db.models import Q
from .models import Car

def car_list(request):
    cars = Car.objects.all()

    # Filters
    make = request.GET.get('make')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    sort = request.GET.get('sort')

    if make and make != 'all':
        cars = cars.filter(make__iexact=make)

    if year_min:
        cars = cars.filter(year__gte=year_min)
    if year_max:
        cars = cars.filter(year__lte=year_max)

    if price_min:
        cars = cars.filter(price__gte=price_min)
    if price_max:
        cars = cars.filter(price__lte=price_max)

    # Sorting
    if sort == 'price_asc':
        cars = cars.order_by('price')
    elif sort == 'price_desc':
        cars = cars.order_by('-price')
    elif sort == 'year_asc':
        cars = cars.order_by('year')
    elif sort == 'year_desc':
        cars = cars.order_by('-year')
    else:
        cars = cars.order_by('-id')  # default ordering

    # Get distinct makes for the filter dropdown
    makes = Car.objects.values_list('make', flat=True).distinct()

    context = {
        'cars': cars,
        'makes': makes,
        'filters': {
            'make': make or 'all',
            'year_min': year_min or '',
            'year_max': year_max or '',
            'price_min': price_min or '',
            'price_max': price_max or '',
            'sort': sort or '',
        }
    }
    return render(request, 'cars/car_list.html', context)



