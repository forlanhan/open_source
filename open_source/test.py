# encoding: utf-8
from elasticsearch import Elasticsearch
import json
es = Elasticsearch([{'host':'192.168.120.90', 'port':9200}])
query = json.dumps({

                "query": {
                    "match":{
                        "name": "中国 科学院",
                        # "operator": "or"

                    }
                }
            })
doc = json.dumps({
    "name" : "中国科学院信息工程研究送"
})
dict = {}
dict['index'] = 'scholarkr'
#dict['from_'] = 10
#dict['doc_type'] = 'Org'
#dict['ignore'] = [400, 404, 401, 402, 403]
#dict['size'] = 1
#dict['q'] = "中国科学院信息工程研究所"
dict['body'] = query
#dict['fields'] = "name"
#dict['body'] = query
#dict['name'] = "中国科学院"
res = es.search(**dict)

#res = es.bulk(**dict)

print res['hits']['hits'][0]
print res['took']
print res['_shards']
