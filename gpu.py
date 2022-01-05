import  numpy
import face_recognition

image = face_recognition.load_image_file('img/abdo2.jpg')
face_location = face_recognition.face_locations(image)
print(face_location)
t,r,b,l = face_location[0]
face = image[t:b,l:r]


image1 = face_recognition.load_image_file('img/abdo2.jpg')
face_location1 = face_recognition.face_locations(image1)
print(face_location1)
t,r,b,l = face_location1[0]
face1 = image1[t:b,l:r]


encode = face_recognition.face_encodings(face)[0]

encode1 = face_recognition.face_encodings(face1)[0]

e= [encode]
print(len(encode1))
print(len(numpy.array(e)[0]))
res = face_recognition.compare_faces(e,encode1)
print(res)