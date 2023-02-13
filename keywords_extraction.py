import openai

def extract_keywords(text):
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Extract keywords from this text and split keywords by comma:" + text,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )


    text = response["choices"][0]["text"]
    return str(text)

if __name__ == "__main__":
    extract_keywords("Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.")
