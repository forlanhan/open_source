# encoding:utf-8
import json
import requests


class Search:
    def __init__(self):
        """
        初始化参数
        :return:
        """
        self.uri = 'http://192.168.120.90:9200/zjp-index:scholarkr/Thesis/_search?pretty'

    def search(self, keyvalue, from_size, page_size):
        try:
            query = json.dumps({
                "from": from_size,
                "size": page_size,
                 "query": {
                    "match": {
                      "_all": keyvalue
                    }
                  },
                "highlight": {
                    "fields": {
                      "*": {}
                    },
                    "require_field_match": False
                  }
            })
            response = requests.post(self.uri, data=query)
            results = response.content
            results = json.loads(results)
            context = {}
            context['total'] = results['hits']['total']
            context['time'] = results['took']
            context["result_content"] = results['hits']['hits']
            return context
        except Exception, e:
            print 'get error : %s' % e
            return -1

    def search_in_id(self, id):
        try:
            query = json.dumps({

                "query": {
                    "match_phrase":{
                        "_id": id
                    }
                }
            })
            response = requests.post(self.uri, data=query)
            results = response.content
            results = json.loads(results)
            context = {}
            context['total'] = results['hits']['total']
            context['time'] = results['took']
            context["result_content"] = results['hits']['hits']
            return context
        except Exception, e:
            print 'get error : %s' % e
            return -1


if __name__ == "__main__":
    uri = 'http://192.168.120.90:9200/test/_search?pretty'
    s = Search()
    s = Search()
    res = s.search("信息安全策略研究", 1,  100)
    print res
    # now-1d/d now/d

