from django.http import JsonResponse

def post_list(request):
  data = {
    'products': [
      {
          'name': 'Naked Cake',
          'description': 'Pensando en los graves problemas de obesidad de la actualidad, el naked cake reduce la cantidad de calorías para consumo.',
          'price': 300,
          'image': 'https://images.pexels.com/photos/5945565/pexels-photo-5945565.jpeg?auto=compress&cs=tinysrgb&w=1600',
          'promotion': {
            'name': 'Promo 1',
            'description': '',
            'discount': 22,
            'price': 288
          }
      },
      {
          'name': 'Basic Vanilla Cake Basic Vanilla Cake Basic Vanilla Cake',
          'description': 'Pensando en los graves problemas de obesidad de la actualidad, el Basic Vanilla Cake reduce la cantidad de calorías para consumo.',
          'price': 190,
          'image': 'https://images.pexels.com/photos/5945565/pexels-photo-5945565.jpeg?auto=compress&cs=tinysrgb&w=1600',
          'promotion': {
            'name': 'Promo 2',
            'description': '',
            'discount': 40,
            'price': 150
          }
      },
      {
          'name': 'Clinkers Cake',
          'description': 'Pensando en los graves problemas de obesidad de la actualidad, el Clinkers Cake reduce la cantidad de calorías para consumo.',
          'price': 320,
          'image': 'https://images.pexels.com/photos/5945565/pexels-photo-5945565.jpeg?auto=compress&cs=tinysrgb&w=1600',
          'promotion': {
            'name': 'Promo 3',
            'description': '',
            'discount': 20,
            'price': 300
          }
      },
      {
          'name': 'Example Cake',
          'description': 'Pensando en los graves problemas de obesidad de la actualidad, el Example vanilla Cake reduce la cantidad de calorías para consumo.',
          'price': 320,
          'image': 'https://images.pexels.com/photos/5945565/pexels-photo-5945565.jpeg?auto=compress&cs=tinysrgb&w=1600',
          'promotion': {
            'name': 'Promo 4',
            'description': '',
            'discount': 20,
            'price': 300
          }
      }
    ]
  }
  return JsonResponse(data)