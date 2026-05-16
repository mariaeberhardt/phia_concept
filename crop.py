from PIL import Image
import os

src = '/Users/aniketharvind/.claude/image-cache/55e0cfdd-8236-4d69-b4ca-6e7e2e2a9e92/1.png'
out = '/Users/aniketharvind/Desktop/Maria_Designs/pinpoint/images'
os.makedirs(out, exist_ok=True)

img = Image.open(src)
print('Size:', img.size)

# Save full screen content (inside phone frame) for reference
# Phone screen approximate bounds in original 1448x1086 image
screen = img.crop((487, 32, 957, 1058))
screen.save(f'{out}/_screen_full.png')
print('Screen size:', screen.size)

# Hero collage area (the big image at top)
hero = img.crop((505, 145, 945, 487))
hero.save(f'{out}/hero.png')
print('Hero size:', hero.size)

# Individual product thumbnails - approximate locations
# Product 1: Polo Ralph Lauren Cardigan
p1 = img.crop((535, 549, 605, 625))
p1.save(f'{out}/p1_cardigan.png')

# Product 2: Mango skirt
p2 = img.crop((535, 631, 605, 707))
p2.save(f'{out}/p2_skirt.png')

# Product 3: Rejuly cosmetic case
p3 = img.crop((535, 713, 605, 789))
p3.save(f'{out}/p3_case.png')

# Product 4: Dolce sunglasses
p4 = img.crop((535, 795, 605, 871))
p4.save(f'{out}/p4_sunglasses.png')

print('Done')
