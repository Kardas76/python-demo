In order to provide smaller size, list all packages:
pip list
and exclude them in .spec file in 'excludes'

Find:
(^\S+)(.+)
Replace:
'$1'

Find:
\n
Replace:
, 


Do NOT exclude:

numpy
Pillow
unicodedata2 