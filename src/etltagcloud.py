import datetime

from etlelk.etlbase import EtlBase
import glob

class EtlTagcloud(EtlBase):

    def __init__(self, config, job_description, limit=100000):
        super().__init__(config, job_description, limit=limit)

    def connect(self):
        pass

    def parse_result(self, results):
        return None

    def load_results(self):
        ans = []
        size = 15000
        if self.load_finished:
            return None
        hits = self.config.es.search(index='sourcecode__sourcecode', params={"from": self.offset, "size": size},
                                     filter_path=['hits.hits._id'])['hits']['hits']
        ids = [x['_id'] for x in hits]
        vterms = self.config.es.mtermvectors(index="sourcecode__sourcecode", body={"ids": ids})
        for x in vterms['docs']:
            if x['term_vectors']:
                for k, v in x['term_vectors']['filecontent']['terms'].items():
                    ans.append({"term": k, "frequency": v["term_freq"]})

        self.load_finished = len(hits) < size
        self.offset += size
        return ans

    def create_query(self, from_date=None, date_field=None):
        pass
