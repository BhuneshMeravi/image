from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ImageSerializer

@api_view(['POST'])
def image(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        image = serializer.validated_data['image']
        filename = default_storage.save(image.name, ContentFile(image.read()))
        file_url = default_storage.url(filename)

        # Generate four variations of the image
        image = Image.open(file_url)
        image.thumbnail((200, 300))
        image.save(f'{filename}_thumbnail.jpg')
        image.thumbnail((500, 500))
        image.save(f'{filename}_medium.jpg')
        image.thumbnail((1024, 768))
        image.save(f'{filename}_large.jpg')
        image.convert('L').save(f'{filename}_grayscale.jpg')

        return Response(status=201)
    return Response(serializer.errors, status=400)
