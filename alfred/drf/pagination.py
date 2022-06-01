from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberOffsetPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "per_page"
    max_page_size = 500
    default_paginate = 20

    def get_page_number(self, request, paginator):
        default_page_number = request.query_params.get(self.page_query_param, None)
        page_number = 1

        if default_page_number:
            page_number = int(default_page_number)
        else:
            offset = request.query_params.get("offset", None)
            if offset is not None:
                page_number = int(offset) / self.get_page_size(request)

        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        return int(page_number or 1)

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)

        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)
        except:  # noqa
            return []

        self.request = request
        return list(self.page)

    def get_page_size(self, request):

        for item in ["per_page", "limit"]:
            try:
                per_page = request.query_params[item]
                return int(per_page)
            except:  # noqa
                continue
        return self.default_paginate

    def get_paginated_response(self, data):
        page = getattr(self, "page", None)
        return Response(
            {
                "next": self.get_next_link() if page else None,  # legado
                "previous": self.get_previous_link() if page else None,  # legado
                "page": page.number if page else 1,
                "per_page": page.paginator.per_page if page else self.default_paginate,
                "total_items": page.paginator.count if page else 0,
                "count": page.paginator.count if page else 0,
                "total_pages": page.paginator.num_pages if page else 1,
                "results": data,
            }
        )
