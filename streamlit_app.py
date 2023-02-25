import openai
import re
import streamlit as sl

openai.organization = sl.secrets["organization"]
openai.api_key = sl.secrets["key"]

temp = sl.sidebar.slider("Craziness of ideas",0.0,1.0,0.5)

originating_text = sl.text_area("enter starting text")
scenario = sl.text_input("Enter prompt'")

go = sl.button("do it!")

if go:
    sl.sidebar.text("Drafting scenario")

    sl.write(scenario+originating_text)

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=scenario+originating_text,
      temperature=temp,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    sl.write(response)
    AI_scenario = response["choices"][0]["text"]

    sl.write(AI_scenario)

    lines = [line.strip() for line in AI_scenario.splitlines() if line.strip()]
    lines = [re.sub("^\d+\.", "", line) for line in lines]
    comma_separated_string = ", ".join(lines)

    sl.write(comma_separated_string)
