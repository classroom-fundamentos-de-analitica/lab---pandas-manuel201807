"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    f = len(tbl0)
    return f


def pregunta_02():
    col = tbl0.shape
    return col[1]


def pregunta_03():
    reg = tbl0.groupby('_c1')['_c1'].count()
    return reg


def pregunta_04():
    prom = tbl0.groupby('_c1')['_c2'].mean()
    return prom


def pregunta_05():
    valorMax = tbl0.groupby('_c1')['_c2'].max()
    return valorMax


def pregunta_06():
    unicos = tbl1['_c4'].unique()
    unicos = list(unicos)
    unicos.sort()
    return [letra.upper() for letra in unicos]


def pregunta_07():
    suma = tbl0.groupby('_c1')['_c2'].sum()
    return suma


def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0


def pregunta_09():
    tbl0['year'] = tbl0['_c3'].map(lambda x: x.split('-')[0])
    return tbl0


def pregunta_10():
    letras = sorted(tbl0._c1.unique())
    data = {"_c2": []}
    for letra in letras:
        valoresC2 = sorted(tbl0[tbl0._c1 == letra]._c2)
        listaC2 = [str(i) for i in valoresC2]
        valorString = ":".join(listaC2)
        data["_c2"] = data["_c2"] + [valorString]
    result = pd.DataFrame(data, index=pd.Series(letras, name="_c1"))
    return result


def pregunta_11():
    numeros = tbl1._c0.unique()
    data = {"_c0": numeros, "_c4": []}
    for numero in numeros:
        valores = sorted(tbl1[tbl1._c0 == numero]._c4)
        valoresString = ",".join(valores)
        data["_c4"] += [valoresString]
    result = pd.DataFrame(data)
    return result


def pregunta_12():
    tbl2['_c5b'] = tbl2['_c5b'].apply(lambda x: str(x))
    tbl2['_c5'] = tbl2[['_c5a', '_c5b']].apply(':'.join, axis=1)
    col0 = sorted(list(tbl2['_c0'].unique()))
    col5 = tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(e for e in sorted(x)))

    result = pd.DataFrame({'_c0': col0, "_c5": list(col5.array)})
    return result


def pregunta_13():
    return ((pd.merge(tbl2,tbl0).groupby("_c1").sum()["_c5b"]))