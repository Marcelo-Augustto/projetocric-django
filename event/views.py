from django.shortcuts import render
from django.views.generic.detail import DetailView

from event.models import Event, Bond, HowKnew, Enrollment

from cities.models import Route

from django.shortcuts import render, redirect
from event.models import EnrollmentForm

from django.contrib import messages


class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs['pk'])
        context['form'] = EnrollmentForm
        return context

def enrollment(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment successful!')
            return redirect('events:event', pk=event.pk)
    else:
        form = EnrollmentForm()
    context = {'event': event, 'form': form}
    
    return render(request, 'events/index.html', context)

