def read_img(path):
     img = keras.utils.load_img(path, target_size=(224,224))
     image_array = tf.keras.utils.img_to_array(img)
     return image_array