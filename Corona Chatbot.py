#importing the required library
from newspaper import Article
import random
import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

#download the punkt package
nltk.download('punkt',quiet=True)

#Get the article
article = Article('https://en.wikipedia.org/wiki/Coronavirus')
article.download()
article.parse()
article.nlp()
corpus = article.text
#print(corpus)



#Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)
#print(sentence_list)


#Function to return random greeting message to user
def greet_res(text):
    text = text.lower()
    #Bot greeting response
    bot_greeting = ['hello','hey','heya','heyz','hi','hii']
    #user greeting response
    user_greeting = ['hello','helo','hellooo','hiiii','hi','heyy']
    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)

#Function to return gratitude mesaage to user
def gratitude_res(text):
    text = text.lower()
    # Bot gratitude response
    bot_gratitude = ['nice to help you', 'most welcome', 'glad to help', 'pleasure to be of help']
    # user gratitude response
    user_gratitude = ['thanku', 'ty', 'tysm', 'thanks', 'thankyou', 'thankss']
    for word in text.split():
        if word in user_gratitude:
            return random.choice(bot_gratitude)


# index sort
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))
    x = list_var

    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index



#Function to bot response
def bot_res(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_res = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    s_score = cosine_similarity(cm[-1],cm)
    # print(s_score)
    s_score_list = s_score.flatten()
    index = index_sort(s_score_list)
    # sen_list = ['asfsaf','agfgsadf','afsfeafa','whats corona']
    # s_score_list = [0.01,0.24,0.16,1] => [1,0.24,0.16,0.01]
    # index = [1,2,0]
    index = index[1:]
    res_flag = 0
    j = 0
    for i in range(len(index)):
        if s_score_list[index[i]]>0.0:
            bot_res = bot_res+' '+sentence_list[index[i]]
            res_flag = 1
            j= j+1
        if j>2:
            break
    if res_flag==0:
        bot_res = bot_res + 'Please be more specific, i didnot understand!'
    sentence_list.remove(user_input)
    return bot_res






#Main function
print('''Welcome to corona chatbot 
To end the conversation type exit/quit''')
exit_list = ['exit','quit','end','quitt','exitt','bye','byeee']
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print("Thanks for interaction,Bye!")
        break
    elif greet_res(user_input)!= None:
        print("Bot: ",greet_res(user_input))

    elif gratitude_res(user_input)!= None:
        print("Bot: ", gratitude_res(user_input))
    else:
        print("Bot: ",bot_res(user_input))


        
        

