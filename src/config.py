import os
from collections import defaultdict
from elasticsearch import Elasticsearch
from etlelk.configbase import ConfigBase
from settings_tagcloud import body_settings_tagcloud
# from dotenv import load_dotenv
from src.settings_sourcecode import body_settings_sourcecode


class Config(ConfigBase):

    # load_dotenv()
    DEBUG = os.environ.get('DEBUG') == "True"

    KIBANA_SAVED_OBJECTS_PATH = os.environ.get('KIBANA_SAVED_OBJECTS_PATH') or './saved_objects'
    KIBANA_HOST = os.environ.get('KIBANA_HOST') or os.environ.get('ES_HOST') or 'kibana'
    KIBANA_PORT = os.environ.get('KIBANA_PORT') or '5601'
    ES_HOST = os.environ.get('ES_HOST') or 'localhost'
    ES_PORT = os.environ.get('ES_PORT') or '9200'
    ES_USER = os.environ.get('ES_USER') or 'admin'
    ES_PASSWORD = os.environ.get('ES_PASSWORD') or 'pass'  ## Setar Variavel de Ambiente
    ES_USE_SSL = os.environ.get('ES_USE_SSL') == "True"
    ES_VERIFY_CERTS = os.environ.get('ES_VERIFY_CERTS') == "True"
    ES_TAGCLOUD_INDEX = 'tagcloud__tagcloud'
    ES_SOUCECODE_INDEX = 'sourcecode__sourcecode'

    if ES_USE_SSL:
        ES_URL = "https://{0}".format(ES_HOST)
    else:
        ES_URL = "http://{0}:{1}".format(ES_HOST, ES_PORT)

    if DEBUG:
        KIBANA_DEST_URL = os.environ.get('KIBANA_DEST_URL') or 'http://10.209.42.191:5601'
    else:
        KIBANA_DEST_URL = "http://{0}:{1}".format(KIBANA_HOST, KIBANA_PORT)


    job_tagcloud = {"index": ES_TAGCLOUD_INDEX, "settings": body_settings_tagcloud,
                      "namespace": "default",
                      "module_name": "etltagcloud", "class_name": "EtlTagcloud"}
    job_sourcecode = {"index": ES_SOUCECODE_INDEX, "settings": body_settings_sourcecode,
                      "namespace": "default", "date_field": "date",
                      "module_name": "etlsourcecode", "class_name": "EtlSourcecode"}

    INDEXES = {'tagcloud': job_tagcloud, 'sourcecode': job_sourcecode}

    es = Elasticsearch(
        hosts=[{'host': ES_HOST, 'port': ES_PORT}],
        http_auth=(ES_USER, ES_PASSWORD),
        use_ssl=ES_USE_SSL,
        verify_certs=ES_VERIFY_CERTS
    )

    # def __init__(self):
    #     global es
    #     self.es = es
