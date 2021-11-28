from rest_framework.response import Response
from rest_framework.decorators import  api_view
from rest_framework.reverse import reverse

@api_view()
def api_root(request):
    return Response({
    'add': reverse('add', request=request),
    'subtract': reverse('subtract', request=request),
    'multiply': reverse('multiply', request=request),
    'divide': reverse('divide', request=request),
})

@api_view()
def add(request):
    '''
    Add function
    add(
        a: int,
        b: int,
        :return: int
    )
    example call: domain/add/?a=1&b=1
    will return a json like: {'function': add, 'result': 2}
    '''
    try:
        num1 = int(request.GET.get('a'))
        num2 = int(request.GET.get('b'))
        return Response({'function': 'add', 'result': num1+num2})
    except Exception as e:
        return Response({'function': 'add', 'result': 'There was an error '+str(e)})

@api_view()
def subtract(request):
    '''
    subtract function
    subtract(
        a: int,
        b: int,
        :return: int
    )
    example call: domain/subtract/?a=10&b=1
    will return a json like: {'function': subtract, 'result': 9}
    '''
    try:
        num1 = int(request.GET.get('a'))
        num2 = int(request.GET.get('b'))
        return Response({'function': 'subtract', 'result': num1-num2})
    except Exception as e:
        return Response({'function': 'subtract', 'result': 'There was an error '+str(e)})

@api_view()
def multiply(request):
    '''
    Multiply function
    multiply(
        a: int,
        b: int,
        :return: int
    )
    example call: domain/multiply/?a=1&b=5
    will return a json like: {'function': multiply, 'result': 5}
    '''
    try:
        num1 = int(request.GET.get('a'))
        num2 = int(request.GET.get('b'))
        return Response({'function': 'multiply', 'result': num1*num2})
    except Exception as e:
        return Response({'function': 'multiply', 'result': 'There was an error '+str(e)})

@api_view()
def divide(request):
    '''
    divide function
    divide(
        a: int,
        b: int,
        :return: int
    )
    example call: domain/multiply/?a=6&b=2
    will return a json like: {'function': divide, 'result': 3}
    '''
    try:
        num1 = int(request.GET.get('a'))
        num2 = int(request.GET.get('b'))
        return Response({'function': 'divide', 'result': num1/num2})
    except Exception as e:
        return Response({'function': 'divide', 'result': 'There was an error '+str(e)})