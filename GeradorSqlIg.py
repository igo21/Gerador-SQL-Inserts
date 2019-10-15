from tkinter import *
import csv #para fazer leitura do arq csv
import clipboard #para efetuar copias do cmd
class Aplicacao:
    def __init__(self, master=None):
        self.contemail=3
        self.id=40
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
        completo=texto[0].split(" ") #nome completo
        primeiro=completo[0]
        ultimo=completo[-1]

        sql1=''
        nometb=str(self.campo.get())
        nometb=nometb.split(';')
        nometbUser=nometb[0]
        nomeMetaUser=nometb[1]
        numCapabilitie=nometb[2]
        sete = ''
        if texto[2].replace(" ","")=="": #todo-mudar
            #sete = "\ninsert into "+nometb+" ("+cabecalho[0]+","+cabecalho[1]+","+cabecalho[2]+","+cabecalho[3]+") values ("+texto[0]+","+texto[1]+","+texto[2]+",example"+str(self.contemail)+"@mail.com);"
            sete = "\ninsert into "+nometbUser+" (id,user_login,user_pass,user_nicename,user_email,user_url,user_registered,user_activation_key,user_status,display_name) " \
                                           "values ("+str(self.id)+",'"+texto[1]+"',md5('"+str(texto[1])+"'),'"+texto[0]+"','example"+str(self.contemail)+"@mail.com','','','','0','"+texto[0]+"'"+");"
            self.contemail=self.contemail+1
        else:
            sete = "\ninsert into " + nometbUser + " (id,user_login,user_pass,user_nicename,user_email,user_url,user_registered,user_activation_key,user_status,display_name) " \
                                               "values (" + str(self.id) + ",'" + texto[1] + "',md5('" + str(texto[1]) + "'),'" + texto[0] + "','" + texto[2]+"','','','','0','" +texto[0] + "'" + ");"
        sql1=sql1+sete
        self.text2.insert(END,sql1)

        nickname = primeiro
        first_name = primeiro
        last_name = ultimo
        description = ""
        rich_editing = "true"
        syntax_highlighting = "true"
        comment_shortcuts = "false"
        admin_color = "fresh"
        use_ssl = "0"
        show_admin_bar_front = "true"
        locale = ""
        wpintr_capabilities = 'a:1:{s:'+str(numCapabilitie)+':"colaborador";b;1;}'
        # 11 é id da rule capabilitie colaborador, em cada PC esse numero poderá mudar.
        wpintr_user_level = "0"
        dismissed_wp_pointers = ""

        #inserts nas outras tabelas
        sql2="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','nickname','"+nickname+"')"
        sql3="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','first_name','"+first_name+"')"
        sql4="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','last_name','"+last_name+"')"
        sql5="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','description','"+description+"')"
        sql6="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','rich_editing','"+rich_editing+"')"
        sql7="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','syntax_highlighting','"+syntax_highlighting+"')"
        sql8="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','comment_shortcuts','"+comment_shortcuts+"')"
        sql9="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','admin_color','"+admin_color+"')"
        sql10="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','use_ssl','"+use_ssl+"')"
        sql11="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','show_admin_bar_front','"+show_admin_bar_front+"')"
        sql12="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','locale','"+locale+"')"
        sql13="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','wpintr_capabilities','"+wpintr_capabilities+"')"
        sql14="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','wpintr_user_level','"+wpintr_user_level+"')"
        sql15="\ninsert into "+nomeMetaUser+" (user_id,meta_key,meta_value) values('"+str(self.id)+"','dismissed_wp_pointers','"+dismissed_wp_pointers+"')"

        self.text2.insert(END, sql2)
        self.text2.insert(END, sql3)
        self.text2.insert(END, sql4)
        self.text2.insert(END, sql5)
        self.text2.insert(END, sql6)
        self.text2.insert(END, sql7)
        self.text2.insert(END, sql8)
        self.text2.insert(END, sql9)
        self.text2.insert(END, sql10)
        self.text2.insert(END, sql11)
        self.text2.insert(END, sql12)
        self.text2.insert(END, sql13)
        self.text2.insert(END, sql14)
        self.text2.insert(END, sql15)

        self.id = self.id + 1  #resetando variavel de ID


    """
        nickname = 02339140052 
        first_name = estagiario 
        last_name = estagiario sobrenome 
        description = "em branco/null"
        rich_editing = true
        syntax_highlighting = true
        comment_shortcuts = false
        admin_color = fresh
        use_ssl = 0 
        show_admin_bar_front = true
        locale = "em branco/null"
        wpintr_capabilities = a:1:{s:11:"colaborador";b;1;}
        wpintr_user_level = 0
        dismissed_wp_pointers = "em branco/null"

    """
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

