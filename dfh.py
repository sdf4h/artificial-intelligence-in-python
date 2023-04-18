import os
import openai
import base64
import time
import argparse
a = input('введите что хотите написовать: ')
print('нужно ввести запрос на англиском языке это важно')
# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prompt", help="Text to image prompt:", default=a)
parser.add_argument("-n", "--number", help="Number of images generated", default=1)
parser.add_argument("-s", "--size", help="Image size: 256, 512 or 1024", default=256)

# Read arguments from the command line
args = parser.parse_args()

openai.api_key = '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'

res = openai.Image.create(
  prompt=args.prompt,
  n=int(args.number),
  size=f'{args.size}x{args.size}',
  response_format="b64_json"
)

for i in range(0, len(res['data'])):
    b64 = res['data'][i]['b64_json']
    filename = f'image_{int(time.time())}_{i}.png'
    print('Saving file ' + filename)
    with open(filename, 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))