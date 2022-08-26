from django_filters import CharFilter, FilterSet, NumberFilter

from reviews.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    name = CharFilter(field_name='name', lookup_expr='contains')
    year = NumberFilter(field_name='year')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'year', 'name')
