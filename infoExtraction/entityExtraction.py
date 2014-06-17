import keywordExtraction as ke

def identifyPersons(text, entities, persons):
    '''
    Given entities already found in text, determine their relation to the child or case.
    Done by finding relationship keyword in sentence that is closest to entity mention.
    :param text: target text
    :param entities: list of Person entities
    :param persons: list of people relationships
    :return: List of person, relation tuples
    '''
    relations = []
    for entity in entities:
        relation = findClosestRelation(text, entity, persons)
        relations.append([entity, relation])
    return relations

def findClosestRelation(text, entity, persons):
    globalMin = ["", 100]
    contexts = ke.getContext(entity, text)
    for context in contexts:
        words = context.lower()
        localMin = len(words)
        place = words.find(entity)
        for person in persons:
            if person in words:
                i = words.find(person)
                if abs(place-i) < localMin and abs(place-i) < globalMin[1]:
                    globalMin[0] = person
    if globalMin[0] is not "":
        return globalMin[0]
    else:
        return "unknown"

#organize entities by type
def org_entities_stan(ents):
    '''
    Organize entities by type
    :param ents:
    :return:
    '''
    entDict = dict()
    for ent, tag in ents:
        if tag in entDict:
            entDict[tag].append(ent)
        else:
            entDict[tag] = [ent]
    return entDict

def get_model_name(default= True):
    if not default:
        return '/classifiers/english.muc.7class.distsim.crf.ser.gz'
    else:
        return '/classifiers/english.all.3class.distsim.crf.ser.gz'

def extract_entities_stanford(sample, stanfordPath, model):
    from nltk.tag.stanford import NERTagger
    st = NERTagger(stanfordPath + get_model_name(model),
                   stanfordPath + '/stanford-ner-2014-01-04.jar')

    entity_names = st.tag(sample.split())

    entities = []
    for entity, tag in entity_names:
        if cmp(tag, "O") != 0:
            entities.append([entity, tag])

    return entities

def extract_persons_stanford(sample, stanfordPath, model):
    from nltk.tag.stanford import NERTagger
    import operator
    st = NERTagger(stanfordPath + get_model_name(model),
                   stanfordPath + '/stanford-ner-2014-01-04.jar')

    entity_names = st.tag(sample.split())

    entity_count = {}
    for entity, tag in entity_names:
        if cmp(tag, "PERSON") == 0:
            if entity in entity_count:
                entity_count[entity] += 1
            else:
                entity_count[entity] = 1

    sorted_occurrences = sorted(entity_count.iteritems(), reverse=True, key=operator.itemgetter(1))
    return sorted_occurrences

# From Edmon's agatha.py
def extract_entities_nltk(sample):
    import nltk
    import operator
    sentences = nltk.sent_tokenize(sample)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)

    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))

    #create a map with entity,count count representing
    # the number of occurrences of an entity
    entity_count = {}
    for entity in entity_names:
        if entity in entity_count:
            entity_count[entity] += 1
        else:
            entity_count[entity] = 1

    sorted_occurrences = sorted(entity_count.iteritems(), reverse=True, key=operator.itemgetter(1))
    return sorted_occurrences

# From Edmon's agatha.py
def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]), )
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names
