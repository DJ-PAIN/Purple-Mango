def GetImg(img_id, FileType, width=None, height=None, cropSquare=False):
  with open(f"images/{img_id}.{FileType}", "rb") as image:
    image = image.read()
    