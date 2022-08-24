import string
import re
import math
from collections import defaultdict

class msgDetector(object):
    def clean(self, s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)
    def tokenize(self, text):
        text = self.clean(text).lower()
        return re.split("\W+", text)
    def get_word_counts(self, words):
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0.0) + 1.0
        return word_counts

    # tokenize comment into word list, and then make word frequency list per each class(means self.target_names right down)
    def fit(self, X, Y):
        self.target_names = ["adjustedszz_bugfix", "issueonly_bugfix", "testchange_javacode", "documentation_technicaldept_add", 
                            "refactoring_codebased", "documentation_technicaldept_remove", "refactoring_keyword","documentation_javainline",
                            "documentation_javadoc", "issueonly_featureadd", "validated_bugfix"]
        
        self.num_messages = {}
        self.log_class_priors = {}
        self.word_counts = {}
        self.vocab = set()
        n = len(X)
        # print("Y", len(Y))
        
        # to make format per each class
        for class_num, class_name in enumerate(self.target_names):
            print(class_name, sum(1 for one_hot_index in Y if one_hot_index == class_num))
            self.num_messages[class_name] = sum(1 for one_hot_index in Y if one_hot_index == class_num)
            self.log_class_priors[class_name] = math.log(self.num_messages[class_name] + 1 / n)
            self.word_counts[class_name] = {}
        
        # count word frequency per class
        for commit_msg, class_index in zip(X, Y):
            c = self.target_names[class_index]
            counts = self.get_word_counts(self.tokenize(commit_msg))
            for word, count in counts.items():
                if word not in self.vocab:
                    self.vocab.add(word)
                if word not in self.word_counts[c]:
                    self.word_counts[c][word] = 0.0
                self.word_counts[c][word] += count
                
                
    def predict(self, X):
        result = []
        for x in X:
            counts = self.get_word_counts(self.tokenize(x))
            self.target_scores = { class_name: 0 for class_name in self.target_names }
            
            for word, _ in counts.items():
                if word not in self.vocab: continue
                
                # add Laplace smoothing(+1) to prevent "zero" error.
                for class_name in self.target_names:
                    log_w_given = math.log( (self.word_counts[class_name].get(word, 0.0) + 1) / (self.num_messages[class_name] + len(self.vocab)) )
                    self.target_scores[class_name] += log_w_given
                    
            self.target_scores[class_name] += self.log_class_priors[class_name]  
            
            max_score = max(self.target_scores.values())
            for class_name, score in self.target_scores.items():
                if score == max_score:
                    result.append(self.target_names.index(class_name))
                    continue
        return result