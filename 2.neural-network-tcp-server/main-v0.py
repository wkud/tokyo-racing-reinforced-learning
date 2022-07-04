import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np
import socket
import json

train_df = pd.read_csv('new2.csv', sep=';')
np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([
    keras.layers.Dense(16, input_shape=(6,), activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(9, activation='sigmoid')])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

x = np.column_stack((train_df.Velocity.values, train_df.Left.values, train_df.Left45.values,
                     train_df.Front.values, train_df.Right45.values, train_df.Right.values))

model.fit(x, train_df.Rotation.values, batch_size=1, epochs=10)





serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind(('', 38000))
serwer.listen(5)


def predict(v, l, l45, f, r45, r):
    v = float("{:.4f}".format(float(v)))
    l = float("{:.4f}".format(float(l)))
    l45 = float("{:.4f}".format(float(l45)))
    f = float("{:.4f}".format(float(f)))
    r45 = float("{:.4f}".format(float(r45)))
    r = float("{:.4f}".format(float(r)))
    pred = model.predict(np.array([[v, l, l45, f, r45, r]]))[0]
    q = 0
    index = 0
    for i in range(len(pred)):
        if q < pred[i]:
            q = pred[i]
            index = i
    if index == 3:
        # print('-1')
        return '-1'
    if index == 7:
        # print('1')
        return '1'
    # print('0')
    return '0'


while True:
    print('Czekam')
    client, address = serwer.accept()
    print('Połączono się z serwerem')
    while True:
        try:
            client.settimeout(5.0)
            msg = client.recv(1024)
            client.settimeout(None)
        except:
            break
        
        if len(msg) > 0:
            string_msg = msg.decode('utf-8')
            # print(string_msg)
            table = string_msg.split(';')
            data_to_send = predict(table[0], table[4], table[5], table[6], table[7], table[8])
            client.send(bytes(data_to_send, 'utf-8'))
        else: break
