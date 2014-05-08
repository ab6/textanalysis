#organize entities by type
def org_entities_stan(ents):
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

    entity_names = st.tag(sample)

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
