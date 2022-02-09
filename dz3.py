class Url:
    def __init__(self, scheme: str = '', authority: str = '', path=None, query=None, fragment: str = ''):
        self.scheme = scheme
        self.authority = authority
        self.path: list = path
        self.query: dict = query
        self.fragment = fragment

        self.link = ''
        if self.scheme != '':
            self.link += self.scheme + '://'

        if self.authority != '':
            self.link += self.authority

        if self.path is not None:
            self.link += '/' + '/'.join(self.path)

        if self.query is not None:
            self.link += '?'
            for key, value in self.query.items():
                self.link += str(key) + '=' + str(value) + '&'
            self.link = self.link[:-1]

        if self.fragment != '':
            self.fragment = '#' + self.fragment

        self.link += self.fragment

    def __str__(self):
        return self.link

    def __eq__(self, other):
        return self.link == other


class HttpsUrl(Url):

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('wikipedia.org', path, query, fragment)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
