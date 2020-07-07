from django_filters.rest_framework import FilterSet

from api.models import Computer


class MyFilter:

    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get("limit")
        if limit and queryset:
            limit = int(limit)
            return queryset[:limit]

        return queryset


class ComputerFilterSet(FilterSet):
    from django_filters import filters
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")

    class Meta:
        model = Computer

        fields = ['name', "min_price", "max_price"]
