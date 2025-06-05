print("*****************Welcome To Skynet****************")

import streamlit as st
import random
import time
import requests
import json
import re
import pandas as pd
import math
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def rcp_similarity(ing_list):
    df = pd.read_csv("rcp_dataset_csv.csv",encoding='latin-1')
    #print(df)
    #print(df.columns)
    #print(df['SEARCH_TERM'])
    #print(df['INGREDIENTS'])
    
    df2 = pd.DataFrame(columns=['pos', 'similarity'])
    
    print("Generating Similarity Scores")
    for i in range(0,len(df)-10000):
        #print("Generating Similarity Index - " + str( (i/len(df))*100  )+str("%") )
        text1=ing_list
        text2=df['INGREDIENTS'][i]
        #print(text1)
        #print(text2)
        vector1 = text_to_vector(text1)
        vector2 = text_to_vector(text2)
        cosine = get_cosine(vector1, vector2)
        #print(cosine)
        new_row_df = pd.DataFrame([{'pos':i,'similarity':cosine}])
        #print(new_row_df)
        df2 = pd.concat([df2, new_row_df], ignore_index=True)
        #print(df2)

    df_sorted = df2.sort_values(by='similarity', ascending=False)
    df_sorted = df_sorted.reset_index()
    pos_similar=df_sorted['pos'][0]
    #print(df_sorted)
    #print(pos_similar)
    #print(df.iloc[pos_similar])
    #print(df['SEARCH_TERM'][pos_similar])
    #print(df['RECIPE_NAME'][pos_similar])
    rcp_no=str(df['SEARCH_TERM'][pos_similar])
    rcp_name=str(df['RECIPE_NAME'][pos_similar])
    return rcp_no,rcp_name




def create_spec():
    url = "https://apireg.unileverservices.com/mule-rnd-e-specificationapi-v1/api/specification?plmVer=v1"
    
    
    payload = {
        "SPECCATEGORY": "Substance",
        "SPECTYPE": "ZING_FRAGR",
        "AUTHGROUP": "ZFOD",
        "VALIDITYAREA": "WORLD",
        "PLMUSER": "",
        "KEYDATE": "",
        "SOURCESPEC": "",
        "3PMSPEC": "",
        "TEMPLATEGRP": "",
        "SPECTEMPLATE": "",
        "COPYFROMSPEC": "",
        "IDENTIFIERS": [
            {
            "LANGUAGE": "EN",
            "IDCATEGORY": "ZCID_ID",
            "IDTYPE": "NAM",
            "IDENTIFIER": "BRIEF ID NEW"
            },
            {
            "LANGUAGE": "EN",
            "IDCATEGORY": "Z_PROD",
            "IDTYPE": "NAM",
            "IDENTIFIER": "Spec  003"
            }
        ],
        "PROPERTYTREE": [
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_H_060_ING_A",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_H_CH_130",
                "PHRASEID": "FIRMENICH"
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_135",
                "PHRASEID": "819870 F"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_H_020 ",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_H_CH_50",
                "PHRASEID": "ING"
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_600",
                "PHRASEID": "NO"
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_700",
                "PHRASEID": "NO"
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_800",
                "PHRASEID": "NO"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_H_060_ING",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_H_CH_100",
                "PHRASEID": "KG"
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_110",
                "PHRASEID": "I-S"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_H_100",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_H_100_CHAR",
                "PHRASEID": "01"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_H_030",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_H_CH_60",
                "PHRASEID": 10
                },
                {
                "CHARACTERISTIC": "ZPLM_H_CH_70",
                "PHRASEID": "GAQ"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_GMC_VAT",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_GMC_H_CHAR_010",
                "PHRASEID": "CUST-GMC24749"
                },
                {
                "CHARACTERISTIC": "ZPLM_GMC_H_CHAR_020",
                "PHRASEID": "CUST-GMC24693"
                },
                {
                "CHARACTERISTIC": "ZPLM_GMC_H_CHAR_030",
                "PHRASEID": "CUST-GMC23562"
                },
                {
                "CHARACTERISTIC": "ZPLM_GMC_H_CHAR_040",
                "PHRASEID": "CUST-GMC24028"
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            },
            {
            "PROPTREE": "ZING_FRAGR",
            "VAT": "ZPLM_PML_010",
            "PHRASEDETAILS": [
                {
                "CHARACTERISTIC": "ZPLM_PML_CHAR_010",
                "PHRASEID": 1234
                },
                {
                "CHARACTERISTIC": "ZPLM_PML_CHAR_011",
                "PHRASEID": 4
                },
                {
                "CHARACTERISTIC": "ZPLM_PML_CHAR_012",
                "PHRASEID": "CUST-PML000000000009"
                },
                {
                "CHARACTERISTIC": "ZPLM_PML_CHAR_013",
                "PHRASEID": "MU02278"
                },
                {
                "CHARACTERISTIC": "ZPLM_PML_CHAR_015",
                "PHRASEID": 2
                }
            ],
            "CHARVALUE": "",
            "USERTEXT": "",
            "DOCLINKAGE": ""
            }
        ],
        "REQUESTDETAILS": {
            "PLMUSERMAILID": "Gertjan.Yspeert@unilever.com",
            "REQUESTINGSYSTEM": "TESTSYSTEM",
            "CORRELATIONID": "TESTSYSTEM_BREIFINGTOOL_05082024",
            "INTERFACE": "TESTSYSTEM"
        }
    }
    
    
    
    headers = {"Client_ID":"1124c5a613f54853b315c51a719aa493","Client_Secret":"855531fACcdc4eB08fc1DBBF334B3D30","Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Request successful!")
        return(response.json())  # If the response is in JSON format
    else:
        print(f"Request failed with status code {response.status_code}")
        return(response.text)












# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! What do you want to do today?",
            "Hi there! Do you need help?",
            "Hope you are having a good day! Let me know what you want to do?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("PLM AI Co-Pilot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if prompt == "Hello" or prompt =="Hi" or prompt =="hi":
            response = st.write_stream(response_generator())
            
        elif prompt == "What can you help with?" or prompt == "What can you do?":
            response = f"1. Create a specification in PLM"
            st.write(response)
            response = f"2. Get Recipe Suggestions from PLM"
            st.write(response)
            
            
        elif prompt == "Create a specification" or prompt == "Create a spec" or prompt == "create spec":
            response = f"Enter Spec Type and Auth Group in a Comma Separated single line"
            st.write(response)
 
        elif prompt == "Get Recipe Suggestions" or prompt == "Suggest me a recipe" or prompt == "suggest recipe":
            response = f"Enter Ingredients for the recipe in comma separated single line in the below format"
            st.write(response)
            response = "ingredient{ing_name1,ing_name2,ing_nameN}"
            st.write(response)

 
        elif prompt == "ZING_FRAGR,ZFOD":
            resp=create_spec()
            nested_data=(resp)
            spec_id = nested_data["CREATEDSPECIFICATION"]["SPECIFICATION"]
            response="Specification created in GPR " + spec_id
            st.write(response)
            st.link_button("Go to PLM Specification", "https://plm-regr.unilever.com/sap/bc/ui2/flp/FioriLaunchpad.html?display=#ZSPECIFICATION-display&/GeneralData/SUBSTANCE/"+str(spec_id)+"/0/0")
        
        elif re.match(r"ingredient{.*\}",prompt):
            response=f"Searching for the Closest Recipe based on your criteria"
            st.write(response)
            input_string=prompt
            matches = re.findall(r'{(.*?)}', input_string)
            ing_list=matches[0]
            rcp_no,rcp_name=rcp_similarity(ing_list)
            response=rcp_no
            st.write(response)
            response=rcp_name
            st.write(response)
            #st.write(matches[0])
            st.link_button("Go to PLM Recipe", "https://plm.unilever.com/sap/bc/ui2/flp/FioriLaunchpad.html?display=#ZMNGRCP-display&/GeneralData/"+rcp_no)
            

        
        else:
            response = f"Sorry I cannot understand what you just said!"
            st.write(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    


        
