import os
from openai import OpenAI

client = OpenAI()

moderation = client.moderations.create(
  input="Kill 'em all!",
)

print(moderation.results)

## OUTPUT ##
# [Moderation(
#     categories=Categories(
#         harassment=False, 
#         harassment_threatening=False, 
#         hate=False, 
#         hate_threatening=False, 
#         illicit=False, 
#         illicit_violent=True, 
#         self_harm=False, 
#         self_harm_instructions=False,
#         self_harm_intent=False, 
#         sexual=False, 
#         sexual_minors=False, 
#         violence=True,
#         violence_graphic=False, 
#         harassment_threatening=False, 
#         hate_threatening=False, 
#         illicit_violent=True, 
#         self_harm_intent=False, 
#         self_harm_instructions=False, 
#         self_harm=False, 
#         sexual_minors=False, 
#         violence_graphic=False, 
#     ),
#     category_applied_input_types=CategoryAppliedInputTypes(
#         harassment=['text'], 
#         harassment_threatening=['text'], 
#         hate=['text'], 
#         hate_threatening=['text'], 
#         illicit=['text'], 
#         illicit_violent=['text'], 
#         self_harm=['text'], 
#         self_harm_instructions=['text'], 
#         self_harm_intent=['text'], 
#         sexual=['text'], 
#         sexual_minors=['text'], 
#         violence=['text'], 
#         violence_graphic=['text'], 
#         harassment_threatening=['text'], 
#         hate_threatening=['text'], 
#         illicit_violent=['text'], 
#         self_harm_intent=['text'], 
#         self_harm_instructions=['text'], 
#         self_harm=['text'], 
#         sexual_minors=['text'], 
#         violence_graphic=['text']
#     ), 
#     category_scores=CategoryScores(
#         harassment=0.3067387800737454, 
#         harassment_threatening=0.2869254730683408, 
#         hate=0.03585116712307011, 
#         hate_threatening=0.03602107325660055, 
#         illicit=0.2658481678739891, 
#         illicit_violent=0.1777403575821696, 
#         self_harm=0.0005506238275354633,
#         self_harm_instructions=0.00026633108675453717, 
#         self_harm_intent=0.0003318044306304943, 
#         sexual=4.8785712278226595e-05, 
#         sexual_minors=6.40200641038395e-06, 
#         violence=0.9440160808816858, 
#         violence_graphic=0.0024141732699500536, 
#         harassment_threatening=0.2869254730683408, 
#         hate_threatening=0.03602107325660055, 
#         illicit_violent=0.1777403575821696, 
#         self_harm_intent=0.0003318044306304943, 
#         self_harm_instructions=0.00026633108675453717, 
#         self_harm=0.0005506238275354633, 
#         sexual_minors=6.40200641038395e-06, 
#         violence_graphic=0.0024141732699500536
#     ), flagged=True\
# )]

