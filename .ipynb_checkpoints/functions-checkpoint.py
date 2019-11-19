import pickle
filename = 'finalized_model_eng.sav'
filename1 = 'finalized_model_afr.sav'

bayes = pickle.load(open(filename, 'rb'))
bayes1 =pickle.load(open(filename1, 'rb'))
def namer(name):
    B = bayes.prob_classify(extract_gender_features("Mungai"))
    B1 =bayes.classify(extract_gender_features(name))
    U=[B.prob("female"),1-B.prob("female")]
    return (B1,max(U))
def namer1(name):
    B = bayes1.prob_classify(extract_gender_features("Mungai"))
    B1 =bayes1.classify(extract_gender_features(name))
    U=[B.prob("female"),1-B.prob("female")]
    return (B1,max(U))
def extract_gender_features(name):
    name = name.lower()
    features = {}
    features["suffix"] = name[-1:]
    features["suffix2"] = name[-2:] if len(name) > 1 else name[0]
    features["suffix3"] = name[-3:] if len(name) > 2 else name[0]
    #features["suffix4"] = name[-4:] if len(name) > 3 else name[0]
    #features["suffix5"] = name[-5:] if len(name) > 4 else name[0]
    features["suffix6"] = name[-6:] if len(name) > 5 else name[0]
    features["prefix"] = name[:1]
    features["prefix2"] = name[:2] if len(name) > 1 else name[0]
    features["prefix3"] = name[:3] if len(name) > 2 else name[0]
    features["prefix4"] = name[:4] if len(name) > 3 else name[0]
    features["prefix5"] = name[:5] if len(name) > 4 else name[0]
    features["wordLen"] = len(name)
    return features