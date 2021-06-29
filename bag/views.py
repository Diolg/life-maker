from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def shopping_bag(request):
    """ A view to return the shopping bag page  """

    return render(request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add qantity of the session to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Edit quantity of sprecified session to the selected amount """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, item_id):
    """ Remove sessions from the shoppong bag """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)  