import plotly.express as px
from os import listdir
def no_special_characters(string):
    trash =[",", "[","]","'","!","?",".","»","=","\\","(",")","/","=","==",":","-",";","^","´","`","|"]
    string=string.lower()
    for character in trash:
        string.replace("character","")
    return string

def Add_Word_Counter(text):
    global word_counter
    for word in text.split():
        word=no_special_characters(word)
        if word in word_counter:
            word_counter[word]+=1
        else:
            word_counter[word]=1

possible_files=[j for j in listdir() if j[-4::]==".pdf" or j[-4::]==".txt" and j.lower()!="anki.txt"]
print(possible_files)
#file=input("Escolha o arquivo a ser analisado (final com .pdf ou .txt) ")
file="vulgata.pdf"
# titulo=input("Título do gráfico: ")
titulo="teste"
word_counter={}
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
        for line in file.readlines:
            Add_Word_Counter(line)
unique_words=len(word_counter)

word_freq_list = list(word_counter.items())

word_freq_list_sorted = sorted(word_freq_list, key=lambda x: x[1], reverse=True)

words = [w for w, f in word_freq_list_sorted]
frequencies = [f for w, f in word_freq_list_sorted]


with open(file[:-4]+'.txt', 'w',encoding="utf-8") as f:
    f.write(f"Análise do arquivo {file}")
    f.write(f"{unique_words} Palavras únicas\n")
    f.write(f"{round(unique_words/num_pages)} Palavras únicas por página\n")
    for j in range(unique_words):
        f.write(f"Rank {j+1}, {words[j]}: frequência  {round(100*(frequencies[j]/unique_words),4)}%  ocorrências   {frequencies[j]} \n")

if anki_resposta.lower()[0:1]!="s":
    fig=px.scatter(x=x,y=y,width=1920,height=1080,title=nomepdf.title() + ativacao_anki)
    fig.update_layout(
        title=titulo_grafico.title(),
        xaxis_title="Compreensão Textual em %",
        yaxis_title="Palavras",
        font=dict(
            family="Courier New, monospace",
            size=36,
            color="RebeccaPurple"
        )
    )

    fig.show()
    fig.write_html(nomepdf+ ativacao_anki+'.html')
Rank=[]
for j in range (1,len(frequencia)+1):
    Rank.append(j)

fig2=px.scatter(x=Rank,y=frequencia,width=1920,height=1080,title=nomepdf.title() + "Frequência palavras",log_y=True,log_x=True)
fig2.update_layout(
    title=nomepdf.title() + " Frequência palavras",
    xaxis_title="Rank",
    yaxis_title="Frequência em %",
    font=dict(
        family="Courier New, monospace",
        size=36,
        color="RebeccaPurple"
    )
)
fig2.update_yaxes(minor=dict(ticks="inside", ticklen=10, showgrid=True),type='log',dtick=1)
fig2.update_xaxes(minor=dict(ticks="inside", ticklen=10, showgrid=True),type='log',dtick=1)
fig2.show()
fig2.write_html(nomepdf.title() + ativacao_anki+ "Frequência palavras"+'.html')
