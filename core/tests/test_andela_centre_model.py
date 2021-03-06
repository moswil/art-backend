# Third-Party Imports
from django.db import IntegrityError, transaction

# App Imports
from core.tests import CoreBaseTestCase

from ..models import AndelaCentre


class AndelaCentreModelTest(CoreBaseTestCase):
    """ Tests for the Andela Centre Model """

    def test_can_save_a_centre(self):
        AndelaCentre.objects.create(name="Gorilla", country=self.country)
        new_centre = AndelaCentre.objects.get(name="Gorilla")
        new_centre_count = AndelaCentre.objects.count()

        self.assertEqual(new_centre_count, 2)
        self.assertIn(new_centre.name, "Gorilla")

    def test_cannot_add_existing_centre_name(self):
        self.assertEqual(AndelaCentre.objects.count(), 1)
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_centre = AndelaCentre.objects.create(name="ET")
                new_centre.save()

        self.assertEqual(AndelaCentre.objects.count(), 1)

    def test_can_edit_a_centre(self):
        self.centre.name = "The dojo"
        self.centre.save()
        self.assertIn("The dojo", self.centre.name)

    def test_can_delete_a_centre(self):
        new_centre = AndelaCentre.objects.create(name="The dojo", country=self.country)
        new_centre_count = AndelaCentre.objects.count()
        new_centre.delete()
        count_after_deletion = AndelaCentre.objects.count()

        self.assertEqual(new_centre_count, 2)
        self.assertEqual(count_after_deletion, 1)

    def test_asset_centre_model_string_representation(self):
        self.assertEqual(str(self.centre), "ET")
