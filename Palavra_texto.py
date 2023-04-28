import plotly.express as px
from linearizar import *
resposta=input("Colocar texto ou Pdf?  ")
titulo_grafico=input("Título do gráfico  ")
anki_resposta=input("Deseja usar o banco de dados Anki? ")
anki=[]
ativacao_anki=""
if anki_resposta.lower()[0:1]=="s":
    import webbrowser
    ativacao_anki=" Com Dados Anki"
    print("converta o texto em uma só linha, usando o site que foi aberto")
    webbrowser.open('https://tools.knowledgewalls.com/online-multiline-to-single-line-converter')
    anki=input("Coloque o txt do deck anki  ").lower().replace(",","").replace("[","").replace("]","").replace("'","'").replace('"""',"").replace(
             "!","").replace("?","").replace(".","").replace("»","").replace("=","").replace("\\","").replace(
    "(","").replace(")","").replace("/","").replace("==","").replace(":","").split()
if resposta.lower()[0:3]=="tex":
    import webbrowser
    print("converta o texto em uma só linha, usando o site que foi aberto")
    webbrowser.open('https://tools.knowledgewalls.com/online-multiline-to-single-line-converter')
    texto=input("Coloque o seu texto:  ").lower().replace(",","").replace("[","").replace("]","").replace("'","'").replace('"""',"").replace(
             "!","").replace("?","").replace(".","").replace("»","").replace("=","").replace("\\","").replace(
    "(","").replace(")","").replace("/","").replace("==","").split().replace(":","") #separa cada palavra
    nomepdf=titulo_grafico
    pages=1
if resposta.lower()=="pdf":
    import PyPDF2
    nomepdf=input("Coloque o nome do pdf (não se deve colocar .pdf)  ")
    pdffileobj = open(nomepdf+ '.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    pages = pdfreader.numPages
    text = []
    for i in range(pages):
        page = pdfreader.getPage(i)
        text.append(page.extractText().lower().replace(",","").replace("[","").replace("]","").replace("'","'").replace('"""',"").replace(
             "!","").replace("?","").replace(".","").replace("»","").replace("“","").replace("”","").replace(
        "-","").replace(";","").split())
    texto=[]
    for j in range(len(text)):
        texto+=text[j]
palavras=[]
words={}
porcentagem=len(texto)
ocorrencias=[]
i=0
mots=[]
for j in texto:
    if j not in palavras:
        palavras.append(j)
        if j not in anki:
            palavras.append(j)
            contagem=100*texto.count(j)/porcentagem
            ocorrencias.append(texto.count(j))
            words[j]=contagem
            i=i+1
sort_data = sorted(words.items(), key=lambda x: x[1], reverse=True)
palabras=[]
frequencia=[]
for j in range(len(sort_data)):
    palabras.append(sort_data[j][0])
    frequencia.append(sort_data[j][1])
soma=0
soma2=0
porcentagens=[]
necessarias=[]
x=[]
y=[]
z=1
i=int(0)
while soma2 <sum(ocorrencias):
    soma+=frequencia[i]
    soma2+=ocorrencias[i]
    if i==int(0):
        d=0
    else:
        x.append(soma)
        y.append(i)
    i+=1

with open(nomepdf+ ativacao_anki+'.txt', 'w') as f:
    f.write(f"{len(texto)} Palavras totais\n")
    f.write(f"{len(palavras)} Palavras únicas\n {ativacao_anki}")
    f.write(f"{round(len(palavras)/pages)} Palavras únicas por página\n")
    f.write(f"{round(x[frequencia.index(min(frequencia))],2)} % , na Palavra {round(y[frequencia.index(min(frequencia))],2)}º Ocorre a transição linear\n ")
    f.write("\n")
    for j in range(i):
        try:
            f.write(f"Rank {j+1},    {palabras[j]}:       {round(frequencia[j],4)}%        {round((frequencia[j]/100)*len(texto))} ocorrencias\n")
        except:ig=0

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
