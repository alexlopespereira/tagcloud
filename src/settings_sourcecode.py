body_settings_sourcecode = {
    "settings": {
        "max_result_window": "15000",
        "analysis": {
            "filter": {
                "source_keywords": {
                    "type": "stop",
                    "ignore_case": True,
                    "stopwords": ["msg", "df", "out", "will", "the", "to", "of", "data", "value", "other", "be", "result", "name", "tm",
                                  "an", "obj", "node", "expected", "this", "that", "it", "res", "cls", "ops", "Returns", "python", "object",
                                  "key", "index", "are", "param", "by", "evaluate", "dtypes"]
                },
                "one_character": {
                    "type": "length",
                    "min": 2
                }
            },
            "tokenizer": {
                "my_tokenizer": {
                    "type": "pattern",
                    "pattern": "[\W+&&[^_]]"
                }
            },
            "analyzer": {
                "my_pattern_analyzer": {
                    "tokenizer": "my_tokenizer",
                    "filter": [
                        "source_keywords",
                        "one_character"
                    ]
                }
            }
        }
    },
    "mappings": {
        "_meta": {
            "created_by": ""
        },
        "properties": {
            "filecontent": {"type": "text",
                            "analyzer": "my_pattern_analyzer",
                            "term_vector": "yes"},
            "filepath": {"type": "keyword"},
            "date": {"type": "date"}
        }
    }
}
