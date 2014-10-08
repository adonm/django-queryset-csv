
import djqscsv
from models import Person
from .util import create_people_and_get_queryset

def querydict_to_kwargs(qd):
    kwargs = {}
    d = dict(qd)
    for k, v in d.items():
        if len(v) > 1:
            raise
        else:
            kwargs[k] = v[0]
    return djqscsv._sanitize_unicode_record(kwargs)


def get_csv(request):
    qs = create_people_and_get_queryset()
    kwargs = querydict_to_kwargs(request.GET)
    return djqscsv.render_to_csv_response(qs, **kwargs)
