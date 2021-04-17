from etlelk.etlbase import EtlBase
import pandas as pd
import datetime
import glob

class EtlTagcloud(EtlBase):

    def __init__(self, config, job_description, limit=100000):
        super().__init__(config, job_description, limit=limit)

    def connect(self):
        pass

    def parse_result(self, results):
        return None

    def load_results(self):
        for f in glob.glob('/path/**/*.c', recursive=True):
            print(f)
        ans = None
        return ans

    def create_query(self, from_date=None, date_field=None):
        pass
