import requests

class Api2Wrapper(object):
    def __init__(self, api_key):
        self.key = api_key

    def insurance_plan_summary(self, member_id):
        # if I had the real api I would either use a pre made
        # python wrapper module made by the company providing the api
        # or call
        # requests.get(https://api2.com?member_id={}).format(memeber_id)
        try:
            resp = {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}
            # if resp.status_code != 200:
                # return {}
            return resp
        except Exception:
                return {}