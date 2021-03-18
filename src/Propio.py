'''
MIT License

Copyright (c) 2020 Sebastian Cornejo
             in collaboration with Faviola Molina from dLab - Fundación Ciencia y Vida

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


"""
Los productos que salen de la contribucion de la UDD son:
33
"""

import datetime
import pandas as pd

def prod33():
    f = open ('holamundo.txt','wb')
    f.write(bytes(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 'utf-8'))
    pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/Datos_Chile/main/paso_a_paso/paso_a_paso.csv").to_csv("Hola.csv")
    f.close()
    return 


if __name__ == '__main__':
    print('Generating producto 33')
    prod33()
