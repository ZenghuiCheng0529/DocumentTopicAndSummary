import openai

def create_Image(description):
  openai.api_key = "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"

  response = openai.Image.create(
    prompt=description,
    n=1,
    size="1024x1024"
  )

  image_url = response['data'][0]['url']

  return image_url
