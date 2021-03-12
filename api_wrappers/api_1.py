import requests

class Api1Wrapper(object):
    def __init__(self, api_key):
        self.key = api_key

    def insurance_plan_summary(self, member_id):
        # if I had the real api I would either use a pre made
        # python wrapper module made by the company providing the api
        # or call
        # requests.get(https://api1.com?member_id={}).format(memeber_id)
        try:
            resp = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
            # if resp.status_code != 200:
                # return {}
            return resp
        except Exception:
            return {}
