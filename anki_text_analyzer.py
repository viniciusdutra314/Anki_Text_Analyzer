import plotly.express as px
from os import listdir
def no_special_characters(string):
    trash =[",", "[","]","'","!","?",".","»","=","\\","(",")","/","=","==",":","-",";","^","´","`","|"]
    new_string=string.lower()
    for character in trash:
        new_string.replace(character,"")
    return new_string

def anki_active(word):
    global anki_words
    if len(anki_words)!=0:
        return word not in anki_words
    else: return True

def Add_Word_Counter(text):
    global word_counter,anki_words

    for word in text.split():
        if word in word_counter:
            fixed_word=no_special_characters(word)
            word_counter[fixed_word]+=1
        if word not in word_counter and anki_active(word):
            fixed_word=no_special_characters(word)
            word_counter[fixed_word]=1

possible_files=[j for j in listdir() if j[-4::]==".pdf" or j[-4::]==".txt" and j.lower()!="anki.txt"]
print(possible_files)
file=input("Escolha o arquivo a ser analisado (final com .pdf ou .txt) ")
assert file[-4::]==".pdf" or file[-4::]==".txt" , "Coloque a extensão do arquivo"
titulo=input("Título do gráfico: ")

word_counter={}

anki_words=set()
if "anki.txt" in listdir():
    with open("anki.txt","r",encoding="utf-8") as archive:
        for line in archive.readlines():
            for words in line.split():
                anki_words.add(no_special_characters(words))

if file[-4::]==".pdf":
    from PyPDF2 import PdfReader
    pdf_object = PdfReader(pdf_file:=open(file, 'rb'))
    num_pages = len(pdf_object.pages)
    for i in range(num_pages):
        text=no_special_characters(pdf_object.pages[i].extract_text())
        Add_Word_Counter(text)
    pdf_file.close()


if file[-4::]==".txt":
    with open("anki.txt","r",encoding='utf-8') as file:
        for line in file.readlines():
            Add_Word_Counter(line)

word_ocur_list = list(word_counter.items())

word_ocur_list_sorted = sorted(word_ocur_list, key=lambda x: x[1], reverse=True)

words = [w for w, f in word_ocur_list_sorted]
occurrences = [f for w, f in word_ocur_list_sorted]
total_occurrences=sum(occurrences)

anki="" if len(anki_words)==0 else "_anki"
with open(file[:-4]+anki+'.txt', 'w',encoding="utf-8") as f:
    f.write(f"Análise do arquivo {file}\n")
    if len(anki_words): f.write(f"Considerando somente o que não está no Anki\n")
    f.write(f"{len(words)} Palavras únicas\n")
    f.write(f"{round(len(words)/num_pages)} Palavras únicas por página\n")
    for j in range(len(words)):
        f.write(f"Rank {j+1}, {words[j]}: frequência  {round(100*(occurrences[j]/total_occurrences),4)}%  ocorrências   {occurrences[j]} \n")

x,y=[],[]
parcial_sum=0
for j in range(len(words)):
    parcial_sum+=occurrences[j]
    x.append(parcial_sum/sum(occurrences))
    y.append(j)

fig=px.scatter(x=x,y=y,width=1920,height=1080,title=titulo.title() + " Estatística")
fig.update_layout(
        xaxis_title="Compreensão Textual em %",
        yaxis_title="Palavras",
        font=dict(family="Courier New, monospace", size=36,color="RebeccaPurple"))
fig.show()
fig.write_html(titulo+"_compreensao_textual"+'.html')

Rank=[j for j in range(1,len(occurrences)+1)]

frequencies=[j/total_occurrences for j in occurrences]

fig2=px.scatter(x=Rank,y=frequencies,width=1920,height=1080,title=titulo.title() + " Frequência de palavras",log_y=True,log_x=True)
fig2.update_layout(xaxis_title="Rank",yaxis_title="Frequência em %",font=dict(
        family="Courier New, monospace",size=36,color="RebeccaPurple"))
fig2.update_yaxes(minor=dict(ticks="inside", ticklen=10, showgrid=True),type='log',dtick=1)
fig2.update_xaxes(minor=dict(ticks="inside", ticklen=10, showgrid=True),type='log',dtick=1)
fig2.show()
fig2.write_html(titulo+"_frequencia_palavras"+'.html')
