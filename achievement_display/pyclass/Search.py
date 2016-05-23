# encoding:utf-8
import json
import requests

class Search:
    def __init__(self):
        """
        初始化参数
        :return:
        """
        self.uri = 'http://192.168.120.90:9200/_search?pretty'

    def search(self, keyvalue, from_size, page_size):
        try:
            query = json.dumps({
                "from": from_size,
                "size": page_size,
                "query": {
                    "match":{
                        "name": keyvalue
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
    print s.search_in_id("Educational_1000000001")
    # now-1d/d now/d

