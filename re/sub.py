from django.test import TestCase
import re

# Create your tests here.

# content = '<p><img alt="temp.png" src="/group/uploads/Entity/2015/11/maiz-61_20151117104605_497.png" title=""/></p>'
content = '<p><img src="/group/uploads/Entity/2015/11/maiz-61_20151117104605_497.png" title="" alt="temp.png"/></p><p><img alt="temp.png"/></p>'
# pattern = re.compile('(?<=<img alt=").*?(?=\..*?")', re.S)
repl = 'temp1'
items0 = re.sub(r'(<img .*?alt=").*?(?=\..*?"/>)', "\g<1>repl", content)
# items0 = re.sub(r'(<img .*?alt=").*?(?=\..*?"/>)', "\g<1>"+repl, content)
# items0 = re.sub(r'(<img .*?alt=").*?(?=\..*?"/>)', "\g<1>%s" %repl, content)
print items0
