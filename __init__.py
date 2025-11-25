import odoo.http as http

_orig_dispatch = http.Root.dispatch

def broken_dispatch(self, request):
    raise Exception("Forced Internal Server Error for testing")

http.Root.dispatch = broken_dispatch
