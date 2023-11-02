from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PeselForm


def pesel(request):
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel_number = request.POST.get('pesel')
            if not pesel_number.isdigit() or len(pesel_number) != 11:
                return HttpResponse('PESEL must be an 11-digit number.')
            digits = [int(digit) for digit in pesel_number]
            weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            weighted_sum = sum(digit * weight for digit, weight in zip(digits[:-1], weights))
            control_digit = (10 - (weighted_sum % 10)) % 10
            if control_digit != digits[-1]:
                return HttpResponse('Invalid PESEL number.')
            else:
                return HttpResponse('Valid PESEL number')
        else:
            return HttpResponse('Invalid form data or PESEL is not 11 digits.')

    else:
        form = PeselForm()
    return render(request, 'pesel/pesel.html', {'form': form})





