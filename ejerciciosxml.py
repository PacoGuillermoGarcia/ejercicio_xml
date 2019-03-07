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

#5. Pedir por teclado una palabra y si esa palabra esta en el titulo de alguna imagen te muestra la URL de la imagen 

def URLimagen(cad,noticias):
	lista=noticias.xpath('//image:image[contains(.,"%s")]/image:loc/text()'%cad, namespaces={'image':'https://www.google.com/schemas/sitemap-image/1.1'})
	return lista


from lxml import etree
noticias=etree.parse("noticias.xml")
while True:
	print('''
		1.-Listar noticias filtradas por año
		2.-Total de Noticias
		3.-Introducir una palabra clave y obtener las noticias relacionadas
		4.-Noticias separadas por cadenas de televisión
		5.-Imagenes
		0.-Salir''')
	opcion=input("Opcion: ")
	if opcion=="1":
		anyo=input("Dime un año: ")
		while anyo not in ('2014','2015','2016','2017','2018','2019'):
			print("No tengo noticias de ese año")
			anyo=input("Dime un año: ")
		for elem in Listanoticias(anyo,noticias):
			print("Titulo:",elem)
	if opcion=="2":
		print("El número total de noticias son:",Contarnoticias(noticias))
	if opcion=="3":
		palabra=input("Dime una palabra clave: ")
		for elem in Titulorelacionado(palabra,noticias):
			print(elem)	
	if opcion=="4":
		cadena=input("Dime la cadena de televisión: ")
		while cadena not in ("LaSexta","Antena3"):
			print("No tengo noticias de esa cadena")
			cadena=input("Dime la cadena de televisión: ")
		if cadena=="Antena3":
			cadena="Cocinatis"
			for elem in Noticiasporcadena(cadena,noticias):
				print(elem)
		else:
			for elem in Noticiasporcadena(cadena,noticias):
				if elem=="Cocinatis":
					print("Antena3")
#cad=input("Dime una palabra clave: ")
#for elem in Titulorelacionado(cad,noticias):
#	print(elem)
#for elem in Noticiasporcadena(cad,noticias):
#	print("Titulo:",elem[0])
#	print("Fecha:",elem[1].replace("T"," ").replace("Z",""))
#for elem in URLimagen(cad,noticias):