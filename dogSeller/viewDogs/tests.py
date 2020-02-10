from django.test import TestCase
from .models import Dogs 
# Create your tests here.

class DogsTest(TestCase):
    def setUp(self):
        d1 = Dogs.objects.create(name="Pug Ash Grey",price="20000", stockNo="1",image="media/images/RoyalCanin_Zoey_PureBreed-1-1-940x529.jpg",breed="Pug",weight="8",description="/This dog is short,cute and very playful. It is friendly and this dog can guard your house as well.")
        d2 = Dogs.objects.create(name="Golden Retriever",price="16000", stockNo="5",image="/media/images/48c56ffe8159c63ec3d6f0d0cfa3f5b920c26340.jpg",breed="Retriever",weight="4",description="This is a excellent dog if you are looking for a friendly dog")
    def test_count_Dogs_in_stock(self):
        gop= Dogs.objects.all()
        self.assertEqual(gop.count(), 2)

    def test_dogs_stock(self):
        d1 = Dogs.objects.create(name="Pug Ash Grey",price="20000", stockNo="1",image="media/images/RoyalCanin_Zoey_PureBreed-1-1-940x529.jpg",breed="Pug",weight="8",description="/This dog is short,cute and very playful. It is friendly and this dog can guard your house as well.")
        self.assertTrue(d1.is_in_stock())