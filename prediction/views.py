from django.shortcuts import redirect, render
from django.contrib.auth.models import User
import cv2 
from deepface import DeepFace


from .models import User
from django.contrib import messages
from collections import Counter

def secondFrequent(list):
    dict = Counter(input)
 
    # Get the list of all values and sort it in ascending order
    value = sorted(dict.values(), reverse=True)
 
    # Pick second largest element
    secondLarge = value[1]
 
    # Traverse dictionary and print key whose
    # value is equal to second large element
    for (key, val) in dict.items():
        if val == secondLarge:
            print(key)
            return


def predict(request):
    return prediction()


def prediction():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(1)
    list = []

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        result = DeepFace.analyze(frame, actions = ["emotion"], enforce_detection=False)
        
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray,1.1,4)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)   

        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame, 
            result['dominant_emotion'],
            (50 ,50),
                font, 3,
                (0,0,255),
                2,
                cv2.LINE_4);
        cv2.imshow('Demo video', frame)

        
        list.append(result["dominant_emotion"])
        
        if cv2.waitKey(10) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows
    
    print(list)

    
    return redirect("home")

# Create your views here.
def home(request): 
    if "login" in request.session: 
        return render(request, "home.html")
    return redirect("login")
 
def login(request):
    if "login" in request.session:
        return redirect("home")
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            get_email = User.objects.get(email=email)
            if get_email.password == password:
                request.session["login"]=email
                return redirect('home')
            messages.add_message(request,messages.ERROR,"Please enter valid password.")
        except Exception as e:
            print(e)
            messages.add_message(request,messages.ERROR,"Please enter valid Email.")
            
    return render(request, "login.html")

def signUp(request):
    if "login" in request.session:
        return redirect("home")   
    if request.POST:
        email = request.POST["email"]
        firstName = request.POST["firstName"]
        password = request.POST["password"]
        Confirm_password = request.POST["Confirm_password"]
        if password == Confirm_password:
            obj = User()
            obj.email = email
            obj.firstName = firstName
            obj.password = password
            obj.Confirm_password = Confirm_password
            obj.save()
            return redirect("login")
        messages.add_message(request,messages.ERROR,"password and confirm password not match.")
    return render(request, "sign_up.html")

def logout(request):
    if "login" in request.session:
        del request.session["login"]
        return redirect("login")
    else:
        return redirect("login")

def aboutus(request):
    return render(request, "aboutus.html")
    