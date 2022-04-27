from django import template
import re

register = template.Library()

blacklist = [
    "and",
    "for",
    "have",
    "bee",
    "the",
    "their",
]


def repl(match):
    word = match.group(0)
    return word[0] + "*" * len(word[1:])


@register.filter()
def censor(text: str) -> str:
    blacklist_capital = r"\b|\b".join(list(map(str.capitalize, blacklist)))
    blacklist_lower = r"\b|\b".join(list(map(str.lower, blacklist)))
    pattern = re.compile(r"\b" + blacklist_capital + r"\b|\b" + blacklist_lower + r"\b")
    return pattern.sub(repl, text)
