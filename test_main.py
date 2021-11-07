import unittest
import extractor


class TumblDownTestCase(unittest.TestCase):
    def test_extract_tumblr_image_links(self):
        # test single image
        self.assertEqual(extractor.extract_tumblr_images("https://kiminukii.tumblr.com/post/656015203710976000"),
                         [
                             "https://64.media.tumblr.com/656c1b0e9008c5daa813c1530c7b4610/f994f9125257a26d-3f/s2048x3072/4a9f313d9f73f21bcc53facda98ad2fb681530c2.jpg"])

        # test multiple images
        self.assertEqual(
            extractor.extract_tumblr_images("https://zandraart.tumblr.com/post/662604327475707904/jellies"),
            [
                "https://64.media.tumblr.com/7ce02d1c06accb2db65ffae410592807/b718ff429b370a25-d4/s640x960/dff9bb177424a46c598be9768abf6d7ace8276af.png",
                "https://64.media.tumblr.com/8173aec87f24dad743c8607721c5fe06/b718ff429b370a25-c4/s640x960/f64312a68a8f8999dc3efad84b7777f8f62db00a.png",
                "https://64.media.tumblr.com/c95be592fed81a52e597f524930207f8/b718ff429b370a25-36/s640x960/189ff2d22791c6110e2d2bbf9c0c8f5338b3a786.png"])

        # test single image without viewer
        self.assertEqual(
            extractor.extract_tumblr_images("https://maruti-bitamin.tumblr.com/post/663149423546777600/sun-sea"),
            [
                "https://64.media.tumblr.com/bdf1a1b5dd22c7bb961452c86994e9bb/f4a9103f1a6f2e3c-6c/s500x750/d7d98b5231495cdd5f3746563f957862640207d9.jpg"])

        # test video
        self.assertEqual(extractor.extract_tumblr_images("https://simonalkenmayer.tumblr.com/post/664168073150988288"),
                         [])

        # test post without media
        self.assertEqual(extractor.extract_tumblr_images(
            "https://stuckwith-harry.tumblr.com/post/640948223894290432/lesser-movies-than-mamma-mia-2008-wouldve-made"),
                         [])

        # test non-posts and non-URLs
        with self.assertRaises(ValueError):
            extractor.extract_tumblr_images("https://temmiechang.tumblr.com/")
        with self.assertRaises(ValueError):
            extractor.extract_tumblr_images("https://www.tumblr.com/")
        with self.assertRaises(ValueError):
            extractor.extract_tumblr_images("https://www.youtube.com/")
        with self.assertRaises(ValueError):
            extractor.extract_tumblr_images("I am a teapot.")


if __name__ == '__main__':
    unittest.main()