from .models import Cars, Contracts

def get_available_cars():
    return Cars.objects.filter(is_reserved=False).exclude(contracts__isnull=False)

def get_user_contracts(user):
    return Contracts.objects.filter(author=user) if user.is_authenticated else []

def create_contract(car, user, counthours):
    return Contracts.objects.create(car=car, author=user, counthours=counthours)

def get_car_by_id(car_id):
    return Cars.objects.get(carid=car_id)

def delete_contract(contract_id, user):
    contract = Contracts.objects.get(contract_id=contract_id, author=user)
    contract.delete()

def create_car(car_data, user):
    car = Cars(**car_data)  # assumes car_data has appropriate keys
    car.owner = user
    car.save()
    return car

def delete_car(car_id):
    car = Cars.objects.get(carid=car_id)
    car.delete()

def get_car_for_edit(car_id):
    return Cars.objects.get(carid=car_id)

def update_car(car_id, car_data):
    car = Cars.objects.get(carid=car_id)
    for key, value in car_data.items():
        setattr(car, key, value)
    car.save()
    return car