import csv
from django.http import HttpResponse

# Number of unruly passengers each year 1995 - 2005. In a real application
# this would likely come from a database or some other back-end data store.

UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]


def unruly_passengers_csv(request):
	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(mimetype='text/csv')
	response['Content-Disposition'] = 'attachment; filename=unruly.csv'


	# Create the CSV writer using the HttpResponse as the "file."
	writer = csv.writer(response)
	writer.writerow(['Year', 'Unruly Airline Passengers'])
	for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
		writer.writerow([year, num])
	

	return response



