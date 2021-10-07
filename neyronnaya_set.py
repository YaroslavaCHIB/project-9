from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, LSTM, GRU
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('C:\\Users\\teacher\\Desktop\\дз\\final_DataFrame.csv')
print(train)
# Максимальное количество слов 
num_words = 10000
# Максимальная длина новости
max_text_len = 10
# Количество classes
nb_classes = 52

labelencoder=LabelEncoder()

tmp = train['activity'].value_counts()
tmp = pd.DataFrame(tmp)
tmp = tmp.reset_index()
tmp.columns = ['activity', 'counts']
print(tmp)
tmp = tmp[tmp['counts'] != 1]
l = list(tmp['activity'])
print(l)
train = train.loc[train['activity'].isin(l)]
print(train)

text = train['name']
print(text)

train['activity']=labelencoder.fit_transform(train['activity'])
print(train)

y_train = utils.to_categorical(train['activity'] - 1, nb_classes)
print(len(y_train))


tokenizer = Tokenizer(num_words=num_words)

tokenizer.fit_on_texts(text)

tokenizer.word_index
print(tokenizer.word_index)

sequences = tokenizer.texts_to_sequences(text)
print(sequences)

index = 36
print(text[index])
print(sequences[index])

print(tokenizer.word_index['сегодня'])

x_train = pad_sequences(sequences, maxlen=max_text_len)
print(x_train[:5])

model_gru = Sequential()
model_gru.add(Embedding(num_words, 32, input_length=max_text_len))
model_gru.add(GRU(16))
model_gru.add(Dense(52, activation='softmax'))

model_gru.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
model_gru.summary()

model_gru_save_path = 'best_model_gru.h5'
checkpoint_callback_gru = ModelCheckpoint(model_gru_save_path, 
                                      monitor='val_accuracy',
                                      save_best_only=True,
                                      verbose=1)
history_gru = model_gru.fit(x_train, 
                              y_train, 
                              epochs=5,
                              batch_size=128,
                              validation_split=0.1,
                              callbacks=[checkpoint_callback_gru])
print(history_gru)                              

plt.plot(history_gru.history['accuracy'], 
         label='Доля верных ответов на обучающем наборе')
plt.plot(history_gru.history['val_accuracy'], 
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()