from DDGPage import SearchHelper

def test_ddg_first_result(get_driver):
    ddg_page = SearchHelper(get_driver)
    ddg_page.url_open("https://duckduckgo.com")
    ddg_page.enter_search("anime")
    ddg_page.click_search_button()
    assert 'anime' in ddg_page.get_first_result_text()
