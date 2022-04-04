from unittest import TestCase
from File import frame_for_met, transcription2


class DNAStringTest(TestCase):

    def test_frame_for_met(self):
        self.assertEqual(
            ['aug', 'acu', 'gua', 'cca', 'gga'],
            frame_for_met("atgactgtaccagga")
        )
        self.assertEqual(
            ['aug', 'acu', 'gua', 'cca', 'gg'],
            frame_for_met("gatgactgtaccagga")
        )
        self.assertEqual(
            ['aug', 'acu', 'gua', 'cca', 'g'],
            frame_for_met("tgatgactgtaccagt")
        )
        self.assertEqual(
            ['ucg', 'aug', 'acu', 'gua', 'cca', 'gga'],
            frame_for_met("tcgatgactgtaccaggatt")
        )
        self.assertEqual(
            None,
            frame_for_met("aaagttacc")
        )
