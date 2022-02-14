from ..models import Measurement


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement


def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.name = new_var["variable"]
    measurement.name = new_var["value"]
    measurement.name = new_var["unit"]
    measurement.name = new_var["place"]
    measurement.name = new_var["dateTime"]
    measurement.save()
    return measurement


def create_measurement(var):
    measurement = Measurement(variable=var["variable"], value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["dateTime"])
    measurement.save()
    return measurement