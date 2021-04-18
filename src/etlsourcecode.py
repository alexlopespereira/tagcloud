import datetime

from etlelk.etlbase import EtlBase
import glob

class EtlSourcecode(EtlBase):

    def __init__(self, config, job_description, limit=100000):
        super().__init__(config, job_description, limit=limit)

    def connect(self):
        pass

    def parse_result(self, results):
        return None

    def load_results(self):
        ans = []
        curr_date = datetime.datetime.now()
        if self.load_finished:
            return None
        for f in glob.glob('../data/**/*.py', recursive=True):
            with open(f, mode='r') as file:
                try:
                    ans.append({"filecontent": file.read(), "filepath": file.name, "date": curr_date})
                except UnicodeDecodeError as e:
                    print(e)
                    pass
        self.load_finished = True
        return ans

    def create_query(self, from_date=None, date_field=None):
        pass
