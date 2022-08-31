import ebooklib
from ebooklib import epub


book = epub.read_epub('Python for Data Analysis Data Wrangling with Pandas, NumPy, and IPython (2nd Edition) (Wes McKinney) (z-lib.org).epub')

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print(image)
