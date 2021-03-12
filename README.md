# NirvanaAssessment

If I had more time for the bonus challenge my strategy to make InsuranceCombiner easily configurable N amount of api's would be to have a json file mapping each api to their respective module in api_wrapper the api_key needed eys hard coded so I would probably use an env var in the real world)

api_map = {'api1':{
                "path": "path/to/api_1_wrapper.py"
                "key": "api_key_1"
                }
            'api2: {
                "path": "path/to/api_3_wrapper.py"
                "key": "api_key_2"
                }

With the approach I can dynamically import each api wrapper we want to use, initialize it and call insurance_plan_summary() on each instance without having to hard code the wrappers in
InsuranceCombiner. Now all someone has to do to add a new api to the system is create a wrapper for it in the api_wrapper directory and follow function naming of all the other api wrappers

Additionally, instead of a json file I could dynamically import all modules from the api_wrapper dir, each api wrapper would have to store its own api at that point or use an env variable.

The reason I went with min, max and average of each field is because I was not sure what the data was being used for after it was coalesced.
With all of these functions available has a few options based on their needs.