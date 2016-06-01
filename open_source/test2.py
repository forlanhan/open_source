# encoding:utf-8
import json
from elasticsearch import Elasticsearch

class Search():
    """
    ES搜索类
    """
    def __init__(self):
        """
        基本的配置信息
        :return:
        """
        self.host = "192.168.120.90"
        self.port = 9200
        self.index = "zjp-index:scholarkr"
        self.doc_type = ['ConferencePaper', 'JournalPaper', 'Thesis']


    def generate_query(self, pap_type, body_type, keyvalue):
        """
        生成查询语句
        :param pap_type:文献类型, 分为三类 学术 | 期刊 | 学位
        :param body_type:文献搜索位置, 全文 | 标题 | 作者 | 单位 | 摘要
        :param keyvalue:搜索关键字
        :return:返回字典 dict
        """
        dict = {}

        if pap_type == "all":
            dict['doc_type'] = self.doc_type
        else:
            dict['doc_type'] = pap_type

        if body_type == "all":
            highlight_field = "*"
            match_field = "_all"
        else:
            match_field = body_type
            highlight_field = body_type

        dict['body'] = json.dumps({
            'query': {
                'match': {
                  match_field: keyvalue
             }
            },
            "highlight":{
                "fields": {
                  highlight_field: {}
                },
                "require_field_match": False
            }
        })

        return dict

    def s_search(self, pap_type, body_type, keyvalue, from_size, page_size):
        """
        :param pap_type:文献类型, 分为三类 学术 | 期刊 | 学位
        :param body_type:文献搜索位置, 全文 | 标题 | 作者 | 单位 | 摘要
        :param keyvalue:搜索关键字
        :param from_size起始数   page_size每页数量
        :return:返回搜索结果
        """

        """
        初始化参数
        """
        dict = {}  #定义查询字典
        s = Elasticsearch([{"host": self.host, "port": self.port}])
        context = {}   #定义返回数据

        """
        定义查询key-value
        """
        dict = self.generate_query(pap_type, body_type, keyvalue)
        dict['index'] = self.index
        dict['from_'] = from_size
        dict['size'] = page_size
        #dict['q'] = keyvalue


        """
        生成结果
        """
        results = s.search(**dict)

        """
        对结果进行提取
        """
        context['total'] = results['hits']['total']          #数据总数
        context['time'] = results['took']                    #数据时间
        context["result_content"] = results['hits']['hits']  #数据内容

        return context


if __name__ == "__main__":
    s = Search()
    res = s.s_search("JournalPaper", "author", "金红", 1, 5)
    print res['total']
    print res['time']
    print res['result_content'][0]
