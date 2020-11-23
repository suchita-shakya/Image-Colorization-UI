from django.shortcuts import render, redirect,get_object_or_404
from skimage.io import imsave

from frontend.models import Gallery,Team,AboutUs,Intro
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow import Graph
from skimage.color import rgb2lab, lab2rgb
from skimage.transform import resize
import numpy as np


model_graph = Graph()
with model_graph.as_default():
     tf_session = tf.compat.v1.Session()
     with tf_session.as_default():
        model = load_model('./models/my_model.h5')  #for loading h5 file


# Create your views here.
def index(request):
    team = Team.objects.all()   #displaying all the fields of table in db
    a_us = AboutUs.objects.all()
    intro = Intro.objects.all()
    context = {'team': team,'a_us': a_us,'intro': intro}

    return render(request, "index.html",context)


def image_upload(request):
    # image= request.POST.get("Input_image")

    # ref=Image(Input_image=image)
    # ref.save()
    # return render(request,"index.html")
    team = Team.objects.all()
    a_us = AboutUs.objects.all()
    intro = Intro.objects.all()
    if request.method == 'POST' and request.FILES['uploaded_image']:     
        image = request.FILES['uploaded_image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        uploaded_file_url = fs.url(filename)
        new_image = Gallery(Input_image=uploaded_file_url)
        new_image.save()

        test_image = load_img(image)
        img1_color = []
        img1 = img_to_array(test_image)
        img1 = resize(img1, (256, 256))
        img1_color.append(img1)
        img1_color = np.array(img1_color, dtype=float)
        img1_color = rgb2lab(1.0 / 255 * img1_color)[:, :, :, 0]
        img1_color = img1_color.reshape(img1_color.shape + (1,))

        with model_graph.as_default():
            with tf_session.as_default():
                output1 = model.predict(img1_color)
                output1 = output1 * 128
                result = np.zeros((256, 256, 3))
                result[:, :, 0] = img1_color[0][:, :, 0]
                result[:, :, 1:] = output1[0]

                # result_image= array_to_img(result)
                from PIL import Image
                # img = Image.fromarray(result, 'RGB')
                # filename1 = img.save('my.jpg')

                # result = Image.fromarray(np.uint8(result))

                # img = Image.fromarray(result)
                # filename1 = img.save('testrgba.jpg')
                # result_image = Image.fromarray(result,'RGB')
                # np_im = np_im - 18
                # new_im = Image.fromarray(np_im)
                # new_im.save("numpy_altered_sample2.png")
                # image1=imsave("newimg.jpg", lab2rgb(result))
                # result_image = fs.save( image1,lab2rgb(result))
                # image1 = request.FILES

                #fs.save(imagename,image)
                imsave("../colorization/media/output/"+image.name, lab2rgb(result))

                result_file_url = "/media/output/"+image.name
               
                new_image1 = Gallery(Output_image=result_file_url)
                new_image1.save()

        # result_image = Image(Output_image=result_file_url)
        # result_image.save()

        context = {'uploaded_file_url': uploaded_file_url, 'result_file_url': result_file_url,'team':team,'a_us': a_us,'intro': intro }
        
        return render(request, "index.html", context)


       


    else:
        return redirect('index/')

