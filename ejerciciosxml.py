#1.Listar las noticias que se publicaron en un año pedido por teclado.

def Listanoticias(anyo,noticias):
	lista=noticias.xpath('//news:news[starts-with(news:publication_date,"%s")]/news:title/text()'%anyo, namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9'})
	return lista

#2.Contar cuantas noticias hay en total

def Contarnoticias(noticias):
	numeronoticias=noticias.xpath('count(//news:news)', namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9'})
	return int(numeronoticias)

#3.Pedir una palabra o palabras clave por teclado y mostrar las noticias relacionadas con esa palabra

def Titulorelacionado(cad,noticias):
	lista=noticias.xpath('//news:news[contains(.,"%s")]/news:title/text()'%cad, namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9'})
	return lista

#4. Pedir por teclado el nombre de la cadena de televisión y o subcadena de la misma y te muestra el titulo y la fecha de las noticias de esa cadena de televisión

def Noticiasporcadena(cad,noticias):
	listanoticias=noticias.xpath('//news:news[x:publication[news:name="%s"]]/news:title/text()'%cad, namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9', 'x':'https://www.sitemaps.org/schemas/sitemap/0.9'})
	listafechas=noticias.xpath('//news:news[x:publication[news:name="%s"]]/news:publication_date/text()'%cad, namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9', 'x':'https://www.sitemaps.org/schemas/sitemap/0.9'})
	return zip(listanoticias,listafechas)




from lxml import etree
noticias=etree.parse("noticias.xml")
#anyo=input("Dime un año: ")
#if anyo not in ('2014','2015','2016','2017','2018','2019'):
	#print("No tengo noticias de ese año")
#else: 
	#for elem in Listanoticias(anyo,noticias):
	#	print(elem)
#print(Contarnoticias(noticias))
cad=input("Dime una palabra clave: ")
#for elem in Titulorelacionado(cad,noticias):
#	print(elem)
for elem in Noticiasporcadena(cad,noticias):
	print("Titulo:",elem[0])
	print("Fecha:",elem[1].replace("T"," ").replace("Z",""))