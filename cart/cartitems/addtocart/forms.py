from django import forms


item_quantity=[(i,str(i)) for i in range(1,21)]

class cartadditemForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=item_quantity, coerce=int, label="quantity")
    update= forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)