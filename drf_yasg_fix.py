from drf_yasg.inspectors import CoreAPICompatInspector, FilterInspector, FieldInspector
from drf_yasg import openapi


class CustomFilterInspector(FilterInspector):
    def get_filter_parameters(self, view):
        if not view.filter_backends:
            return []

        parameters = []
        for backend in view.filter_backends:
            if hasattr(backend, 'get_schema_operation_parameters'):
                parameters.extend(backend.get_schema_operation_parameters(view))
        return parameters