
# api 1 stubs
def bad_response(self, something):
    return {}

def no_deductable(self, something):
    return{"stop_loss": 10000, "oop_max": 5000}

def no_stop_loss(self, something):
    return{"deductible": 1000, "oop_max": 5000}

def no_oop(self, something):
    return{"deductible": 1000, "stop_loss": 10000}