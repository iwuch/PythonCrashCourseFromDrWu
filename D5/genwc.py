from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
import csv
def generateWordCloud(filepath,filename,titlename,stopwords,wordslen=10,iscsv=False,istitle=False):
    with open(filepath+filename,encoding='utf-8') as f:
        contents = f.read()
    punc_lst = ["'",'.',',','?','-','!','\"',':',';','(',')',']','[','_']
    for punc in punc_lst:
        contents = contents.replace(punc,' ')
    words_list = contents.split()
    words_dict = {}
    words_set = set(words_list)
    words = []
    for word in words_set:
        words_dict[word] = words_list.count(word)

    stop_words = stopwords 
    
    if istitle:
        for word in sorted(words_dict,key=words_dict.__getitem__,reverse=True):
            if len(words)>=wordslen:
                break
            if len(word)>4 and word not in stop_words and word[0].istitle():
                print(f'{word}:{words_dict[word]}')
                words.append((word,words_dict[word]))
    else:
        for word in sorted(words_dict,key=words_dict.__getitem__,reverse=True):
            if len(words)>=wordslen:
                break
            if len(word)>4 and word not in stop_words:
                print(f'{word}:{words_dict[word]}')
                words.append((word,words_dict[word]))             

    wd = (
        WordCloud()
        .add("", words, word_size_range=[20, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title=titlename))
        )
    wd.render(titlename+".html")

    if iscsv:
        headers = ['word','count']
        with open(titlename+'.csv','w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(words)

if __name__=='__main__':
    filepath = "./"
    filename = "alice.txt"
    titlename = "test"
    stopwords =['little','again','herself','could','would','There','thought','The','And','You','What','She','But','March','according','united','states']
    wordslen = 10
    iscsv = True
    istitle =True
    generateWordCloud(filepath,filename,titlename,stopwords,wordslen,iscsv,istitle)