from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Cody has heard about a cool new Magic: The Gathering deckbuilding site.
        # He navigates to the homepage to check it out.
        self.browser.get('http://localhost:8000')

        # He notices the title and header mention the Tolarian Playground.
        self.assertIn('Tolarian Playground', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Tolarian Playground', header_text)

        # He is invited to create a new deck with the deckbuilder.

        # He types "The Dark Knight" into a text box as the name of his new deck.

        # When he hits enter, the page updates, and now it lists "The Dark Knight"
        # as a deck in a deck list table.

        # There is still a text box inviting him to add another deck. He enters
        # "Use Your Illusion."

        # The page updates again and now shows both decks in a deck list table.

        # Cody wonders whether the site will remember his decks. The he sees that
        # the site has generated a unique UTL for her. There is some explanatory
        # test to that effect.

        # Satisfied, he goes back to sleep.
