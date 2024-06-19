import json
from django.views.generic import FormView
from .forms import JsonRpcForm
from .jsonrpc_client import jsonrpc_request


class JsonRpcView(FormView):
    template_name = 'api_client/form.html'
    form_class = JsonRpcForm

    def form_valid(self, form):
        method = form.cleaned_data['method']
        params = form.cleaned_data['params']
        try:
            params = json.loads(params)
        except json.JSONDecodeError:
            return self.render_to_response(self.get_context_data(
                form=form, result="Invalid JSON in parameters"))
        result = jsonrpc_request(method, params)
        return self.render_to_response(self.get_context_data(
            form=form, result=result))
