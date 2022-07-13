from engine.Engine import Engine

class CapuletEngine(Engine):

    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        engine_needs_service = self.current_mileage - self.last_service_mileage > 30000
        return engine_needs_service
