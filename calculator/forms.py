from django import forms

class FencingForm(forms.Form):
    land_in_acres = forms.FloatField(label='Land in acres')
    distance_between_posts = forms.FloatField(label='Distance between posts (in meters)')
    lines_of_barbed_wire = forms.IntegerField(label='Number of lines of barbed wire')
    weight_per_post = forms.FloatField(label='Weight per post (in kg)')
    number_of_people_to_offload = forms.IntegerField(label='Number of people to offload')
    number_of_corners = forms.IntegerField(label='Number of corners')