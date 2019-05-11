# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:19:46 2018

@author: itm
"""

import tensorflow as tf

a=tf.constant([5])
b=tf.constant([3])
suma=tf.add(a,b)        #para realizar la suma con instrucciones
#result=tf.variable(0)   # para inicializar la variable
sess=tf.Session()
result=sess.run(suma)      #para que corra la operacion
print(result)
sess.close()

#session=tf.Session()
#print("HOLA MUNDO")
#session.close()
