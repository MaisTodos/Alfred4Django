from alfred.drf.pagination import PageNumberOffsetPagination


def test_attributes():
    assert PageNumberOffsetPagination.page_query_param == "page"
    assert PageNumberOffsetPagination.page_size_query_param == "per_page"
    assert PageNumberOffsetPagination.max_page_size == 500
    assert PageNumberOffsetPagination.default_paginate == 20


def test_methods(request):
    methods_list = [
        "get_page_number",
        "paginate_queryset",
        "get_page_size",
        "get_paginated_response",
    ]
    for method in methods_list:
        assert method in dir(PageNumberOffsetPagination)
