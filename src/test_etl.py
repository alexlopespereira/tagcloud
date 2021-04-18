from etlelk import KibanaFunctions
from etlelk.run_etl_jobs import run_etl_job
from config import Config

config = Config()
kf = KibanaFunctions(config)
kf.els.delete_index(config.es, config.INDEXES['sourcecode']['index'])
run_etl_job(config, config.INDEXES['sourcecode'])

kf.els.delete_index(config.es, config.INDEXES['tagcloud']['index'])
run_etl_job(config, config.INDEXES['tagcloud'])




