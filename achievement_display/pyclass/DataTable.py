#encoding: utf-8
from django_datatables_view.base_datatable_view import BaseDatatableView
from achievement_display.models import *
from achievement_display.pyclass.ConvertIdName import ConvertIdName

class OrderListJson(BaseDatatableView):

    model = Docyxcheckresult
    columns = ['id', 'processtime', 'checkstat', 'picnum', 'alertpicnum', 'reserverInt']
    order_columns = ['id', 'processtime', 'checkstat', 'picnum', 'alertpicnum', 'reserverInt']
    max_display_length = 500


    def render_column(self, row, column):
        # We want to render user as a custom column
        c = ConvertIdName()
        if column == 'id':
            #return '<td align="center" style="">%s</td>' % row.id
            return '<a href="#"> %s</a>' % row.id
        elif column == 'alertpicnum':
            return '<span class="badge">%s</span> ' % row.alertpicnum

        elif column == 'processtime':
            return '<span class="badge">%s</span> ' % row.processtime

        elif column == 'checkstat':
            return '<span class="badge">%s</span> ' % row.checkstat

        elif column == 'picnum':
            return '<span class="badge">%s</span> ' % row.picnum

        elif column == 'reserverInt':
            return c.convet_id_name(row.id)


        return c.convet_id_name(row.id)



    # def get_initial_queryset(self):
    #     # return queryset used as base for futher sorting/filtering
    #     # these are simply objects displayed in datatable
    #     # You should not filter data returned here by any filter values entered by user. This is because
    #     # we need some base queryset to count total number of records.
    #     return Docyxcheckresult.objects.all()
    #
    # def filter_queryset(self, qs):
    #     # use request parameters to filter queryset
    #
    #     # simple example:
    #     search = self.request.GET.get(u'search[value]', None)
    #     if search:
    #         qs = qs.filter(name__istartswith=search)
    #
    #     # more advanced example
    #     filter_customer = self.request.GET.get(u'customer', None)
    #
    #     if filter_customer:
    #         customer_parts = filter_customer.split(' ')
    #         qs_params = None
    #         for part in customer_parts:
    #             q = self.Q(customer_firstname__istartswith=part)|self.Q(customer_lastname__istartswith=part)
    #             qs_params = qs_params | q if qs_params else q
    #         qs = qs.filter(qs_params)
    #     return qs
