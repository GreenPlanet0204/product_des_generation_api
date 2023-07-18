import openai
import time

# using gpt-3.5 model
openai.api_key = "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"

# Interact with Openai Api GPT-3.5 Model to generate answers to your questions.
def interact_with_ChatGPT(question):
    messages = [({
        "role" : "user",
        "content" : question
    })]
    while True:
        try:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response.choices[0].message.content
            break
        except Exception as e:
            print("Error:", e)
            print("Retrying in 5 seconds...")
            time.sleep(5)
    return reply


# The language list that GPT can translate.
LanguageList = {'English', 'Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Dutch', 'Swedish', 'Norwegian', 'Finnish', 'Danish', 'Arabic', 'Chinese', 'Japanese', 'Korean', 'Russian'}



def WhatLanguage(text):
    WhatLanguagePrompt = "What language is the following text in?"\
    "{'English', 'Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Dutch', 'Swedish', 'Norwegian', 'Finnish', 'Danish', 'Arabic', ' Chinese', 'Japanese', 'Korean', 'Russian'} if it is, say it or I don't know."\
    "I gave an example below."\
    "Human: Ich gehe zur Schule."\
    "AI: German"\
    "Human: أنا ذاهب إلى المدرسة."\
    "AI: Arabic"\
    "Human: jfijfj jjesie."\
    "AI: I don't know."\
    f"Human: {text}"\
    "AI:"
    return interact_with_ChatGPT(WhatLanguagePrompt)



def Translator(source, target, text):
    TranslatePrompt = f'Translate next {source} text to {target}.\n'\
    'If you can not translate it directly, translate it into English first, then translate it back into the target language and say it.\n'\
    'No explanation needed when answering.\n'\
    'Only translated text are required.\n'\
    'Do not use unnecessary words such as "Sure, " and "As an AI language model...".\n'\
    'Keep the output format.\n'\
    f'{text}'
    return interact_with_ChatGPT(TranslatePrompt)



def OriginalTranslator(target, text):
    source = str(WhatLanguage(text))
    if source == "I don't know.":
        return text
    return Translator(source, target, text)


# info = {
#     'title' : "Micro-Pop Microwave Popcorn Popper",
#     'productInformation' : "Ecolution Patented, with Temperature Safe Glass",
#     'additionalKeyword' : ['3-in-1 Lid Measures Kernels', 'Melts Butter', 'Made Without BPA', 'Dishwasher Safe'],
#     'numberOfWords' : "5"
# }

def GenerateProductDescription(information):
    question = f'The name of the product is {information["title"]}, the currently known information about this product is {information["information"]}, and the additional keyword is {",".join(information["keywords"])}.'\
    f'Create a professional and artistic description of this product in {information["number"]} words.'
    return interact_with_ChatGPT(question)



