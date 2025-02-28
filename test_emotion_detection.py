from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for 'I am glad this happened' (Expecting 'joy' as the dominant emotion)
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Test case for 'I am really mad about this' (Expecting 'anger' as the dominant emotion)
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Test case for 'I feel disgusted just hearing about this' (Expecting 'disgust' as the dominant emotion)
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        # Test case for 'I am so sad about this' (Expecting 'sadness' as the dominant emotion)
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        # Test case for 'I am really afraid that this will happen' (Expecting 'fear' as the dominant emotion)
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
