from PIL import Image
import sys

if len(sys.argv) != 3:
    print("USEAGE:")
    print("img2ico 入力先 出力先")
    sys.exit(1)

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

img = Image.open(input_file_name)
img.save(output_file_name, format="ICO", size=[(32, 32)])

