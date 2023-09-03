import os
import dominate
from dominate.tags import *
doc = dominate.document(title='视频资料')
with doc.head:
    meta(charset="utf-8")
with doc:
    filenames=os.listdir()
    for filename in filenames:
        with audio(src=f'/收录网站/资料库/网友资料库/网友节目/假的路标/{filename}'):
            pass
with open("index.html","w",encoding="utf-8") as f:
    f.write(doc.render())