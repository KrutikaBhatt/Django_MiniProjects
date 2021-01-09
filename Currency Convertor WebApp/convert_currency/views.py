import requests
from datetime import date
from django.shortcuts import render
from .models import Currency,History,Feedback
from .forms import HistoryForm
# Create your views here.


def index(request):

	API ="Z91BHR6HZNHV6E68"
	BASE_URL=r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

	if request.method == 'POST':
		print("Post requested")
		form = HistoryForm(request.POST)
		if form.is_valid():
			obj = form.save()
			print(obj)
		"""
		main_url = BASE_URL + "&from_currency=" + From + "&to_currency=" + To + "&apikey=" + API
		result = requests.get(main_url).json()

		Conversion_factor = result['Realtime Currency Exchange Rate']["5. Exchange Rate"]
		form.fields['Conversion_factor'] = Conversion_factor
		form.fields['Result'] = round(float(Amount)*Conversion_factor,3)
"""
	form = HistoryForm()

	
	#main_url = BASE_URL + "&from_currency=" + From + "&to_currency=" + To + "&apikey=" + API	

	#result = requests.get(main_url).json()  # Recieve the JSON file 
	history_data = []
	"""
	The result is viewed as
	{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "INR",
        "2. From_Currency Name": "Indian Rupee",
        "3. To_Currency Code": "USD",
        "4. To_Currency Name": "United States Dollar",
        "5. Exchange Rate": "0.01363900",
        "6. Last Refreshed": "2021-01-08 12:15:02",
        "7. Time Zone": "UTC",
        "8. Bid Price": "0.01363898",
        "9. Ask Price": "0.01363923"
    }
}
	"""
	history = History.objects.all()
	for his in history:
		Exchange_Rate = his.Conversion_factor

		result_conversion = {
		'from': his.From,
		'To' : his.To,
		'amount' : his.Amount,
		'Conversion_values': Exchange_Rate,
		'result' : his.Result,
		'Date' :his.Date,
		}

		history_data.append(result_conversion)

	context	={'history_data':history_data,'form':form}

	return render(request,'convert_currency/Convertor.html',context)

def fullform(request):

	fullform_data =[]
	data = Currency.objects.all()

	for curr in data:
		currency = {
		'name': curr.currency,
		'shortform' :curr.shortform,
		}

		fullform_data.append(currency)

	context = {'fullform_data': fullform_data}
	
	return render(request,'convert_currency/Fullforms.html',context)

def feedback(request):
	return render(request,'convert_currency/Feedback.html')