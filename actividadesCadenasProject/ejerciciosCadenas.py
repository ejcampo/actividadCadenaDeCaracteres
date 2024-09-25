#1. Teniendo en cuenta las siguientes variables que describen su edad, nombre y comida favorita, genera
#una cadena para presentarse:
print("")
name = "Luis"
age = 27
favoriteFood = "Pasta con salsa Bolañesa"
text = f'''Hola! Mi nombre es {name}. Yo tengo {age} años, y mi
comida favorita es {favoriteFood}'''
print(text)
print("")

#2. Crea un código que solicite al usuario su nombre completo. Luego deberá contar el número de letras
#de su nombre, ignorando los espacios. Finalmente, debe saludar al usuario e informarle la longitud de
#su nombre.
fullName = input("Por favor ingrese su nombre completo: ")
length_without_spaces = len(fullName.replace( ' ', ''))
print(f"Hola, {fullName}! Tu nombre tienen {length_without_spaces} letras, excluyendo los espacios.")
print("")

#3. El analista de datos de una prestigiosa empresa láctea de la ciudad de Popayán, calculó las cifras de
#ventas del último trimestre: el porcentaje de aumento de las ventas y crecimiento de ingresos. Genere
#una cadena que le permita mostrar los porcentajes.
increaseSalesParcent = 12.937200081
revenueGrowthPercent = 18.33206078
text1 = f'''Las ventas de la empresa láctea aumentaron un {increaseSalesParcent:.2f}%
y los ingresos crecieron un {revenueGrowthPercent:.2f}%.'''
text1 = text1.replace(".", ",").replace("%,", "%.")
print(text1)
print("")

#4. Se proporciona un mensaje secreto codificado en una cadena, para decodificar el mensaje: "Omita
#los primeros tres caracteres y luego omita todos los demás caracteres".
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
decodedMessage = secretMessage[3::2]
print(decodedMessage)
print("")

#5. Se proporciona una frase y luego se debe mostrar el número de palabras en esa frase.
text2 = 'EL nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
word_count = len(text2.split())
print(f"Numero de palabras en la frase: {word_count}")
print("")

#6. Escriba un programa que tome una cadena como entrada y reemplace todas las apariciones de la letra
#"a" con la letra "e".
word = "Camila"
new_word = word.replace("a", "e")
print(new_word)
print("")

#7. Dada la siguiente frase, escriba un programa que invierta el orden de las palabras en esa frase.
sentence = "La historia del lenguaje de programación Python"
inverted_sentence = sentence.split()[::-1]
print(*inverted_sentence)
print("")