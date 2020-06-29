from scrapy.cmdline import execute

import sys
import os

p = os.path.dirname(os.path.abspath(__file__))
print(p)
# execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
execute(["scrapy", "crawl", "chinatax_inquiries"])
# execute(["scrapy", "crawl", "chinatax_hubei"])
# execute(["scrapy", "crawl", "chinatax_guangdong"])