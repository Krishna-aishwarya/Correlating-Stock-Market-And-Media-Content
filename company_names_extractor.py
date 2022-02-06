from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Model Id
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

ner_results = ""
def get_companies_and_stocks_names(tweet_content):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(tweet_content)
    ner_companies_n_stocks = []
    for ner_dict in ner_results:
        if "ORG" in ner_dict['entity']:
            ner_companies_n_stocks.append(ner_dict['word'])
            
            
            
    # print(ner_companies_n_stocks)
    return ner_companies_n_stocks
    