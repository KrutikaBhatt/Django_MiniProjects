from django.forms import ModelForm,TextInput
from .models import Currency,History,Feedback

class HistoryForm(ModelForm):
	class Meta:
		model = History
		fields = ['To','From','Amount','Result','Conversion_factor']
		widgets={'To' :TextInput(attrs={'class':'input','placeholder':"Add currency ,eg :INR"}),
		'From': TextInput(attrs = {'class' : 'input','placeholder' :'Add currency ,eg :USD"'}),
		'Amount': TextInput(attrs = {'class' : 'input','placeholder' :'1.00"'})
		}

		print(widgets['To'])

		




		
