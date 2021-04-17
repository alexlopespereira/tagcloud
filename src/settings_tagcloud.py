body_settings_tagcloud = {
  "settings": {
    "analysis": {
      "analyzer": {
        "my_stop_analyzer": {
          "type": "stop",
          "stopwords": []
        }
      }
    }
  },
"mappings": {
    "_meta": {
      "created_by": ""
    },
    "properties": {
              "sourcefile": { "type": "text", "analyzer": "my_stop_analyzer"}
            }
    }
}
