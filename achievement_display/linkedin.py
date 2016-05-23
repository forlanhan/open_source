import json
import requests


def search(uri, fromDate, toDate):
    try:
        query = json.dumps({
            "from": 0,
            "size": 1,
            "query": {
                "filtered": {
                    "query": {
                        "term": {"source_web": "linkedin_public"}
                    },
                    "filter": {
                        "range": {
                            "scrapy_time": {
                                "gte": fromDate,
                                "lte": toDate}
                        }
                    }
                }
            }
        })

        response = requests.get(uri, data=query)
        results = response.content
        results = json.loads(results)
        return results['hits']['total']
    except Exception, e:
        print 'get error : %s' % e
        return -1


def get_total(uri):
    try:
        query = json.dumps({
            "from": 0,
            "size": 1,
            "query": {
                "fuzzy_like_this": {
                    "fields": ['source_web'],
                    "like_text": 'linkedin_public'
                }
            }
        })
        response = requests.get(uri, data=query)
        results = response.content
        results = json.loads(results)
        return results['hits']['total']
    except Exception, e:
        print 'post es errors and e : ' % e
        return -1


if __name__ == "__main__":
    uri = 'http://192.168.120.17:9206/datahouse/records/_search?pretty'

    fromDate, toDate = '1900-10-01', '2016-04-12'
    print search(uri, fromDate, toDate)
    # now-1d/d now/d
    print get_total(uri)
