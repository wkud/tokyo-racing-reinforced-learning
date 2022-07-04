import tensorflow as tf
from tensorflow import keras
import keyboard
import pandas as pd
import numpy as np
import socket
import json

train_df = pd.read_csv('merge.csv', sep=';')
np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([
    keras.layers.Dense(16, input_shape=(9,), activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(3, activation='sigmoid')])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

x = np.column_stack((train_df.Left.values, train_df.Left22.values, train_df.Left45.values,
                     train_df.Left67.values, train_df.Front.values, train_df.Right22.values,
                     train_df.Right45.values, train_df.Right67.values, train_df.Right.values))

model.fit(x, train_df.Rotation.values, batch_size=5, epochs=10)





serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind(('', 5240))
serwer.listen(5)


def predict(l, l67, l45, l22, f, r22, r45, r67, r):
    l22 = float("{:.4f}".format(float(l22)))
    l = float("{:.4f}".format(float(l)))
    l67 = float("{:.4f}".format(float(l67)))
    l45 = float("{:.4f}".format(float(l45)))
    f = float("{:.4f}".format(float(f)))
    r45 = float("{:.4f}".format(float(r45)))
    r22 = float("{:.4f}".format(float(r22)))
    r = float("{:.4f}".format(float(r)))
    r67 = float("{:.4f}".format(float(r67)))
    pred = model.predict(np.array([[l, l67, l45, l22, f, r22, r45, r67, r]]))[0]
    q = 0
    index = 0
    for i in range(len(pred)):
        if q < pred[i]:
            q = pred[i]
            index = i
    if index == 2:
        # print('-1')
        return '-1'
    if index == 1:
        # print('1')
        return '1'
    # print('0')
    return '0'

while True:
    print('Czekam')
    client, address = serwer.accept()
    print('Połączono się z serwerem. Naciśnij \'q\', aby zakończyć')
    while True:
        try:
            client.settimeout(5.0)
            msg = client.recv(1024)
            client.settimeout(None)
        except:
            break
        
        if keyboard.read_key() == "q":
            print("You pressed q")
            break
        
        if len(msg) > 0:
            string_msg = msg.decode('utf-8')
            print(string_msg)
            table = string_msg.split(';')
            data_to_send = predict(table[4], table[5], table[6], table[7], table[8], table[9],
                                   table[10], table[11], table[12])
            client.send(bytes(data_to_send, 'utf-8'))
        else: break