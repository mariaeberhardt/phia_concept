from PIL import Image
src = '/Users/aniketharvind/.claude/image-cache/55e0cfdd-8236-4d69-b4ca-6e7e2e2a9e92/1.png'
img = Image.open(src)
# Zoom into Polo price area
crop1 = img.crop((615, 580, 760, 615)).resize((580, 140))
crop1.save('/Users/aniketharvind/Desktop/Maria_Designs/pinpoint/images/_zoom_polo.png')
crop2 = img.crop((615, 663, 760, 695)).resize((580, 128))
crop2.save('/Users/aniketharvind/Desktop/Maria_Designs/pinpoint/images/_zoom_mango.png')
crop3 = img.crop((615, 745, 760, 776)).resize((580, 124))
crop3.save('/Users/aniketharvind/Desktop/Maria_Designs/pinpoint/images/_zoom_case.png')
crop4 = img.crop((615, 824, 760, 858)).resize((580, 136))
crop4.save('/Users/aniketharvind/Desktop/Maria_Designs/pinpoint/images/_zoom_dolce.png')
print('done')
