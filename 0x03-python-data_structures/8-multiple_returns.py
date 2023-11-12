#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        n = len(sentence)
        ch = sentence[0]
        return (n, ch)
    else:
        return (0, None)
