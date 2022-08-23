from rest_framework import viewsets
from rest_framework.response import Response
from stats.models import Order, Product
from stats.serializers import ProductSerializer, OrderSerializer
from stats.services import OrderReportService
from datetime import datetime


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        queryset = self.queryset
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        metric = self.request.query_params.get('metric')

        if all([date_start, date_end, metric]):
            date_start, date_end = date_start.split('-'), date_end.split('-')
            start_date = datetime(
                int(date_start[0]), int(date_start[1]), int(date_start[2]))
            end_date = datetime(
                int(date_end[0]), int(date_end[1]), int(date_end[2]))
            report = OrderReportService.get_report_by_metric(
                queryset, metric, start_date, end_date
            )
            return Response(report)

        queryset = self.paginate_queryset(queryset)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
