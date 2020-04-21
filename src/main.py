import boto3
import os
import random
import string
import botocore
import base64
import os
import sys
from word_search_puzzle.algorithms import create_panel
import RAKE

DEBUG = True

def print_panel(panel):
    """
    Get a serializable panel

    :param panel: The word search puzzle panel.
    """
    outstr = ''
    for r in range(panel.height()):
        for c in range(panel.width()):
            outstr += panel[r, c] + ' '
        outstr += '\n'
    return outstr


def handler(event, context):
  print(event)
  text = event.get("text")
  maxwords = int(event.get("maxwords"))
  width = event.get("width")
  height = event.get('height')
  rake = RAKE.Rake(RAKE.SmartStopList())
  phraseList = rake.run(text, maxWords = 1, minFrequency = 1)
  print(phraseList)
  phraseListLen = len(phraseList)
  if phraseListLen < maxwords:
      maxwords = phraseListLen
  slicedTuples = phraseList[:maxwords]
  sliced = [x[0] for x in slicedTuples]
  result = create_panel(height=15, width=15, words_value_list=sliced)
  return { "result": print_panel(result.get('panel')), "words": sliced, }
