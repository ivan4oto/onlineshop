from typing import List
from stats.metric import Metric
from django.db.models import Sum, Count
from dateutil.rrule import rrule, MONTHLY


class OrderReportService():
    @classmethod
    def get_report_by_metric(cls, qs, metric, start_date, end_date) -> List:
        response = []
        if metric.upper() == Metric.COUNT.name:
            for dt in rrule(MONTHLY, dtstart=start_date, until=end_date):
                filtered_queryset = qs.filter(date__month=dt.month
                                              ).filter(
                                                date__year=dt.year
                                                ).aggregate(Count('products'))
                month = dt.strftime("%Y") + ' ' + dt.strftime("%b")
                value = filtered_queryset.get('products__count')
                if value:
                    response.append({
                            'month': month,
                            'value': value
                        })
        elif metric.upper() == Metric.PRICE.name:
            for dt in rrule(MONTHLY, dtstart=start_date, until=end_date):
                new_qs = qs.filter(date__month=dt.month).filter(
                    date__year=dt.year)
                month = dt.strftime("%Y") + ' ' + dt.strftime("%b")
                total = sum([qs.products.all().aggregate(Sum('price')
                                ).get('price__sum') for qs in new_qs])
                if total > 0:
                    response.append({
                        'month': month,
                        'value': total
                    })
        return response
