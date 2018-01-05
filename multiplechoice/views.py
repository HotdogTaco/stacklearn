from django.shortcuts import render, reverse
from django.views import generic
from multiplechoice import models as multiplechoice_models

class MultipleChoiceAnswerCreateView(generic.CreateView):
    """ Class-based view to create answers to multiple choice questions.
    """
    model = mathstack_models.MultipleChoiceAnswer
    fields = ["raw_subject","raw_answer"]
    template_name = "mathstack/multiple_choice_answer_create.html"
    #context_object_name

    def get_context_data(self, **kwargs):
    	context_data = super(MultipleChoiceAnswerCreateView, self).get_context_data()
    	context_data["operand1"] = 10
    	return context_data
