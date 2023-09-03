import os
import dominate
from dominate.tags import *
from dominate.util import *
doc = dominate.document(title='网友节目')
with doc.head:
    meta(charset="utf-8")
with doc:
    filenames=os.listdir()
    for filename in filenames:
        if not filename.endswith("py") and not filename.endswith("html"):
            with audio(src=f'/收录网站/资料库/网友资料库/网友节目/假的路标/{filename}',controls="true"):
                pass
with open("index.html","w",encoding="utf-8") as f:
    f.write(doc.render())