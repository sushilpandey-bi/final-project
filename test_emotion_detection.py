import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am so happy and excited today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am extremely angry right now!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("This makes me feel very sad and depressed.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am scared and terrified of this!")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()
