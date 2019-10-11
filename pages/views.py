from django.shortcuts import render

# Create homepage
def index(request):
  
  return render(request, 'pages/index.html')