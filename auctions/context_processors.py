from .models import  categories

def categories_processor(request):
    return {'categories': categories.objects.all()}