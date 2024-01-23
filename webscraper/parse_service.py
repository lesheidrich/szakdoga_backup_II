

# def table_2_df(url, session=None, http=None, https=None):
#     response_text = request_sauce_text(url, session, http, https)
#     soup = BeautifulSoup(response_text, 'html.parser')
#     table_html = soup.find('table', class_='tablesaw')
#     table_str = str(table_html)
#     mock_html = StringIO(table_str)
#
#     return pd.read_html(mock_html)