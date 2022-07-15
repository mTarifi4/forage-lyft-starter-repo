import unittest
from datetime import datetime
from carFactory import CarFactory
     
class TestCalliope(unittest.TestCase):

    def test_engine_should_be_serviced (self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30001
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_calliope(last_service_date, current_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced (self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 29999
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_calliope(last_service_date,current_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced (self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 20000
        current_date = today

        car = CarFactory.create_calliope(last_service_date, current_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced (self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 20000
        current_date = today

        car = CarFactory.create_calliope(last_service_date, current_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())   



class TestGlissade(unittest.TestCase):

    def test_engine_should_be_serviced (self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30001
        last_service_mileage = 0
        current_date = today

        car = CarFactory.create_glissade(last_service_date, current_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())




if __name__ == '__main__':
    unittest.main()


