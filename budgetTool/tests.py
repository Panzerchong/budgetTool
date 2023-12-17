from django.test import TestCase
from .models import Service

class ServiceModelTestCase(TestCase):
    
    def setUp(self):
        # Create a Service instance for testing
        self.service = Service.objects.create(
            name="Test Service",
            category="OTHERS",
            type="Automation Engineer 2",
            isOnSite=True,
            hours_estimated=10,
            hours_worked=8,
            travel_actual=3000,
        )

    def test_create_service(self):
        self.assertIsInstance(self.service, Service)
        self.assertEqual(self.service.name, "Test Service")

    def test_read_service(self):
        service = Service.objects.get(id=self.service.id)
        self.assertEqual(service.name, "Test Service")

    def test_update_service(self):
        self.service.name = "Updated Service"
        self.service.save()
        updated_service = Service.objects.get(id=self.service.id)
        self.assertEqual(updated_service.name, "Updated Service")

    def test_delete_service(self):
        service_id = self.service.id
        self.service.delete()
        with self.assertRaises(Service.DoesNotExist):
            Service.objects.get(id=service_id)