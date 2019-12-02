# TG_essay_bot
For MLH local hack day

 - task: paraphrasing - synonym or structure paraphrase
 - implementation: telegram bot

TO RUN:
 - installing spacy, tensorflow, python
 - run paraphrase.py it will ask for input or you can simply use as a function, docstring is listed
 after installing spacy:
 - python -m spacy download en_core_web_sm
 - python -m spacy download en<br>
Link to a model:
https://drive.google.com/file/d/18uOQsosF4uVGvUgp6pB4BKrQZ1FktlmM/view<br>
Link to a pickle packages:
https://drive.google.com/uc?id=1l2liCZqWX3EfYpzv9OmVatJAEISPFihW&export=download<br>
#Algorithm of the paraphrasing <br>
Sentence -> LSTM-encoder->LSTM-decoder->Synonym changing->LSTM-encoder->LSTM-decoder -> Paraphrased sentence
