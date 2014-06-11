from django.http import HttpResponse
from django.conf import settings

import xlwt

def xls_to_response(xls, fname):
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % fname
    xls.save(response)
    return response

def family_search_report(variants, family):
    raise NotImplementedError