import unittest
from mus_orch import Musician, Orchestra, MusOrch, task_1, task_2, task_3


class TestRK1Tasks(unittest.TestCase):
    def setUp(self):
        self.orchestras = [
            Orchestra(1, "Electric Light Orchestra"),
            Orchestra(2, "Mariinsky Theatre Orchestra"),
            Orchestra(3, "Moscow Chamber Orchestra"),
            Orchestra(4, "Ukrainian Radio Symphony Orchestra"),
            Orchestra(5, "National Symphony Orchestra of Ukraine"),
        ]
        self.musicians = [
            Musician(1, "Линн", 70000, 1),
            Musician(2, "Тэнди", 67000, 1),
            Musician(3, "Смирнов", 20000, 2),
            Musician(4, "Карпов", 32000, 3),
            Musician(5, "Прокопенко", 14000, 4),
            Musician(6, "Карчук", 12000, 5),
            Musician(7, "Соловьёва", 14000, 3),
        ]
        self.mus_orch = [
            MusOrch(1, 1),
            MusOrch(1, 2),
            MusOrch(2, 3),
            MusOrch(3, 4),
            MusOrch(3, 7),
            MusOrch(4, 5),
            MusOrch(5, 6),
            MusOrch(1, 3),
            MusOrch(4, 1),
            MusOrch(2, 4),
            MusOrch(3, 3),
        ]

    def test_task_1(self):

        answer = [
            ("Карпов", 32000, "Moscow Chamber Orchestra"),
            ("Карчук", 12000, "National Symphony Orchestra of Ukraine"),
            ("Линн", 70000, "Electric Light Orchestra"),
            ("Прокопенко", 14000, "Ukrainian Radio Symphony Orchestra"),
            ("Смирнов", 20000, "Mariinsky Theatre Orchestra"),
            ("Соловьёва", 14000, "Moscow Chamber Orchestra"),
            ("Тэнди", 67000, "Electric Light Orchestra"),
        ]

        self.assertEqual(task_1(self.orchestras, self.musicians), answer)

    def test_task_2(self):

        answer = [
            ("Electric Light Orchestra", 2),
            ("Moscow Chamber Orchestra", 2),
            ("Mariinsky Theatre Orchestra", 1),
            ("Ukrainian Radio Symphony Orchestra", 1),
            ("National Symphony Orchestra of Ukraine", 1),
        ]

        self.assertEqual(task_2(self.orchestras, self.musicians), answer)

    def test_task_3(self):

        answer = {
            "Смирнов": [
                "Electric Light Orchestra",
                "Mariinsky Theatre Orchestra",
                "Moscow Chamber Orchestra",
            ],
            "Карпов": ["Mariinsky Theatre Orchestra", "Moscow Chamber Orchestra"],
        }

        self.assertEqual(task_3(self.orchestras, self.musicians, self.mus_orch), answer)


if __name__ == "__main__":
    unittest.main()
