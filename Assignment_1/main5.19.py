# 1671617

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

service_first = str(input('Select first service:\n'))
service_second = str(input('Select second service:\n'))
print()
services = {
    "Oil change":35,
    "Tire rotation":19,
    "Car wash":7,
    "Car wax":12,
    "-": "No Service"
}

oil_change = services.get('Oil change')
tire_rotation = services.get('Tire rotation')
car_wash = services.get('Car wash')
car_wax = services.get('Car wax')
no_service = services.get('-')

print("Davy's auto shop invoice\n")

if service_first=="Oil change":
    print('Service 1: Oil change, $35')
elif service_first=="Tire rotation":
    print('Service 1: Tire rotation, $19')
elif service_first=="Car wash":
    print('Service 1: Car wash, $7')
elif service_first=="Car wax":
    print('Service 1: Car wax, $12')
elif service_first=="-":
    print('Service 1: No service')


if service_second=="Oil change":
    print('Service 2: Oil change, $35\n')
elif service_second=="Tire rotation":
    print('Service 2: Tire rotation, $19\n')
elif service_second=="Car wash":
    print('Service 2: Car wash, $7\n')
elif service_second=="Car wax":
    print('Service 2: Car wax, $12\n')
elif service_second=='-':
    print('Service 2: No service\n')

total = 0
if service_first!= "-":
    total += services[service_first]

if service_second!= "-":
    total += services[service_second]


print('Total: $' + str(total))
