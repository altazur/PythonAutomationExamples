import asyncio
from pyppeteer import launch

async def test_ddg_first_result():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://duckduckgo.com')
    await page.click('#search_form_input_homepage')
    await page.keyboard.type('anime')
    await page.click('#search_button_homepage') # This line seems doesn't work at all
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(test_ddg_first_result())
