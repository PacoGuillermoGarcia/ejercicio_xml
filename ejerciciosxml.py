#1.Listar las noticias que se publicaron en un año pedido por teclado.

def Listanoticias(anyo,noticias):
	lista=noticias.xpath('//news:news[starts-with(news:publication_date,"%s")]/news:title/text()'%anyo, namespaces={'news':'https://www.google.com/schemas/sitemap-news/0.9'})
	return lista









#from lxml import etree
#noticias=etree.parse("noticias.xml")
#anyo=input("Dime un año: ")
#if anyo not in ('2014','2015','2016','2017','2018','2019'):
	#print("No tengo noticias de ese año")
#else: 
	#for elem in Listanoticias(anyo,noticias):
	#	print(elem)