import unittest
from unittest import mock
from chair_factory import (
    Chair,
    ModernBuilder,
    ModernChair,
    VintageBuilder,
    VintageChair,
)


class TestChairBuilders(unittest.TestCase):
    def test_modern_builder(self):
        self.assertIsInstance(ModernBuilder().build_chair(1, 1), ModernChair)

    def test_vintage_builder(self):
        self.assertIsInstance(VintageBuilder().build_chair(1, 1), VintageChair)

    def test_builder(self):
        self.assertIsInstance(VintageBuilder().build_chair(1, 1), Chair)

    def test_modern_chair_constructor(self):
        chair = mock.Mock()
        chair.weight = 1
        chair.cost = 1
        result = ModernBuilder().build_chair(1, 1)
        self.assertEqual(result.weight, chair.weight)
        self.assertEqual(result.cost, chair.cost)

    def test_vintage_builder_proccess(self):
        builder = VintageBuilder()
        builder.building_process = mock.MagicMock()
        builder.build_chair(2, 2)
        builder.building_process.assert_called_once_with(2, 2)


if __name__ == "__main__":
    unittest.main()
