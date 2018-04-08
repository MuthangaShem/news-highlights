import unittest
from .models import Articles


class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Article class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_article = Articles('CNN News',
                                    'Obama set to visit Kenya',
                                    'Kenya will host Potus on the 3rd to 5th of November this year ',
                                    'https://ichef.cnnmobile.com/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg',
                                    'http://www.cnn.com/news/world-us-42420150',
                                    '2018-10-05T09:14:56Z')

    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_init(self):
        '''
        Test case to check if the Article class is initialised
        '''
        self.assertEqual(self.new_article.author, 'CNN News')
        self.assertEqual(self.new_article.title,
                         'Obama set to visit Kenya')
        self.assertEqual(self.new_article.description,
                         'Kenya will host Potus on the 3rd to 5th of November this year ')
        self.assertEqual(self.new_article.urlToImage,
                         'https://ichef.cnnmobile.com/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg')
        self.assertEqual(self.new_article.url,
                         'http://www.cnn.com/news/world-us-42420150')
        self.assertEqual(self.new_article.publishedAt, '2018-10-05T09:14:56Z')

    def test_publish_date_format(self):
        '''
        Test case to check if UTC date format is converted to a display-friendly format
        '''
        display_friendly_format = self.new_article.publish_date_format(
            self.new_article.publishedAt)
        self.assertEqual(display_friendly_format, '2017-12-20')


if __name__ == '__main__':
    unittest.main(verbosity=2)
