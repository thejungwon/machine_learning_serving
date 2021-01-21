import tensorflow as tf
def train():
    
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data(path='mnist.npz')
    
    
    # Normalize the train dataset
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    # Normalize the test dataset
    X_test = tf.keras.utils.normalize(X_test, axis=1)
    print("TRAIN")

    #Build the model object
    model = tf.keras.models.Sequential()
    # Add the Flatten Layer
    model.add(tf.keras.layers.Flatten())
    # Build the input and the hidden layers
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    # Build the output layer
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x=X_train, y=y_train, epochs=5) # Start training process
    # Evaluate the model performance
    test_loss, test_acc = model.evaluate(x=X_test, y=y_test)
    # Print out the model accuracy 
    print('\nTest accuracy:', test_acc)
    model.save("my_model")


if __name__ == "__main__":
    train()