# -*- coding: utf-8 -*-
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maiziedu_website.settings")

import django

django.setup()

import re
from mz_lps.models import Quiz

def change_quiz_itemlist():
    quizs = Quiz.objects.filter(id__startswith=836000098)
    pattern = r'<.*?="(?P<item_option>\w)">\w: (?P<item_list>.*?)<.*?>'
    repl = "['" + "\g<item_option>" + "', '" + "\g<item_list>" + "'],"
    for quiz in quizs:
        try:
            print quiz.item_list
            if re.search(pattern, quiz.item_list):
                # print items
                item_list = "[" + re.sub(pattern, repl, quiz.item_list) + "]"
                # quiz.item_list = item_list
                # quiz.save()
                print item_list
        except UnicodeEncodeError:
            continue


def test():
    pattern = r'>(?P<item_list>.*?)nt \*p = &a;  p = 20;<'
    pattern = r'>(?P<item_list>.*?)<'
    string = '>nt *p = &a;  p = 20;<'
    repl = "\g<0>"
    repl = "a"
    if re.search(pattern, string):
        item = re.sub(pattern, repl, string)
        print item


if __name__ == "__main__":
    change_quiz_itemlist()
    # test()