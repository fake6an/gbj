from gbj_intent import get_intent
from gbj_entity import get_entity
from gbj_seq2seq import get_seq2seq
from gbj_image import get_image

from gbj_scenario import dust
from gbj_scenario import weather
from gbj_scenario import restaurant
from gbj_scenario import travel
from gbj_scenario import attraction

from tokenizer import tokenize
from util.spell_checker import fix

# from gensim.models.word2vec import Word2Vec



#CONFIG
get_entity = get_entity()
get_seq2seq = get_seq2seq()

print("###### application.py ######")



def run(pdata, state, type):
    
    if type == "nlp":
        print('\n\nInput Questuon', end='\n')
        speech = preprocess(pdata)
        print("\n\nPreprocessed >> " + speech, sep="", end="\n\n")
        
        intent = get_intent(speech)
        print("Intent >> " + intent, sep="", end="\n\n")
        
        entity = get_entity.predict(speech.split(' '))
        print("Entity >> " + str(entity), sep="", end="\n\n")

        answer = scenario(intent, entity, state, speech)
            
    else:
        answer = get_image(pdata)


    return answer



def preprocess(speech):
    speech = fix(speech)
    speech = tokenize(speech)
    speech = fix(speech)

    return speech



def scenario(intent, entity, state, speech):
    if intent == "먼지":
        return dust(entity, state, None)
    
    elif intent == "날씨":
        return weather(entity, state, None)

    elif intent == "맛집":
        return restaurant(entity, state, None)
    
    elif intent == "여행지":
        return travel(entity, state, None)
    
    elif intent == "관광지":
        return attraction(entity, state, None)
    
    else:
        return get_seq2seq.seq2seq_run(speech)



# 테스트
# run('바다가 유명한 여행지 알려주라')
# a = ['분위기', '좋은', '카페'], ['O', 'O', 'LOCATION']
# entity = tuple(a)
# test = scenario("맛집", entity)
# print(test)