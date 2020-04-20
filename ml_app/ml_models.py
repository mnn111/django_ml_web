from django.shortcuts import render
import getpass
from .forms import TitanicForm
from .models import TitanicDb

def rfc(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import pickle
    # titanic_model_nnkeras.sav
    with open('titanic_model.sav', 'rb') as m:
        randomforest = pickle.load(m)
        x = [[pclass, sex, age, sibhp, parch, fare, mbarked, title]]
        pred = randomforest.predict(x)
        # pred =123
        if pred == 0:
            pred = 'Will not Survive'
        elif pred == 1:
            pred = "Survive"
        else:
            pred = "Error occured"
    return pred


def keras_nn(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import numpy as np
    from keras.models import load_model

    model_predict = load_model('titanic_nn_keras.h5')


    person = np.array([[pclass, sex, age, sibhp, parch, fare, mbarked, title]])
    prediction_rate = model_predict.predict(person)

    if prediction_rate >.5 :
        prediction = "Survive"
    else:
        prediction = "Will not Survive"
    prediction_rate = round(prediction_rate[0][0]*100, 2)
    return prediction, prediction_rate

def titanic(request):
    if request.method == 'POST':
        form = TitanicForm(request.POST or None)
        if form.is_valid():
            form.save()


    last_entry = TitanicDb.objects.last()

    # id = last_entry.id
    pclass = last_entry.pclass
    sex = last_entry.sex
    age = last_entry.age
    sibhp = last_entry.sibhp
    parch = last_entry.parch
    fare = last_entry.fare
    mbarked = last_entry.mbarked
    title = last_entry.title

    pred = rfc(pclass, sex, age, sibhp, parch, fare, mbarked, title)
    # pred = 'testing'
    try:
        prediction, prediction_rate = keras_nn(pclass, sex, age, sibhp, parch, fare, mbarked, title)
    except:
        prediction = 'Not Suported/Error occured'
        prediction_rate = 'Not Suported/Error occured'

    last_entry.skl_result = pred
    last_entry.nn_result = prediction
    last_entry.nn_rate = prediction_rate
    last_entry.save()
    return render(request, 'titanic_pred.html', {'pred': pred,
                                               'prediction': prediction,
                                               'sur_rate': prediction_rate})