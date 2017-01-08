from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
