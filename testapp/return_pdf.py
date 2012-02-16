from reportlab.pdfgen import canvas
from django.http import HttpResponse

from cStringIO import StringIO

def hello_pdf(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'

	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)


	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(10, 800, "Hello World.")


	#Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response



def hello_pdf_advanced(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello_advanced.pdf'

	temp = StringIO()

	# Create the PDF object, using the StringIO object as its "file."
	p = canvas.Canvas(temp)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 800, "Hello advanced World.")

	#Close the PDF object cleanly.
	p.showPage()
	p.save()

	# Get the value of the StringIO buffer and write it to the response.
	response.write(temp.getvalue())
	return response
