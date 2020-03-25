import datetime
from haystack import indexes
from .models import Term, Synonym


class TermIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Term

    def get_description(self, obj):
        return obj.description

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def get_search_data(self, obj):
        return obj.specs

    def get_title(self, obj):
        return obj.title

    index_title = True
