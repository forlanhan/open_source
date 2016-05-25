#encoding: utf-8
from django_datatables_view.base_datatable_view import BaseDatatableView
from achievement_display.models import *
from achievement_display.pyclass.ConvertIdName import ConvertIdName

class BmCheck(BaseDatatableView):
    """
    id: 编号
    alertnum: 告警数量
    score: 打分
    processtime: 处理时间
    processresult: 处理结果

    reserverInt: 保留字段1
    reserverStr: 保留字段2
    """
    model = Docbmcheckresult
    columns = ['id', 'alertnum', 'score', 'processtime', 'processresult', 'reserverint']
    order_columns = ['id', 'alertnum', 'score', 'processtime', 'processresult', 'reserverint']
    max_display_length = 500

    # def render_column(self, row, column):
    #     # We want to render user as a custom column
    #     c = ConvertIdName()
    #     if column == 'reserverint':
    #         return c.convet_id_name(row.id)
    #     else:
    #         return super(BmCheckAlert, self).render_column(row, column)


    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. This is because
        # we need some base queryset to count total number of records.
        return Docbmcheckresult.objects.all()
