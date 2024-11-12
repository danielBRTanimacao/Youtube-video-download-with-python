from re import compile

YOUTUBE_REGEX = compile(
    r'(https?://)?(www\.)?'
    r'(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)'
    r'([\w-]{11})'
)

def url_validator(url: str) -> bool:
    if YOUTUBE_REGEX.match(url):
        return True
    return False
