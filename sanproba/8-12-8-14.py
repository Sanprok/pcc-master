# def make_car(proizv_name, model, **proiz):
#     a = {proizv_name: model}
#     # a[proizv_name] = model
#     for i, d in proiz.items():
#         a[i] = d
#     return a

import mak

b = 'sudzuki'
car = mak.make_car(b, 'outback', color='blue', зажигание='автомат', tow_package=True, )
print(car)
