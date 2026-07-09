
def leer_opcion():
    try:
     correcto=0
     while correcto==0:
      opcion=int(input("Ingrese una opcion: "))
      if not ValueError:
       correcto=1
       return opcion
       break
    
    except ValueError:
       print("Ingrese un numero entero")

#Pendiente      
def cupos_genero(genero):
  print("Me rindo en esta parte")
  
   
       
def busqueda_precio(p_min, p_max,cartelera):
  lista_precio=[]
  for codigo in cartelera:
   print("Tambien")

  
  
  
def agregar_pelicula(codigo, titulo, genero,duracion,clasificacion, idioma, es_3d, precio, cupos,peliculas):
  lista_pelicula=[]
  lista_pelicula.append(codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos)
  peliculas.append(lista_pelicula)
  return peliculas 

def eliminar_pelicula(peliculas,cartelera):
  eliminar=input("Ingrese la pelicula a eliminar")
  for codigo in peliculas:
    if codigo==peliculas[eliminar[0]]:
     peliculas.remove[eliminar[0]]
     return peliculas
    
def programa_principal():
    peliculas={
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }
    cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],

}

    while True:
      print("========== MENÚ PRINCIPAL ==========\n1. Cupos por género\n2. Búsqueda de películas por rango de precio\n3. Actualizar precio de película")
      print("4. Agregar película\n5. Eliminar película\n6. Salir\n=====================================")
      opcion=leer_opcion()
      match opcion:
         case 1:
            genero=cupos_por_genero(genero)
           
         case 2:
          try:
            while True:
             
             p_min=int(input("Ingrese e lnumero minimo: "))
             p_max=int(input("Ingrese el valor maximo: "))
             if p_min>p_max:
               print("El numero min debe ser menor al maximo")
               
             else:
              busqueda=busqueda_precio(p_min, p_max,cartelera)
              print(busqueda)
              break

          except ValueError:
            print("Debe ingresar numeros no letras")
            continue


         case 3:
          actualizar_precio(codigo,nuevo_precio)
          
         case 4:
          while True:
           codigo=input("Ingrese el codigo de la pelicula")
           if len(codigo)==0 or codigo in peliculas:
            print("El codigo no debe existir de antes y debe tener al menos un caracter")
            continue
           else:
             print("")
           valido=True
           titulo=input("Ingrese el titulo de la pelicula: ")
           if len(titulo)==0:
            print("La pelicula debe tener un nombre")
            continue
           else:
             print("")
             valido=True
             
           genero=input("Ingrese el titulo de la pelicula: ")
           if len(genero)==0:
            print("La pelicula debe tener un nombre")
            continue
           else:
             print("")
             valido=True
           
           try:
            duracion=int(input("Ingrese la duracion: "))
            if duracion <= 0 :
             print("El valor debe ser mayor que 0")
             continue
            else:
              print("")
              valido=True
           
           except ValueError:
            print("El valor debe ser mayor que 0")
             
           clasificación=input("Ingrese la clasificacion debe ser exactamente A,B o C")
           if clasificacion != "A" or clasificacion != "B" or clasificacion != "C":
             print("Clasificacion ingresada incorrectamente")
           else:
            print("")
            valido=True
           idioma=input("Ingrese el idioma")
           if len(idioma)==0:
            print("El idioma debe tener caracteres")
            continue
           else:
             print("")
             valido=True
           es_3d=input("Es o no es 3D:  ")
           if es_3d!="s":
             print("")
           elif es_3d!="n":
             print("")

           else:
             print("Incorrecto")
           
           try:
             precio=int(input("Ingrese la duracion: "))
             if precio <= 0 :
              print("El valor debe ser mayor que 0")
              continue
             else:
              print("")
           except ValueError:
            print("El valor debe ser mayor que 0")
            continue
           
           try:
             cupos=int(input("Ingrese el cupo: "))
             if cupos <= 0 :
              print("El valor debe ser mayor que 0")
              continue
             else:
              print("")
           except ValueError:
            print("El valor debe ser mayor que 0")
            continue
           agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos,peliculas,cartelera)
           print("Pelicula agregada")
         case 4:
            eliminar=eliminar_pelicula()

         case 5:
          print("Gracias por usar nuestro programa")
          break
programa_principal()
        
      
           
           


          
          

      
 

