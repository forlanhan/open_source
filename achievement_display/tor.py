import json
import requests


def search(uri, fromDate, toDate):
    try:
        query = json.dumps({
            "from": 0,
            "size": 1,
            "query": {
                "filtered": {
                    "filter": {
                        "range": {
                            "scrapy_time": {
                                "gte": fromDate,
                                "lte": toDate
                            }
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
        })
        response = requests.get(uri, data=query)
        results = response.content
        results = json.loads(results)
        return results['hits']['total']
    except Exception, e:
        print 'post es errors and e : ' % e
        return -1


if __name__ == "__main__":
    uri = 'http://192.168.120.17:9206/hiddenwebs/hiddenwebpages/_search?pretty'

    fromDate, toDate = '2015-1-1', '2016-10-1'
    # print search(uri, fromDate, toDate)
    # now-1d/d now/d
    print get_total(uri)
