class EcoTracker:
    def __init__(self):
        self.activities = []
    
    def add_activity(self, name, carbon_footprint):
        self.activities.append({
            'name': name,
            'carbon_footprint': carbon_footprint
        })
    
    def total_footprint(self):
        return sum(act['carbon_footprint'] for act in self.activities)

if __name__ == "__main__":
    tracker = EcoTracker()
    tracker.add_activity("Car Travel", 200)
    tracker.add_activity("Electricity Use", 150)
    print(f"Total Carbon Footprint: {tracker.total_footprint()} kg CO2")