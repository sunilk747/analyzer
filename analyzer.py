'''
Implementation of Naive Bayes algorithm to classify tweeets into categories
'''

class analyzer:

    def __init__(self):
        
        '''
        self.trivial : list, stores the words which should not be considered for categorizaton.
        self.category : dict, stores the total no. of positive and negative tweets.
        self.words : dict, it is of the form {word:{positive:value, negative:value}}.
        self.total : stores the total no. of tweets.
        ''' 
        self.trivial = ['i', 'the', 'then', 'on', 'and', 'also', 'very', 'do', 'which', 'by', 'a']
        self.category = {}
        self.words = {}
        self.total = 0.0

    def train(self, text, category):
        
        '''
        method to train the algorithm based on which it will classify the tweets into categories.
        '''

        if category == '0':
            try:
                self.category['0'] += 1.0
            except:
                self.category['0'] = 1.0
        else:
            try:
                self.category['1'] += 1.0
            except:
                self.category['1'] = 1.0
        
        text = text.lower()    
        words = text.split()
        for word in words:
            if word in self.trivial:
                continue
        
            else:
                try:
                    if category == '0':
                        try:
                            self.words[word]['0'] += 1.0
                        except:
                            self.words[word]['0'] = 1.0

                    if category == '1':
                        try:
                            self.words[word]['1'] += 1.0
                        except:
                            self.words[word]['1'] = 1.0

                except:
                    self.words[word] = {}
                    if category == '0':
                        self.words[word]['0'] = 1.0
                    if category == '1':
                        self.words[word]['1'] = 1.0

        self.total += 1.0

    def classify(self, text):
        
        '''
        classifies a tweet into a category.
        '''

        text = text.lower()
        text = text.replace('(',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('---',' ').replace('!',' ').replace(')',' ')
        words = text.split()
    
        prob_cats = []
        for word in words:
            if word in self.trivial or word not in self.words:
                continue
    
            try:
                temp1 = 1.0
                temp1 *= self.words[word]['0']/self.category['0']  
        
                temp2 = 1.0
                temp2 *= self.words[word]['1']/self.category['1'] 
            except:
                continue

        prob_cats.append([temp1, 'Negative'])
        prob_cats.append([temp2, 'Positive'])

        return max(prob_cats)[1] 

    def train_from_data(self):

        '''
        A saved data set is used for the purpose of training the algorithm.
        '''

        fi = open('corpus/data.txt', 'rb')
        for lines in fi:
            lines = lines.replace('(',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('---',' ').replace('!',' ').replace(')',' ')
            li = lines.strip('\n').split('\t')
            self.train(li[1], li[0])

        fi.close()

if __name__ == '__main__':

    c = analyzer()
    c.train_from_data()
    print c.classify('I love playing games')
