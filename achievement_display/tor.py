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
                            "create_time": {
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
        return -1




# def get_total(uri):
#     try:
#         query = json.dumps({
#             "from": 0,
#             "size": 1,
#
#             "query": {
#                 "regexp": {
#                     "create_time": "2016",
#
#
#             }
#         }
#
#         })
#         response = requests.get(uri, data=query)
#         results = response.content
#         results = json.loads(results)
#         return results['hits']['total']
#     except Exception, e:
#         print 'post es errors and e : ' % e
#         return -1

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
        return -1


if __name__ == "__main__":
    uri = 'http://192.168.120.17:9206/hiddenwebs_v2/hiddenwebpages/_search?pretty'
    fromDate, toDate = '2016-04-11', '2016-04-12'
    print search(uri, fromDate, toDate)
    # now-1d/d now/d
   # print get_total(uri)
