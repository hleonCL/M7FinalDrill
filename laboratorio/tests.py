from django.test import TestCase, Client
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')
        print('setUpTestData se ejecutó correctamente \n **************** ')


    def test_laboratorio(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.nombre, 'Laboratorio 1')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'País 1')
        print('La prueba de laboratorio se ejecutó correctamente \n ****************')


    def test_laboratorio_url(self):
        client = Client()
        response = client.get('/laboratorios/')
        self.assertEqual(response.status_code, 200)
        print('La prueba de url HTTP 200 se ejecutó correctamente \n ****************')


    def test_laboratorio_template(self):
        client = Client()
        response = client.get(reverse('laboratorios'))
        self.assertTemplateUsed(response, 'laboratorios.html')
        self.assertContains(response, 'Laboratorio 1')
        print('La prueba Reverse URL se ejecutó correctamente\n ****************')

