# Desarrollo_Equipo_3

Este repositorio contiene el archivo Model.py el cual contiene código de NLP para la comparación de dos archivos y poder decir si contiene plagio y en que porcentaje. También está el archivo NewModel.py con nuestro nuevo modelo que contiene Inteligencia Artificial. Cuenta con 2 archivos main para correr nuestras implementaciones, main.py corre nuestra implementación de NLP y mainIA.py tiene nuestro modelo con Inteligencia Artificial. Cuenta con la carpeta **originals** que contiene los archivos .txt originales, también la carpeta **suspicious** que tiene los .txt de los cuales se sospecha presencia de plagio. Dentro de la carpeta **tests** se encuentran todos los archivos de nuestras pruebas unitarias. 

## Instrucciones NLP
**Instalar las siguientes librerías**
```bash
pip3 install  nltk
pip3 install sklearn
pip3 install pairwise
pip3 install spacy
python -m space download en_core_web_sm
pip3 install scikit-learn
pip3 install tabulate
```

**Para correr el proyecto**
```bash
python3 main.py
```
Elegir una opción del 1 al 4:

<img width="441" alt="Captura de pantalla 2024-05-27 a la(s) 10 51 08 p m" src="https://github.com/JorgeBlancoA01745907/Desarrollo_Equipo_3/assets/69489228/5d6ec20f-f2ee-470e-b3a4-6f7ae6244ca7">

Si se elige la opción 1 proporcionar el nombre de los archivos a comparar y si se elige 2 poner el nombre del archivo.

<img width="475" alt="Captura de pantalla 2024-05-27 a la(s) 10 55 13 p m" src="https://github.com/JorgeBlancoA01745907/Desarrollo_Equipo_3/assets/69489228/a8f38333-dabe-4cb7-82a4-4f2d4db54c04">



**Para correr las pruebas unitarias**

```bash
python3 -m unittest   
```



## Instrucciones IA
**Instalar las siguientes librerías**
```bash
pip3 install matplotlib
pip3 install nltk
pip3 install transformers
pip3 install torch
pip3 install tabulate
pip3 install scikit-learn

```

**Para correr el proyecto**
```bash
python3 mainIA.py
```


