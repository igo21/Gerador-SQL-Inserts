from tkinter import *
import csv
import clipboard #para efetuar copias do cmd
class Aplicacao:
    def __init__(self, master=None):
        self.contemail=0
        self.telamaster = master
        self.fontePadrao = ("Arial", "10", 'bold')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['bg'] = '#696969'
        self.primeiroContainer.pack(side=LEFT)

        # campo tabela bd

        self.campo = Entry(self.primeiroContainer)
        self.campo['width'] = 15
        self.campo['font'] = "Arial", "15"
        self.campo['justify']=CENTER
        self.campo['bg'] = 'white'
        self.campo.insert(0,"nomeTB")
        self.campo.pack(side=TOP)
        
        #fim campo tabelabd
        
        
        # botão gerar

        self.gerar = Button(self.primeiroContainer)
        self.gerar["text"] = "Gerar"
        self.gerar["font"] = ("Calibri", "12", "bold")
        self.gerar["width"] = 20
        self.gerar['bg'] = '#00cc4c'
        self.gerar['fg'] = '#191919'
        self.gerar["command"] = self.capturaTexto
        self.gerar.pack(side=TOP)

        #botão apagar

        self.apagar = Button(self.primeiroContainer)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Calibri", "12", "bold")
        self.apagar["width"] = 20
        self.apagar['bg'] = '#e61919'
        self.apagar['fg'] = '#191919'
        self.apagar["command"] = self.apagaTexto
        self.apagar.pack(side=TOP)

        #botão copiar
        self.copiar = Button(self.primeiroContainer)
        self.copiar["text"] = "Copiar"
        self.copiar["font"] = ("Calibri", "12", "bold")
        self.copiar["width"] = 20
        self.copiar['bg'] = '#ffdf00'
        self.copiar['fg'] = '#191919'
        self.copiar["command"] = self.copiaTexto
        self.copiar.pack(side=TOP)

        #botão sair
        self.sair = Button(self.primeiroContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "12", "bold")
        self.sair["width"] = 20
        self.sair['bg'] = '#000'
        self.sair['fg'] = '#fff'
        self.sair["command"] = self.sair_exit
        self.sair.pack(side=TOP)
       
       
        self.text2 = Text(master, height=40, width=100)
        self.scroll = Scrollbar(master, command=self.text2.yview)
        self.text2.configure(yscrollcommand=self.scroll.set)

        self.text2.tag_configure('color', foreground='#000')
        self.text2.insert(END, '#Feito por Igor Ramos de Oliveira, 14-10-2019.\n')
        #self.quote = '#Digite os atributos separados por enter\n'
        self.text2.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)
       
    def capturaTexto(self):
        """Gerar sql importação aqui - igor ramos de oliveira"""
        #inicio do tratamento do texto a ser convertido em sql inserts
        self.apagaTexto()
        self.text2.insert(END,"#Sql Gerado com Sucesso! #2019-10/14\n\n")
        arquivo = open('pessoas.csv')
        linhas = csv.reader(arquivo)
        cabecalho=[]
        texto=[]
        #cabecalho=linhas[0]
        #print(cabecalho)
        c=0
        for linha in linhas:
            #print(linha)
            if c!=0:
                for j in linha:
                    #print(j.split(";"))
                    texto=j.split(";")
                    self.geraSql(texto,cabecalho)
            else:
                for i in linha:
                    cabecalho=i.split(";")
                    #print(i.split(";"))#vetor splitado em ; pode ser usado para gravar cada parte em uma variavel e ser usado posteriormente.
            c=c+1
           
        #fim do tratamento de texto e geração
        #inicio codigo gerador
    
       
    def geraSql(self,texto,cabecalho):
        #fazer funcção aqui
        #cabecalho=[]
        #cabecalho=cabecalho
        mae=''
        nometb=str(self.campo.get())
        sete = ''
        if texto[3].replace(" ","")=="":
            sete = "\ninsert into "+nometb+" ("+cabecalho[0]+","+cabecalho[1]+","+cabecalho[2]+","+cabecalho[3]+") values ("+texto[0]+","+texto[1]+","+texto[2]+",example"+str(self.contemail)+"@mail.com);"
            self.contemail=self.contemail+1
        else:
            sete = "\ninsert into "+nometb+" ("+cabecalho[0]+","+cabecalho[1]+","+cabecalho[2]+","+cabecalho[3]+") values ("+texto[0]+","+texto[1]+","+texto[2]+","+texto[3]+");"
        mae=mae+sete
        self.text2.insert(END,mae)    
        
    def apagaTexto(self):
        self.contemail=0
        self.text2.delete(1.0, END)
        self.text2.insert(END, '#Feito por Igor Ramos de Oliveira, 14-10-2018.\n')
       
    def apagaTexto2(self):
        self.text2.delete(1.0, END)
       
    def copiaTexto(self):
        texto = self.text2.get(1.0, END)
        clipboard.copy(texto)

    def sair_exit(self):
        self.telamaster.destroy()

def centralizar(janela):
    x = (janela.winfo_screenwidth() - janela.winfo_reqwidth()) / 6
    y = (janela.winfo_screenheight() - janela.winfo_reqheight()) / 6
    janela.geometry("+%d+%d" % (x, y))

root = Tk()
root.title("Gerador SLQ versão : 1.0")
root.resizable(0,0)
root['bg']='#545454'
centralizar(root)
Aplicacao(root)
root.mainloop()
#aqui é  fim do código
#fim :)

#arquivo pessoas.csv
#nome;idade;email
#Gustavo;28;gustavo@dicasdeprogramcao.com.br
#Joao;35;joao@dicasdepython.com.br
#Maria;23;maria@dicasdeprogramacao.com.br
#Ana;25;ana@dicasdepython.com.br
