import re
from unidecode import unidecode

def slugify(value):
  value = unidecode(value).lower()
  value = re.sub(r'[^\w\s-]', '-', value)
  value = re.sub(r'[-\s]+', '-', value)
  return value.strip('-')