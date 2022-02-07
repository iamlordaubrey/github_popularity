INVALID_URLS = [
    'https://www.google.com/',
    'http://github.com/vuejs',
    'localhost',
    'a',
    '1'
]

VALID_URLS = [
    'https://github.com/freeCodeCamp/freeCodeCamp',
    'https://github.com/sindresorhus/awesome',
    'https://github.com/vuejs/vue',
]

INVALID_OPERANDS = [
    ('a', 3),
    (None, 2),
    ([3, True, 'a'], 5),
]

VALID_OPERANDS = [
    (1, 3),
    [400, 70],
]

OPERANDS_AND_SCORE_LIST = [
    (1, 2, 5),
    (400, 70, 540),
    (1000, 1000, 3000),
]
