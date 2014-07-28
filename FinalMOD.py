# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 2014

@author: Wellington Viana Lobato Junior
"""

import BeautifulSoup as bfs
import mechanize

navegador = mechanize.Browser()
navegador.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  

#pgi = "http://www.mangahere.co/manga/elfen_lied/c001/" #Primeira Página do manga,sempre!

pgi = raw_input("Entre com o link: ")

html = navegador.open(pgi)
sopa = bfs.BeautifulSoup(html)

opcao_paginas = sopa.findAll('select',{"class":"wid60"})
#opcao_paginas = sopa.findAll('img',{"id":"image"})
opcao_paginas = str(opcao_paginas)

#print opcao_paginas

opcao_paginas = opcao_paginas.replace("<option value=","")
opcao_paginas = opcao_paginas.replace("</option>","")
opcao_paginas = opcao_paginas.replace('<option selected="selected">',"")
opcao_paginas = opcao_paginas.replace("</select>","")
opcao_paginas = opcao_paginas.replace('<select class="wid60" onchange="change_page(this)">',"")
opcao_paginas = opcao_paginas.replace('[',"")
opcao_paginas = opcao_paginas.replace(']',"")
opcao_paginas = opcao_paginas.replace('selected="selected"','')
opcao_paginas = opcao_paginas.replace('"',"")

opcao_paginas = opcao_paginas.split("\n") #Transforma a string em lista
opcao_paginas.remove('')
opcao_paginas.remove('')

#print opcao_paginas 

nome_do_arquivo = 0
for op in opcao_paginas:
    num = op.find(">")
    new_pgi = op[0:num]
    #print new_pgi """Conter os links das paginas"""
    
    #print "O problema pode estar aqui:",new_pgi
    
    try:
        html2 = navegador.open(new_pgi)
        sopa2 = bfs.BeautifulSoup(html2)
        new_opcao = sopa2.findAll('img',{"id":"image"})
        for img in new_opcao:
            filename = str(nome_do_arquivo)+".jpg"
            nome_do_arquivo = nome_do_arquivo + 1
            data = navegador.open(img['src']).read()
            save = open(filename,'wb')
            save.write(data)
            save.close()
      
    except:
        print "Processo finalizado!"
        break  