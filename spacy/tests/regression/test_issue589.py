# coding: utf-8
from __future__ import unicode_literals

from ...vocab import Vocab
from ...tokens import Doc

import pytest


def test_issue589():
    vocab = Vocab()
    vocab.strings.set_frozen(True)
    doc = Doc(vocab, words=['whata'])
