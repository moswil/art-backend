# Third-Party Imports
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError

# App Imports
from core.models import AssetMake, AssetType
from core.tests import CoreBaseTestCase


class AssetMakeTestCase(CoreBaseTestCase):
    def test_can_create_asset_make(self):
        count = AssetMake.objects.count()
        AssetMake.objects.create(name="Bose", asset_type=self.asset_type)
        self.assertEqual(AssetMake.objects.count(), count + 1)

    def test_cannot_add_existing_asset_make(self):
        count = AssetMake.objects.count()
        with self.assertRaises(ValidationError):
            AssetMake.objects.create(
                name=AssetMake.objects.first().name, asset_type=self.asset_type
            )
        self.assertEqual(AssetMake.objects.count(), count)

    def test_can_edit_asset_make(self):
        self.asset_make.name = "Sony"
        self.asset_make.save()
        make = AssetMake.objects.get(id=self.asset_make.id)
        self.assertEqual(make.name, "Sony")

    def test_asset_make_model_string_representation(self):
        asset_make = AssetMake.objects.first()
        self.assertEqual(str(asset_make), asset_make.name)

    def test_cannot_add_make_with_non_exisiting_type(self):
        """ Test cannot add make with non-existing type """
        with self.assertRaises(ValueError):
            AssetMake.objects.create(name="Skull Candy", asset_type=6898)

    def test_delete_type_protects_make(self):
        """ Test that the make is not deleted when the type is deleted """
        type_count = AssetType.objects.count()
        make_count = AssetMake.objects.count()
        with self.assertRaises(ProtectedError):
            self.asset_type.delete()
        self.assertEqual(AssetType.objects.count(), type_count)
        self.assertEqual(AssetMake.objects.count(), make_count)
