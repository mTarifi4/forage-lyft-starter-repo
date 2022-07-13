from battery.Battery import Battery

class SpindlerBattery(Battery):
    
    def __init__(self, current_date, last_service_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        year_difference = self.current_date.year - self.last_service_date.year
        return year_difference > 2
