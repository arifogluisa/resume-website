from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile, Skill
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import send_mail


class IndexView(SuccessMessageMixin, TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')
    success_message = 'Your message has been sent successfully'

    def form_valid(self, form):
        form.save()
        from_email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(subject, message, from_email, ['arifogluisa@gmail.com'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["me"] = Profile.objects.first()
        context["skills"] = Skill.objects.all()
        return context
    