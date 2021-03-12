import sys
from api_wrappers.api_1 import Api1Wrapper
from api_wrappers.api_2 import Api2Wrapper
from api_wrappers.api_3 import Api3Wrapper
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

# MAX_WORKERS = 3

class InsuranceCombiner(object):

    def __init__(self, api_1_key, api_2_key, api_3_key):
        # facade design pattern
        self.Api1Wrapper = Api1Wrapper(api_1_key)
        self.Api2Wrapper = Api2Wrapper(api_1_key)
        self.Api3Wrapper = Api3Wrapper(api_1_key)

    def get_plan_averages(self, member_id):
        # I wanted to make this faster by concurrently calling each api
        # but I don't want to go over the time limit
        # responses = []
        # with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        #     for resp  in executor.map(self._call_api, member_id):
        #         responses.append(resp)
        api_1_resp =  self.Api1Wrapper.insurance_plan_summary(member_id)
        api_2_resp =  self.Api2Wrapper.insurance_plan_summary(member_id)
        api_3_resp =  self.Api3Wrapper.insurance_plan_summary(member_id)

        deductable_total = [0,0]
        stop_loss_total = [0,0]
        oop_max_total = [0,0]
        for resp in [api_1_resp, api_2_resp, api_3_resp]:
            if resp.get('deductible', False):
                deductable_total[0] += resp['deductible']
                deductable_total[1] += 1
            if resp.get('stop_loss', False):
                stop_loss_total[0] += resp['stop_loss']
                stop_loss_total[1] += 1
            if resp.get('oop_max', False):
                oop_max_total[0] += resp['oop_max']
                oop_max_total[1] += 1

        average = {}
        # Set to none if we somehow don't get a value from any of the APIs
        average['deductible'] = None if deductable_total[0] == 0 else \
                int(deductable_total[0]/deductable_total[1])
        average['stop_loss'] = None if stop_loss_total[0] == 0 else \
                int(stop_loss_total[0]/stop_loss_total[1])
        average['oop_max'] = None if oop_max_total[0] == 0 else \
                int(oop_max_total[0]/oop_max_total[1])
        return average

    def get_plan_min(self, member_id):
        # I wanted to make this faster by concurrently calling each api
        # but I don't want to go over the time limit
        # responses = []
        # with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        #     for resp  in executor.map(self._call_api, member_id):
        #         responses.append(resp)
        api_1_resp =  self.Api1Wrapper.insurance_plan_summary(member_id)
        api_2_resp =  self.Api2Wrapper.insurance_plan_summary(member_id)
        api_3_resp =  self.Api3Wrapper.insurance_plan_summary(member_id)

        min_deductible = sys.maxsize
        min_stop_loss = sys.maxsize
        min_oop_max = sys.maxsize
        for resp in [api_1_resp, api_2_resp, api_3_resp]:
            if resp.get('deductible', False) and resp['deductible'] < min_deductible:
                min_deductible = resp['deductible']
            if resp.get('stop_loss', False) and resp['stop_loss'] < min_stop_loss:
                min_stop_loss = resp['stop_loss']
            if resp.get('oop_max', False) and resp['oop_max'] < min_oop_max:
                min_oop_max = resp['oop_max']

        plan_mins = {}
        # Set to none if we somehow don't get a value from any of the APIs
        plan_mins['deductible'] = None if min_deductible == sys.maxsize else min_deductible
        plan_mins['stop_loss'] = None if min_stop_loss == sys.maxsize else min_stop_loss
        plan_mins['oop_max'] = None if min_oop_max == sys.maxsize else min_oop_max
        return plan_mins

    def get_plan_max(self, member_id):
        # I wanted to make this faster by concurrently calling each api
        # but I don't want to go over the time limit
        # responses = []
        # with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        #     for resp  in executor.map(self._call_api, member_id):
        #         responses.append(resp)
        api_1_resp =  self.Api1Wrapper.insurance_plan_summary(member_id)
        api_2_resp =  self.Api2Wrapper.insurance_plan_summary(member_id)
        api_3_resp =  self.Api3Wrapper.insurance_plan_summary(member_id)

        max_deductible = 0
        max_stop_loss = 0
        max_oop_max = 0
        for resp in [api_1_resp, api_2_resp, api_3_resp]:
            if resp.get('deductible', False) and resp['deductible'] > max_deductible:
                max_deductible = resp['deductible']
            if resp.get('stop_loss', False) and resp['stop_loss'] > max_stop_loss:
                max_stop_loss = resp['stop_loss']
            if resp.get('oop_max', False) and resp['oop_max'] > max_oop_max:
                max_oop_max = resp['oop_max']

        plan_maxes = {}
        #Set to none if we somehow don't get a value from any of the APIs
        plan_maxes['deductible'] = None if max_deductible == 0 else max_deductible
        plan_maxes['stop_loss'] = None if max_stop_loss == 0 else max_stop_loss
        plan_maxes['oop_max'] = None if max_oop_max == 0 else max_oop_max
        return plan_maxes

    # def _call_api(self, api, member_id):
    #     return api.insurance_plan_summary(member_id)
